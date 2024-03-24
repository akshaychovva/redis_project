FROM python:3.13-rc-bookworm

ENV PYTHONBUFFERED=1

WORKDIR /django

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD python manage.py redis_project.wsgi:application --bind 0.0.0.0:8000

EXPOSE 8000
