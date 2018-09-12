FROM tiangolo/uwsgi-nginx-flask:python3.6

COPY ./app /app
COPY ./requirements.txt /app/requirements.txt

RUN pip3 install -r /app/requirements.txt
