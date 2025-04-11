# Library

Application that stores and handles books data

## Environment variables Setup

1. Copy `.env.example` to `.env`:
```bash
cp .env.example .env
```

2. Edit `.env` and set your secrets:
It's important that you set the following variables:
- POSTGRES_DB
- POSTGRES_USER
- POSTGRES_PASSWORD
- DJANGO_SECRET_KEY

You can use the follow code to generate a new DJANGO_SECRET_KEY:
```python3
import secrets
import string

print(''.join(secrets.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(50)))
```

## Run application

```bash
docker compose up -d --build
```

## API Usage

Access the endpoint `/docs` to get information about how to use the endpoints available in the Library API

## Tests

**NOTE**: It's a prerequisite to have your containers running to run this command

```bash
make pytest
```

## Seeds

**NOTE**: It's a prerequisite to have your containers running to run this command

```bash
make seeds
```
