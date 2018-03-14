# intranet
A RESTful intranet-like website based on Django REST Framework

## 1- Introduction

   This project has been created in an attempt to learn how to use Django, Django Rest Framework, Ajax and more.
   
   I've created it under MIT license, so knock yourself out with it.
   
   It is based on my house, which is a colocation I share with 7 other people.

   I've decided to create a basic intranet in order to get to know who is who. This does not aim to go live, though.

## 2- Before starting
### 2.1- Technologies used
* [Python v3.6.3](https://www.python.org/)
* [Django v1.11.4](https://www.djangoproject.com/)
* [Django Rest Framework v3.4.0-2](http://www.django-rest-framework.org/)
* [Bootstrap v4.0.0-beta](https://getbootstrap.com/)
* [Font-Awesome v4.7.0](https://fontawesome.com/)
* [MDBootstrap v4.4.1 Free](https://mdbootstrap.com/)
* [jQuery v3.2.1](https://jquery.com/)
* [Popper](https://github.com/FezVrasta/popper.js)
* [Eclipse (Oxygen) v.7.2](https://www.eclipse.org/)
* PyDev (Eclipse AddOn)

I also took some code samples from tutorials, and will try to cite them as best as possible :
* [OpenClassrooms](https://openclassrooms.com/)
* [Real Python](https://realpython.com/)
* [W3Schools](https://www.w3schools.com/)

### 2.2- How to install
I won't describe the processus to install Eclipse, PyDev, Python, ... There are a million other tutorials doing it way better than me

1. Create an Eclipse PyDev project where you want (the basic DB PyDev creates must be named db.sqlite3)
2. If you want, create a python venv in the directory created
3. Download the git project
4. Unzip it
5. Copy all the files located in ikoab_elise/ to the Eclipse project folder
6. As the Django project private key and database are to be avoided in a git repository, they have been moved in a module called secret.py

   I suggest you create a dummy django project somewhere and use its private key in ikoab_elise 
   
   You have to create a new secret.py file in ikoab_elise/ikoab_elise/ and add the following code :

```python   
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '[your own private key]'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

7. Reopen the project in Eclipse and refresh it (all the files added should now appear)
8. Perform the Make Migrations and Migrations operations to create the database tables

## 3- The project
### 3.1- The applications
#### 3.1.1- api
This application provides the basic API used by the site (or any other external appliance for that matter).

It contains :
* The model Person, used to store people living in the house in the database
* The model serializer, PersonSerializer, which is used to serialize Person objects to json
* The api views itself, which takes care of CRUD requests, and maps them to RESTful requests
* Unit tests inherited from django.test.TestCase

#### 3.1.2- web
This is the website itself. It renders pages depending on the user's actions.

Both pages are rendered with the help of html pages under templates/ and web/templates/, and use a base of Ajax for asynchronous communication with the server.

It doesn't contain any low-level or DB-related treatment. It instead relies on the api to handle it.

It consists of two pages :
* Home : displays all the people living in the house
* Badge : displays the informations of a person

It contains :
* Views for both pages
* Forms modules to render forms directly from the database models
* Unit tests inherited from django.test.TestCase
