#!/usr/bin/env python
"""
Generate resume PDFs from Django templates using WeasyPrint.

Usage:
    python generate_resume_pdf.py          # Generate both PDFs
    python generate_resume_pdf.py ru       # Generate Russian PDF only
    python generate_resume_pdf.py en       # Generate English PDF only
"""

import os
import sys
import shutil
import django
from django.conf import settings

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

if not settings.configured:
    settings.configure(
        DEBUG=True,
        SECRET_KEY='pdf-generation-key',
        INSTALLED_APPS=[
            'django.contrib.staticfiles',
            'app',
        ],
        TEMPLATES=[
            {
                'BACKEND': 'django.template.backends.django.DjangoTemplates',
                'DIRS': [],
                'APP_DIRS': True,
                'OPTIONS': {
                    'context_processors': [
                        'django.template.context_processors.debug',
                        'django.template.context_processors.request',
                        'django.template.context_processors.static',
                    ],
                },
            },
        ],
        STATIC_URL=STATIC_ROOT + '/',
        STATIC_ROOT=STATIC_ROOT,
    )

django.setup()

from django.template.loader import render_to_string
from weasyprint import HTML

RESUMES = {
    'ru': {
        'template': 'app/resume-russian.html',
        'output': 'resume_ru.pdf',
    },
    'en': {
        'template': 'app/resume-english.html',
        'output': 'resume_en.pdf',
    },
}


def prepare_static_files():
    if os.path.exists(STATIC_ROOT):
        shutil.rmtree(STATIC_ROOT)
    os.makedirs(os.path.join(STATIC_ROOT, 'app'))

    src_dir = os.path.join(BASE_DIR, 'app', 'static', 'app')
    for filename in os.listdir(src_dir):
        shutil.copy(
            os.path.join(src_dir, filename),
            os.path.join(STATIC_ROOT, 'app', filename),
        )


def generate_pdf(lang):
    config = RESUMES[lang]
    html_string = render_to_string(config['template'])
    html = HTML(string=html_string, base_url=f"file://{BASE_DIR}/")
    html.write_pdf(config['output'])
    print(f"Generated {config['output']}")


def cleanup():
    if os.path.exists(STATIC_ROOT):
        shutil.rmtree(STATIC_ROOT)


def main():
    langs = sys.argv[1:] if len(sys.argv) > 1 else ['ru', 'en']

    for lang in langs:
        if lang not in RESUMES:
            print(f"Unknown language: {lang}. Use 'ru' or 'en'.")
            sys.exit(1)

    prepare_static_files()
    try:
        for lang in langs:
            generate_pdf(lang)
    finally:
        cleanup()


if __name__ == '__main__':
    main()
