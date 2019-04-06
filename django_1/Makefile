.PHONY: build

build:
	python manage.py collectstatic --noinput
	python manage.py runserver 0.0.0.0:8000

migrations:
	python manage.py makemigrations
	python manage.py migrate

run:
	python manage.py runserver 0.0.0.0:8000

static:
	python manage.py collectstatic --noinput
