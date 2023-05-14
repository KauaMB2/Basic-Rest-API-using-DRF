<h2>BASIC API USING DJANGO REST FRAMEWORK</h2>

1. Create a new virtual environment (optional)
2. Install Django and Django REST framework using pip
3. Create a new Django project using the django-admin command line tool
4. Create a new Django app within the project using the manage.py command line tool
5. Create models within the app, defining their fields and relationships
6. Create serializers to convert models to JSON and vice versa
7. Create views that handle HTTP requests and responses, using the serializers to serialize/deserialize data
9. Map the views to URLs using Django's URL routing system

Create a new Django project:
```django-admin startproject project_name```

Create a new Django application:
```python manage.py startapp application_name```

Create a database:
```python manage.py migrate```

Make migrations:
Create a database:
```python manage.py makemigrations```

Create a admin:
```python manage.py createsuperuser```

Run a Django project:
```python manage.py runserver```

