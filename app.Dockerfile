FROM python:3.14.3-alpine3.23
COPY ./requirements.txt /requirements.txt
RUN ["pip", "install", "-r", "/requirements.txt"]
WORKDIR /app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
