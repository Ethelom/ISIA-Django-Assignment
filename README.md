# ISIA-Django-Assignment

This is the Django assignment of September 2020 for the ISIA course. The use case implemented was the "Store Review", where a customer
can review a store after a confirmed purchase.

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
