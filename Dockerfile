FROM python:3.12

WORKDIR /code/

RUN pip install --upgrade pip

COPY ./requirements.txt /code/requirements.txt
COPY ./task_tracker /code/

RUN pip install -r /code/requirements.txt

EXPOSE 8000

RUN python manage.py migrate

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]