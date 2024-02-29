import json
from django.urls import reverse
import pytest

from task_tracker.tasks.models import Task
from task_tracker.tasks.tests.factories import TaskFactory

def get_new_task():
    return {
        "name": "Task test",
        "description": "Descripcion larga muy muy larga",
        "estimate": 30,
        "state": "planned"
    }

@pytest.mark.django_db
def test_create_task_successful(client):
    new_task = get_new_task()
    response = client.post("/tasks/", data=new_task)
    response_body = response.data
    assert response.status_code == 201
    assert response_body["name"] == new_task["name"]
    assert response_body["description"] == new_task["description"]
    assert response_body["estimate"] == new_task["estimate"]

def test_create_task_fail(client):
    new_task = get_new_task()
    new_task["state"] = "completed"
    response = client.post("/tasks/", data=new_task)

    assert response.status_code == 400
    assert response.data == {"state": ["Task can only be created in Planned state"]}

@pytest.mark.django_db
def test_change_state(client):
    task = TaskFactory()
    payload = {
        "state": "progress"
    }
    response = client.patch(f"/tasks/{task.id}/", data=json.dumps(payload), content_type="application/json")

    task.refresh_from_db()
    assert response.status_code == 200
    assert task.state == payload["state"]

@pytest.mark.django_db
def test_status(client):
    task_1 = TaskFactory()
    task_2 = TaskFactory(estimate=5.0)
    task_3 = TaskFactory(state="completed", estimate=2.0)

    response = client.get("/tasks/status/")
    response_body = response.data
    assert response.status_code == 200

    assert response_body["planned"] == task_1.estimate + task_2.estimate
    assert response_body["progress"] == 0
    assert response_body["completed"] == task_3.estimate

@pytest.mark.django_db
def test_filters_successful(client):
    task_1 = TaskFactory()
    task_2 = TaskFactory(estimate=5.0)
    task_3 = TaskFactory(state="completed", estimate=2.0)

    response = client.get("/tasks/")
    assert response.status_code == 200
    
    for state in Task.TASK_STATES:
        response_2 = client.get(f"/tasks/?state={state}")
        for task in response_2.data:
            assert task["state"] == state

@pytest.mark.django_db
def test_filters_failed(client):
    task_1 = TaskFactory()
    response = client.get(f"/tasks/?state=invalid_state")

    assert response.status_code == 400
