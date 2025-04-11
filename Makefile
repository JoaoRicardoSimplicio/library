seeds:
	docker compose exec app python3 manage.py book_seeds --include-online

test:
	docker compose exec app pytest
