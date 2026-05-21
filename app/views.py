from django.shortcuts import render
from django.http import HttpResponse

from app.resume_pdf import RESUME_PDF_FILENAME, RESUME_TEMPLATE, write_resume_pdf


def home(request):
    return render(request, RESUME_TEMPLATE, {})


def resume_pdf(request):
    base_url = request.build_absolute_uri('/')
    pdf = write_resume_pdf(base_url=base_url, request=request)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{RESUME_PDF_FILENAME}"'
    return response


def styles(_request):
    css = open("app/static/app/styles.css").read()
    return HttpResponse(css, content_type="text/css")


def favicon(_request):
    png = open("app/static/app/favicon.png", "rb").read()
    return HttpResponse(png, content_type="image/png")


FONT_CONTENT_TYPES = {
    "ttf": "font/ttf",
    "woff": "font/woff",
    "woff2": "font/woff2",
    "otf": "font/otf",
}


def font(_request, filename):
    ext = filename.rsplit(".", 1)[-1].lower()
    content_type = FONT_CONTENT_TYPES.get(ext, "application/octet-stream")
    data = open(f"app/static/app/fonts/{filename}", "rb").read()
    return HttpResponse(data, content_type=content_type)


def yandex_verification(_request):
    html = open("app/static/yandex_b7c26d3a89609f98.html", "rb").read()
    return HttpResponse(html, content_type="text/html")
