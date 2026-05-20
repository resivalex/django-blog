#!/usr/bin/env python
"""
Generate the resume PDF from the Django template using WeasyPrint.

Usage:
    python generate_resume_pdf.py
"""

import os
import shutil
import django
from django.conf import settings

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
RESUME_TEMPLATE = 'app/resume.html'
RESUME_PDF_FILENAME = 'Ivan_Reshetnikov_Senior_MLE.pdf'

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


def generate_pdf():
    html_string = render_to_string(RESUME_TEMPLATE)
    html = HTML(string=html_string, base_url=f"file://{BASE_DIR}/")
    html.write_pdf(RESUME_PDF_FILENAME)
    print(f"Generated {RESUME_PDF_FILENAME}")


def cleanup():
    if os.path.exists(STATIC_ROOT):
        shutil.rmtree(STATIC_ROOT)


def main():
    prepare_static_files()
    try:
        generate_pdf()
    finally:
        cleanup()


if __name__ == '__main__':
    main()
