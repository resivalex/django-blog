from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML

RESUME_TEMPLATE = "app/resume.html"
RESUME_PDF_FILENAME = "Ivan_Reshetnikov_Senior_MLE.pdf"


def home(request):
    return render(request, RESUME_TEMPLATE, {})


def resume_pdf(request):
    html_string = render_to_string(RESUME_TEMPLATE, request=request)
    base_url = request.build_absolute_uri('/')
    pdf = HTML(string=html_string, base_url=base_url).write_pdf()
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{RESUME_PDF_FILENAME}"'
    return response


def styles(_request):
    css = open("app/static/app/styles.css").read()
    return HttpResponse(css, content_type="text/css")


def favicon(_request):
    png = open("app/static/app/favicon.png", "rb").read()
    return HttpResponse(png, content_type="image/png")


def yandex_verification(_request):
    html = open("app/static/yandex_b7c26d3a89609f98.html", "rb").read()
    return HttpResponse(html, content_type="text/html")
