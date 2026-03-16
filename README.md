# Sputnik - Django Static Page Generator

A static page generator built with Django and [django-distill](https://github.com/meeb/django-distill).

## Setup

```bash
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
python manage.py distill-local output --force
```

## Deployment

The generated static files in `output/` can be deployed to any static hosting provider.
