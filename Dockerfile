FROM python:3.9
LABEL maintainer="Aaron Vigal admin@aaronvigal.com"

RUN pip install pipenv

WORKDIR /usr/src/app
COPY main.py .
COPY Pipfile .
COPY hsctf-feedback-53e1011913d3.json .

RUN mkdir /certs
COPY server.crt /certs
COPY server.key /certs

RUN pipenv install

ENV FLASK_APP main.py
CMD ["pipenv", "run", "gunicorn", "-w", "4", "-b", ":443", "--certfile", "/certs/server.crt", "--keyfile", "/certs/server.key", "main:app" ]
EXPOSE 443