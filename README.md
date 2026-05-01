# Library Management

A small Flask app for managing books, members, borrowing, returns, and transaction history.

This project is now set up to use `uv` for dependency management and commands. If you are running the app locally, use `uv` for install, database setup, and development commands.

## What it does

- Create, update, list, and delete books
- Create, update, list, and delete members
- Borrow and return books
- Track transactions
- Search books by title or author
- Import books from the Frappe library API
- View simple reports for popular books and paying members

## Tech stack

- Python 3.13
- Flask
- Flask-SQLAlchemy
- Flask-WTF
- SQLAlchemy
- SQLite for local development
- `uv` for environment and dependency management

## Quick start

```sh
git clone https://github.com/Emonemon74/library-management.git
cd flask-library-management
uv sync
cp .env.example .env
```

Create the local database:

```sh
uv run python - <<'PY'
from library import app, db

with app.app_context():
    db.create_all()
    print("Created DB tables")
PY
```

Start the development server:

```sh
uv run flask --app app run
```

The app will use a local SQLite database at `instance/library.db`.

## Environment variables

Create a `.env` file in the project root. You can start from `.env.example`.

Example:

```env
FLASK_ENV=dev
SECRET_KEY=replace-this-with-a-random-long-string
SQL_DATABASE_URL=sqlite:///library.db
```

Notes:

- `SECRET_KEY` is required for sessions, forms, and flash messages.
- In local development, `SQL_DATABASE_URL` defaults to `sqlite:///library.db` if you do not set it.
- In non-dev environments, `SQL_DATABASE_URL` and `SECRET_KEY` should be set explicitly.

## Setup details

### 1. Install dependencies

```sh
uv sync
```

This installs the dependencies declared in `pyproject.toml` and uses `uv.lock` for reproducible local setup.

### 2. Create the database

Run this once when setting up the project, and again only if you delete the SQLite file and need to recreate it.

```sh
uv run python - <<'PY'
from library import app, db

with app.app_context():
    db.create_all()
PY
```

### 3. Run the app

```sh
uv run flask --app app run
```

### 4. Production-style command

If you want to run the app with Gunicorn:

```sh
uv run gunicorn app:app
```

## Common commands

```sh
uv sync
uv run flask --app app run
uv run python
uv run gunicorn app:app
```

## Project structure

```text
.
├── app.py
├── library/
│   ├── __init__.py
│   ├── forms.py
│   ├── models.py
│   ├── routes/
│   └── templates/
├── pyproject.toml
├── requirements.txt
└── uv.lock
```

## Screenshots

### Home

![Home](screenshots/Screenshot%20(128).png)

### Books

![Books](screenshots/Screenshot%20(129).png)
![Create book](screenshots/Screenshot%20(130).png)

### Import from Frappe

![Import](screenshots/Screenshot%20(131).png)

### Borrow

![Borrow](screenshots/Screenshot%20(132).png)

### Transactions

![Transactions](screenshots/Screenshot%20(134).png)

### Search

![Search](screenshots/Screenshot%20(136).png)

### Reports

![Top books](screenshots/Screenshot%20(137).png)
![Top members](screenshots/Screenshot%20(138).png)

### Return

![Return](screenshots/Screenshot%20(142).png)
