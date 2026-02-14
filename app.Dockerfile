FROM python:3.14.3-alpine3.23
COPY ./requirements.txt /requirements.txt
RUN ["pip", "install", "-r", "/requirements.txt"]
COPY ./.pg_service.conf /root/.pg_service.conf
COPY ./.pgpass /root/.pgpass
WORKDIR /app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
