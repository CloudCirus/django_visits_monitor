# Django service for monitoring visits.

## About

In some premises, the employee stands for a specific purpose, for a specific time. For example, in a bank vault.

The service displays three web pages:
1. all active passes.
2. visits by pass.
3. who is indoors now.

## Install

Python3 must be installed (3.8.5+).

1. Install requirements, use:
```
pip install -r requirements.txt
```
2. Create .env file inside project dir.
3. Add vars into .env, like:
```
ALLOWED_HOSTS=localhost,127.0.0.1,0.0.0.0
```
```
SECRET_KEY=your_django_project_key
```
Without DEBUG var default set is False.
```
DEBUG=True
```
Postgres DB example:
```
DB_URL=postgres://db_name:db_password@db_host:db_port/db_name
```

## Getting Started 

```
python manage.py runserver 0.0.0.0:8000
```

## Project goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/)
