<!-- python manage.py makemigrations -->
python manage.py createsuperuser
python manage.py collectstatic

<!-- using pipenv -->
pipenv install ...
<!-- post gres commands -->
\l --list all databases
\c DBNAME use database
\dt show tables
<!-- deployment -->
heroku login
heroku create APPNAME
git push heorku master
heroku config
heroku config:set EMAIL_HOST_PASSWORD=....
heroku addons:create heroku-postgresql:hobby-dev
heroku config -s | grep DATABASE_URL
heroku config -s | grep DATABASE_URL