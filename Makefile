run:
	python3 manage.py runserver
migrate:
	python3 manage.py makemigrations
	python3 manage.py migrate
super:
	python3 manage.py createsuperuser
venv:
	source venv/bin/activate
celery:
	celery -A celery worker -l debug
