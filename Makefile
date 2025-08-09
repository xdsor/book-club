start: before-run run

dev:
	uv run manage.py runserver

build-static:
	uv run manage.py collectstatic --noinput
	npm run build

migrations:
	uv run manage.py makemigrations
	uv run manage.py migrate

compose-run:
	docker-compose up --build

before-run: migrations

run:
	uv run gunicorn app.wsgi --bind 127.0.0.1:8000