# # pull official base image
# FROM python:3.10.4-slim-buster

# # set work directory
# WORKDIR /usr/src/app

# # set environment variables
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

# # Install system dependencies
# RUN apt-get update && apt-get install -y \
#     netcat \
#     cmake \
#     redis-server \
#     build-essential
    
# # # install system dependencies
# # RUN apt-get update && apt-get install -y netcat
# # RUN apt-get install -y redis-server

# # install dependencies
# RUN pip install --upgrade pip
# COPY ./requirements.txt .
# RUN pip install -r requirements.txt

# # copy project
# COPY . .

# # Expose ports
# EXPOSE 8000

# # Start Redis and celery worker in the background
# CMD python manage.py migrate && python manage.py collectstatic --no-input && service redis-server start && exec gunicorn core.wsgi:application --bind 0.0.0.0:8000