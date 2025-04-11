seeds:
	docker compose exec app python3 manage.py book_seeds --include-online

test:
	docker compose exec app pytest

build:
	docker build -t library-app:latest .

run:
	docker compose up -d

migrate:
	docker compose exec app python3 manage.py migrate

collectstatic:
	docker compose exec app python3 manage.py collectstatic
