FROM python:3.9

RUN apt-get update
RUN pip3 install django
RUN pip3 install djangorestframework
WORKDIR /usr/src/app
COPY . .
EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0:8000"]
