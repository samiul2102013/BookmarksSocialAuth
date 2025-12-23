# Django Bookmarks

A social bookmarking application built with Django 5, following the "Django 5 by Example" book.

## Features

- **User Authentication**
  - User registration and login
  - Password change and reset via email
  - Custom email authentication backend
  - Profile management with photo upload

- **Social Authentication**
  - Login with Google
  - Login with GitHub
  - Connect/disconnect multiple social accounts
  - Automatic profile creation for social users
  - Profile picture download from social providers

## Tech Stack

- Python 3.12
- Django 5.2
- social-auth-app-django (Python Social Auth)
- Pillow (Image processing)
- SQLite (Development database)

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/django-bookmarks.git
cd django-bookmarks
```

### 2. Create and activate virtual environment

```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### 3. Install dependencies

```bash
pip install django social-auth-app-django Pillow python-dotenv
```

### 4. Set up environment variables

Create a `.env` file in the project root with:

```
SECRET_KEY=your-secret-key
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY=your-google-client-id
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET=your-google-client-secret
SOCIAL_AUTH_GITHUB_KEY=your-github-client-id
SOCIAL_AUTH_GITHUB_SECRET=your-github-client-secret
```

### 5. Run migrations

```bash
python manage.py migrate
```

### 6. Create a superuser (optional)

```bash
python manage.py createsuperuser
```

### 7. Run the development server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/account/` to access the application.

## Project Structure

```
bookmarks/
├── account/                 # User account app
│   ├── authentication.py    # Custom auth backends
│   ├── forms.py            # User forms
│   ├── models.py           # Profile model
│   ├── pipeline.py         # Social auth pipeline
│   ├── views.py            # Account views
│   └── templates/          # Account templates
├── bookmarks/              # Project settings
│   ├── settings.py         # Django settings
│   └── urls.py             # Main URL config
├── media/                  # User uploaded files
├── .env                    # Environment variables (not in repo)
├── .gitignore             # Git ignore file
├── manage.py              # Django management script
└── README.md              # This file
```

## Setting Up Social Authentication

### Google OAuth2

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project
3. Enable OAuth consent screen
4. Create OAuth 2.0 credentials
5. Add redirect URI: `http://127.0.0.1:8000/social-auth/complete/google-oauth2/`
6. Copy Client ID and Secret to `.env`

### GitHub OAuth

1. Go to [GitHub Developer Settings](https://github.com/settings/developers)
2. Create a new OAuth App
3. Set callback URL: `http://127.0.0.1:8000/social-auth/complete/github/`
4. Copy Client ID and Secret to `.env`

## URLs

| URL | Description |
|-----|-------------|
| `/account/` | Dashboard |
| `/account/login/` | Login page |
| `/account/logout/` | Logout |
| `/account/register/` | User registration |
| `/account/edit/` | Edit profile |
| `/account/password-change/` | Change password |
| `/account/password-reset/` | Reset password |
| `/account/social-accounts/` | Manage social accounts |

## Learning Progress

This project is part of my Django learning journey using "Django 5 by Example" book.

### Completed Chapters:
- [x] Chapter 1: Building a Blog Application
- [x] Chapter 4: Building a Social Website - Authentication
- [x] Chapter 5: Social Authentication

## License

This project is for educational purposes.

## Author

Samiul - Learning Django 🚀
