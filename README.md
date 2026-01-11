# Simple Python Web Server

[![Release App](https://github.com/Ilkar20/simple-python/actions/workflows/main.yml/badge.svg)](https://github.com/Ilkar20/simple-python/actions)
![Docker Pulls](https://img.shields.io/docker/pulls/hkyiyi/python-app)
![Deployment Status](https://img.shields.io/badge/Render-Live-brightgreen?logo=render&logoColor=white)

This repository contains a simple web application written in Python. It was created as part of the "DevOps with Docker" MOOC to demonstrate a full CI/CD pipeline, including automated image publishing and cloud deployment.

## 🚀 Live Application
The application is automatically deployed to Render on every push to the `main` branch.  
**View the live site here:** [https://simple-python-wcv8.onrender.com](https://simple-python-wcv8.onrender.com)

## 🛠️ Deployment Pipeline
The pipeline is managed via **GitHub Actions** and follows these steps:
1. **Build & Push:** Creates a multi-platform Docker image and pushes it to [Docker Hub](https://hub.docker.com/r/hkyiyi/python-app).
2. **Continuous Deployment:** Triggers a webhook to **Render**, which pulls the latest image and updates the live service.

## 📦 How to Run Locally

### From Docker Hub
You can run the pre-built image directly without needing the source code:
```bash
docker run -p 8000:8000 hkyiyi/python-app