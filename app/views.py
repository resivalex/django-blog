from django.shortcuts import render
from django.http import HttpResponse
from .resume_english import html as english_html
from .resume_russian import html as russian_html


def home(request):
    return render(request, 'app/resume-russian.html', {'html': russian_html()})


def english_resume(request):
    return render(request, 'app/resume-english.html', {'html': english_html()})


def styles(_request):
    css = open('app/static/app/styles.css').read()
    return HttpResponse(css, content_type="text/css")
