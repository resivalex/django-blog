#!/usr/bin/env python
"""
Generate the resume PDF from the Django template using WeasyPrint.

Usage:
    python generate_resume_pdf.py
"""

import os
import django
from django.conf import settings

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, 'app', 'static')

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
        STATIC_URL=STATIC_DIR + '/',
    )

django.setup()

from app.resume_pdf import RESUME_PDF_FILENAME, write_resume_pdf


def generate_pdf():
    write_resume_pdf(base_url=f"file://{BASE_DIR}/", target=RESUME_PDF_FILENAME)
    print(f"Generated {RESUME_PDF_FILENAME}")


if __name__ == '__main__':
    generate_pdf()
