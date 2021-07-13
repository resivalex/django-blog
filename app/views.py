from django.shortcuts import render
from .resume_english import html as english_html
from .resume_russian import html as russian_html


def home(request):
    return render(request, 'app/resume-russian.html', {'html': russian_html()})


def english_resume(request):
    return render(request, 'app/resume-english.html', {'html': english_html()})
