FROM ubuntu:trusty
RUN sudo apt-get -y update
RUN sudo apt-get -y upgrade
RUN sudo apt-get install -y sqlite3 libsqlite3-dev

FROM python:3.7.3-slim
COPY /src/requirements.txt /
RUN pip3 install -r /requirements.txt
COPY /src /app
WORKDIR /app
RUN mkdir -p /app/db_folder
CMD ["gunicorn" ,"main:app", "-w", "2", "--threads", "2", "-b", "0.0.0.0:8000"]

