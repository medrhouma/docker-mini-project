
# DevOps Flask Application

## Description
A simple Flask web application containerized with Docker.

## Technologies
- Python 3.12
- Flask 3.1.2
- Docker

## Docker Hub
Image: medrhouma/devops-flask-app

Available versions:
- 1.0.0
- 1.0.1
- 1.0

## Download the image

docker pullmedrhouma/devops-flask-app:1.0.1

## Run the application

docker run -d \
  --name flask-container \
  -p 5000:5000 \
  -e APP_MESSAGE="Hello from Docker!" \
  -e APP_VERSION="1.0.1" \
  --memory=256m \
  --cpus=0.5 \
  TON_USERNAME/devops-flask-app:1.0.1

## Access the application

http://localhost:5000

Health check:
http://localhost:5000/health

## Environment variables

| Variable | Default value |
|---|---|
| APP_MESSAGE | Welcome message |
| APP_VERSION | 1.0.0 |

## Resource limits
- Memory: 256 MB
- CPU: 0.5 core

## Stop the container

docker stop flask-container

## Remove the container

docker rm flask-container
