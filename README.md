# Little Lemon

Little Lemon is a Django-based restaurant management and booking application built as part of the Coursera Back-End Developer Capstone project. The project combines a Django web frontend with a REST API for menu management and table reservations, along with authentication support for secure access.

## Overview

This project is designed to simulate a real-world restaurant backend. It allows users to:

- View and manage the restaurant menu
- Book tables for upcoming visits
- Authenticate and access protected API endpoints
- Explore a simple restaurant landing page built with Django templates and static assets

## Tech Stack

- Python
- Django
- Django REST Framework
- Djoser
- MySQL
- HTML / CSS
- Django Templates

## Project Structure

```text
LittleLemon/
├── littlelemon/              # Django project settings and routing
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── restaurant/              # Main app
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   └── migrations/
├── templates/               # Django HTML templates
│   └── index.html
├── static/                  # CSS, images, and other static files
├── tests/                   # Test files
├── manage.py
├── requirements.txt
├── README.md
├── .gitignore
└── ...
```

## Features

- Menu management via REST API
- Table booking API with authentication
- User registration and token-based authentication support
- Django admin integration
- Restaurant landing page and branding
- Structured backend built with Django REST Framework

## Getting Started

### Prerequisites

Make sure you have the following installed:

- Python 3.x
- pip
- virtualenv (recommended)

### Installation

1. Clone the repository:

```bash
git clone https://github.com/mTornam/LittleLemon.git
cd LittleLemon
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Configure the database in `littlelemon/settings.py` if needed.

5. Apply database migrations:

```bash
python manage.py migrate
```

6. Run the development server:

```bash
python manage.py runserver
```

7. Open the app in your browser:

```text
http://127.0.0.1:8000/restaurant/
```

## API Endpoints

### Authentication

These routes are provided through Django authentication tools and Djoser:

- `POST /auth/users/` - create a new user
- `POST /auth/token/login/` - log in and obtain an auth token
- `POST /api-token-auth/` - obtain a DRF token for API authentication

### Restaurant

- `GET /restaurant/` - home page
- `GET /restaurant/menu/` - list all menu items
- `POST /restaurant/menu/` - create a new menu item
- `GET /restaurant/menu/<id>/` - retrieve a specific menu item
- `PUT /restaurant/menu/<id>/` - update a menu item
- `DELETE /restaurant/menu/<id>/` - delete a menu item
- `GET /restaurant/booking/tables/` - list bookings
- `POST /restaurant/booking/tables/` - create a booking

> Note: Booking endpoints are protected and require authentication.

## Running Tests

```bash
python manage.py test
```
