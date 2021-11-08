# Django service for monitoring visits.

## About

In some premises, the employee stands for a specific purpose, for a specific time. For example, in a bank vault.

The service displays three web pages:
1. all active passes.
2. visits by pass.
3. who is indoors now.

## Install

Python3 must be installed (3.8.5+).

- Install requirements, use:
```
pip install -r requirements.txt
```
- Create .env file inside project dir.
- Add vars in .env, like:
```
DEBUG=true (or false)

SECRET_KEY=your_django_project_key

DB_HOST=your_db_host
DB_PORT=your db_port
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
```

## Getting Started 

```
python manage.py runserver 0.0.0.0:8000
```

## Project goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/)
