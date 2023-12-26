# below code is for building image with docker compose file
# FROM python:3.10.7-slim

# ENV PYTHONDONTWRITEBYTECODE=1

# ENV PYTHONUNBUFFERED=1

# WORKDIR /app

# COPY requirements.txt /app/requirements.txt

# RUN pip install -r requirements.txt

# COPY . /app



# below code is for building image with docker build command independently
FROM python:3.10.7-slim

ENV PYTHONUNBUFFERED 1

# NOTE: these variables are needed to be uncomment when we want to run the image on docker not required for kubernetes

# ENV DB_HOST=mysql
# ENV DB_PORT=3306
# ENV DB_NAME=contact
# ENV DB_USER=root
# ENV DB_PASSWORD=Albatros@47

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . /app

EXPOSE 8000

# NOTE: this below line is needed to be uncomment when we want to run the image on docker not required for kubernetes
CMD python3 manage.py migrate && python3 manage.py runserver 0.0.0.0:8000

# CMD python3 manage.py migrate

# commands to build image and run container out of it
# docker build -t contact-api .
# docker run --name contact-api-container -p 8000:8000 --network contact_contact contact-api
