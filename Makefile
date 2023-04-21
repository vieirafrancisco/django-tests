run:
	@echo "> 🚀 Starting server"
	poetry run python manage.py runserver

build:
	@echo "> 💻 Run migrations"
	poetry run python manage.py migrate
	@echo "> 💻 Run collectstatic"
	poetry run python manage.py collectstatic --no-input

collectstatic:
	@echo "> 💻 Run collectstatic"
	poetry run python manage.py collectstatic --no-input

makemigrations:
	@echo "> 💻 Run makemigrations"
	poetry run python manage.py makemigrations

migrate:
	@echo "> 💻 Run migrations"
	poetry run python manage.py migrate
 