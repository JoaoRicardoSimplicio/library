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

1. Build the app image
```bash
make build
```

2. Up the containers
```bash
make run
```

3. Apply migrations
```bash
make migrate
```

## API Usage

1. Generates static files
```
make collectstatic
```

**NOTE**: It's a prerequisite to generate static files before access docs endpoint

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
