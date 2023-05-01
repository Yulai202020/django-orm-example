### install django
pip3 install django

django-admin startproject mysite

mysite/.env

    DATABASE_URL = 'postgres://user:password@localhost:port/databse'

mysite/settings.py
```python
import os
from dotenv import load_dotenv
load_dotenv() 
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "postgres",
        "DATABASE_URL": os.environ.get("DATABASE_URL")
    }
}
```
### create app

python3 manage.py startapp student

### create model

student/models.py
```py
from django.db import models

class Teacher(models.Model):
    firstname = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)

    def __str__(self):
        return self.firstname

class Student(models.Model):
      
    firstname = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    age = models.IntegerField()
    classroom = models.IntegerField()
    teacher = models.CharField(max_length=100)

    def __str__(self):
        return self.firstname
```

### migrate to the database

python3 manage.py makemigrations

python3 manage.py migrate