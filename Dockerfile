FROM python:3.8-alpine
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=finorg.settings
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install waitress

workdir /django
RUN mkdir -p /django/static
COPY requirements.txt requirements.txt
COPY . /django

RUN pip3 install -r requirements.txt
RUN python manage.py collectstatic 



