FROM python:3.14.3-alpine3.23
COPY ./requirements.txt /requirements.txt
RUN ["pip", "install", "-r", "/requirements.txt"]
WORKDIR /app
# Temporary CMD
CMD ["top"]
