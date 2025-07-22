start: before-run run

dev: build-static before-run compose-run

build-static:
	uv run manage.py collectstatic --noinput
	npm run build

migrations:
	uv run manage.py makemigrations
	uv run manage.py migrate

compose-run:
	docker-compose up

before-run: migrations

run:
	uv run gunicorn app.wsgi --bind 0.0.0.0:8000