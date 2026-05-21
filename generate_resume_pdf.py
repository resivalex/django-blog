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

from app.resume_pdf import RESUME_PDF_FILENAME, write_resume_pdf


def prepare_static_files():
    if os.path.exists(STATIC_ROOT):
        shutil.rmtree(STATIC_ROOT)
    os.makedirs(os.path.join(STATIC_ROOT, 'app'))

    src_dir = os.path.join(BASE_DIR, 'app', 'static', 'app')
    for filename in os.listdir(src_dir):
        src_path = os.path.join(src_dir, filename)
        dst_path = os.path.join(STATIC_ROOT, 'app', filename)
        if os.path.isdir(src_path):
            shutil.copytree(src_path, dst_path)
        else:
            shutil.copy(src_path, dst_path)


def generate_pdf():
    write_resume_pdf(base_url=f"file://{BASE_DIR}/", target=RESUME_PDF_FILENAME)
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
