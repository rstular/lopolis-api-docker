FROM tiangolo/uwsgi-nginx-flask:python3.6

RUN apt-get update && apt-get install -y python3-pip

COPY ./app /app
COPY ./requirements.txt /app/requirements.txt

RUN pip3 install -r /app/requirements.txt