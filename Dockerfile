FROM python:3.5-alpine

COPY ./app /app
COPY ./requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

WORKDIR /app

CMD [ "gunicorn", "--workers", "100", "-b", ":80", "main:app" ]
