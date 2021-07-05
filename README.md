<div align='center'>
  
# Canoo Home Automation App
  
### Overview
  
This application uses interactive tables to let users Create, Read, Update and Delete (CRUD) lights and thermostats for home automation. There is also a history log table that tracks all these events. This is done by connecting a React UI frontend to a Flask + MongoDB backend through a REST API. Detailed documentation on the REST API commands can be found in: [commands.txt](https://github.com/LevonAr/canoo-app-v2.0/blob/main/backend/commands.txt).

Here is a simple overview diagram of this application's architecture:

![Architecture Diagram](https://github.com/LevonAr/canoo-app-v1.0/blob/main/CanooDiagram.svg)
  

### Features of the project:
Frontend backed by Next.js giving optimized server side rendering
  
Clean design and responsive pages.
  
Form validations and proper error handling.
  
Detailed log visualization of each step.
  
Dockerized application makes app easy to install and launch within minutes.
  
Made with keeping scalibilty in mind.
  
Focused on application security.
  
  
### Technologies
  
![](https://img.shields.io/badge/Python-Language-informational?style=for-the-badge&logo=python&logoColor=white&color=2bbc8a)
![](https://img.shields.io/badge/Javascript-Language-informational?style=for-the-badge&logo=javascript&logoColor=white&color=2bbc8a)

![](https://img.shields.io/badge/Flask-Tool-informational?style=for-the-badge&logo=flask&logoColor=white&color=2bbc8a)
![](https://img.shields.io/badge/React-Tool-informational?style=for-the-badge&logo=react&logoColor=white&color=2bbc8a)
![](https://img.shields.io/badge/Docker-Tool-informational?style=for-the-badge&logo=docker&logoColor=white&color=2bbc8a)
![](https://img.shields.io/badge/MongoDB-Tool-informational?style=for-the-badge&logo=mongodb&logoColor=white&color=2bbc8a)
![](https://img.shields.io/badge/Next-Tool-informational?style=for-the-badge&logo=next.js&logoColor=white&color=2bbc8a)

</div>




# Getting Started

Prerequisites: Install Docker. For instructions on how to do this see [official documentation](https://docs.docker.com/get-docker/).

## Step 1: Clone

#### `git clone https://github.com/LevonAr/canoo-app-v2.0.git`

#### `cd canoo-app-v2.0`

Clone this repository on your local machine. Then navigate into it.

## Step 2: Run Backend

#### `cd backend`
#### `docker-compose up -d` (this may take some time for first build).
Once running, navigate to: http://localhost:8000

Browser should display "hello world!", indicating server is operating properly.

## Step 3: Run Frontend

#### `cd ../`
#### `cd frontend`
#### `docker-compose up -d`(this may take some time for first build).
Once running, navigate to: http://localhost:3000

Browser should display application.


# Testing

Navigate to root directory.
#### `cd backend`
#### `pip install -r requirements.txt`
#### `python tests.py`
