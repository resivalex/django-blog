from django.shortcuts import render
from django.http import HttpResponse
from .resume_english import html as english_html
from .resume_russian import html as russian_html


def home(request):
    return render(request, 'app/resume-english.html', {'html': english_html()})


def english_resume(request):
    return render(request, 'app/resume-russian.html', {'html': russian_html()})


def styles(_request):
    css = open('app/static/app/styles.css').read()
    return HttpResponse(css, content_type='text/css')


def favicon(_request):
    png = open('app/static/app/favicon.png', 'rb').read()
    return HttpResponse(png, content_type='image/png')


def yandex_verification(_request):
    html = open('app/static/yandex_b7c26d3a89609f98.html', 'rb').read()
    return HttpResponse(html, content_type='text/html')
