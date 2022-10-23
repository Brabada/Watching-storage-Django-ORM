# Simulation of vault's access system

Django-based learning project that shows list of employees with access to vault, their access cards, employees that's currently in vault and level of suspicious.

Project working on localhost http://127.0.0.1:8000/ by default. List of employees fetching from external DB: checkpoint.devman.org

There is three pages:
- Main page with list of employees with access to vault (http://127.0.0.1:8000/);
- Page with list of current visitors of vault with entry time and duration of visit (http://127.0.0.1:8000/storage_information/);
- Card with visits of employer. There is access from main page by clicking on employer (http://127.0.0.1:8000/passcard_info/)


### How to install
For start you need `Python3` and `pip`.

For installing required packages:
```shell
$ cd "path_where_is_script"
$ pip install -r "requirements.txt"
```

## How to launch
Add to `.env` next parameters:
```text
export DB_HOST=
export DB_PORT=
export DB_NAME=
export DB_USERNAME=
export DB_PASSWORD=
export DB_SECRET_KEY=
export DEBUG=False
```

Then launch server:
```shell
$ cd "path_where_is_script"
$ python manage.py runserver
```

Then open http://127.0.0.1:8000/ in browser.
