# Random Exchange

A minimal Q&A web app built with Flask.

Users can create accounts, ask questions, and post answers.

---

## Features

- User registration and login
- Ask questions
- Post answers
- Password hashing with Flask-Bcrypt
- Form validation using Flask-WTF
- SQLite database with SQLAlchemy
- Database migrations using Flask-Migrate
- Flash messages for user feedback

---

## Tech Stack

- Python
- Flask
- Flask-SQLAlchemy
- Flask-Login
- Flask-WTF
- Flask-Bcrypt
- Flask-Migrate
- SQLite
- Bootstrap

---

## Setup

### Clone the repository

```bash
git clone <your-repo-url>
cd random_exchange
```

### Create virtual environment

#### Linux/macOS

```bash
python -m venv venv
source venv/bin/activate
```

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Project

```bash
python run.py
```

Open in browser:

```text
http://127.0.0.1:5000
```

---

## Database Migration

Initialize migrations:

```bash
flask db init
```

Create migration:

```bash
flask db migrate -m "initial migration"
```

Apply migration:

```bash
flask db upgrade
```

---

## Project Structure

```text
.
├── app
│   ├── database
│   ├── static
│   │   ├── css
│   │   ├── images
│   │   └── js
│   ├── templates
│   │   └── components
│   ├── forms.py
│   ├── models.py
│   ├── routes.py
│   └── __init__.py
├── migrations
├── config.py
├── requirements.txt
├── run.py
└── LICENSE
```

---

## Environment Variables

Create a `.env` file:

```env
SECRET_KEY=your_secret_key
```

---

## .gitignore

```gitignore
venv/
__pycache__/g
*.pyc
instance/
app/database/*.db
.env
```

---

## Status

MVP in development.
