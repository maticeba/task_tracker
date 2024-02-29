# task_tracker

## Excecute the app
This app is dockerized to prevent any conflict in dependencies 

### Requirements
- Docker
- Docker compose

### Run the app
- Build the project "docker-compose build" (for docker compose v1) / "docker compose build" (for docker compose v2)
- Run the project "docker-compose up" (for docker compose v1) / "docker compose up" (for docker compose v2)

For the first time the project is build you need to run the migrations
- docker exec -it task_tracker bash
- python manage.py migrate

## Endpoints

### [GET] /tasks/
Returns a list of all tasks 

Response model: 

```
[{
    "id": 2,
    "name": "Task 2",
    "description": "Descripcion larga muy muy larga",
    "estimate": 30.0,
    "state": "completed"
}]
```
Params:

- state: options ["planned", "progress", "completed"]


### [POST] /tasks/
Create a task

Payload Model:

```
{
    "name": "Task 2",
    "description": "Descripcion larga muy muy larga",
    "estimate": 30.0,
    "state": "planned"
}
```

Note: Tasks can only be created in planned state

### [DELETE] /tasks/{id}
Deletes a task

### [POST] /tasks/{id}/state/
Updates a task state

Payload Model:

```
{
    "state": "progress"
}
```

### [GET] /tasks/status/
Returns the sum of all hours for each task state

Response Model:

```
{
    "planned": 3.0,
    "progress": 0,
    "completed": 20.0
}
```