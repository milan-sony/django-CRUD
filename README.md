
# Django-CRUD_MySQL

This is a simple project that perfroms CRUD operations in Django using Mysql database.
## Run Locally
You will need to install Python on  you system. Head over to https://www.python.org/downloads/ to download python.

Once you have downloaded Python on your system, 
run the following command inside your git enabled terminal

```bash
  git clone https://github.com/milan-sony/Django_CRUD.git
```

Then go to the project folder

```bash
  cd Django_CRUD
```
(This is optional, but strongly recommended) Make a virtual environment

```bash
  python -m venv venv
```
Activate the virtual environment

```bash
  venv/Scripts/activate
```

Install the dependencies needed for this project

```bash
  pip install -r requirement.txt
```
Now minimize the terminal and make a database on MySQL named django_crud

Once you have created the database, head back to the terminal and make migrations

```bash
  python manage.py makemigrations
```
This will create all the migration files (database migrations) required to run this project

Now apply this migrations

```bash
  python manage.py migrate
```

Then run the server

```bash
  python manage.py runserver
```

Once the server is hosted click on the link http://127.0.0.1:8000/


