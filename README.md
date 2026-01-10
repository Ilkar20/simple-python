# Simple Python Web Server

This repository contains a simple web application written in Python. It was created as part of the "DevOps with Docker" MOOC to demonstrate image publishing and cloud deployment.

## Description
The application uses Python's `http.server` module to serve a basic HTML response. It is designed to be lightweight and portable using Docker.

## How to Run
You can run this application directly from Docker Hub without needing the source code.

### From Docker Hub
You can run the pre-built image directly from Docker Hub:
```bash
docker run -p 8000:8000 hkyiyi/python-app 
