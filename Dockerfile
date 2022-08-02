# pull official base image
FROM python:3.9.13-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1



# copy project
COPY . .

# install dependencies
RUN pip install --upgrade pip

RUN pip install -r requirements.txt