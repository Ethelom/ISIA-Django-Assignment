# ISIA-Django-Assignment

This is the Django assignment of September 2020 for the ISIA course. The use case implemented was the "Store Review", where a customer
can review a store after a confirmed purchase.

The project contains two apps: **store_review** and **home**. The first one concerns the implemented use case, whereas the second one
regards the index, which gives access to the use case.

Moreover, there are two folders (static/ and templates/) that do **NOT** pertain to a specific app and as such belong
to the whole project. Thus, they can be found at the same directory level with the apps.
This is encouraged according to the Django [docs](https://docs.djangoproject.com/en/3.1/howto/static-files/).

Of course, each app has each own static/ and templates/ folders, but those can be found in each app's respective folder.

# Dependencies and Run
In order to install the dependencies run the following commands in the root:

* If [Pipenv](https://pipenv.pypa.io) is not already installed run:

```
pip install pipenv
```

* In order to specify what python version the virtual environment is going to use, you can run:
```
pipenv --python path/to/python.exe
```
The project uses Python 3.7.9 by default as this is a stable version.

* Create a virtual environment:
```
pipenv shell
```

* Install the required dependencies from Pipfile:
```
pipenv install --dev
```

* Change directory by running:

``` 
cd enterprice/
```

* Now that Django (as well as other dependencies) have been installed in your virtual environemnt, you can run the local server:

```
python manage.py runserver
```
You should expect something like the following:

>System check identified no issues (0 silenced).
October 14, 2020 - 00:07:17
Django version 3.1.2, using settings 'enterprice.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

* Open your browser and paste the above local URL.

# Accounts
You can login as one of the following customers:
1. username: t8170136 / password: Theodosis14
2. username: tommy / password: djangotommy

From the navbar navigate to "My purchases" in order to see what purchases you've made so far.
There, you can choose to either make a new store review or edit an existing one.
Each store has all the reviews concerning it gathered at its own profile.
