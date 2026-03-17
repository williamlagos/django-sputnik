# Sputnik - Django Static Page Generator

A static page generator built with Django and [django-distill](https://github.com/meeb/django-distill).

## Setup

Clone the repository and install dependencies:

```bash
git clone https://github.com/williamlagos/django-sputnik.git
cd django-sputnik
pip install -r requirements.txt
```

## Development

Run the development server:

```bash
python manage.py runserver
```

## Generate static site

Generate the static site to the `output/` directory:

```bash
python manage.py collectstatic --noinput
python manage.py distill-local output --force
```

## Deployment

The generated static files in `output/` can be deployed to any static hosting provider (GitHub Pages, Netlify, Cloudflare Pages, etc.).
