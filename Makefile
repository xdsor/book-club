start: run

dev: build compose-run

build:
	uv run manage.py collectstatic --noinput
	npm run build

compose-run:
	docker-compose up

run:
	uv run gunicorn app.wsgi --bind 0.0.0.0:8000