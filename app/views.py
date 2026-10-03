from django.shortcuts import render
from django.http import Http404, HttpResponse

from app.posts import POSTS, POSTS_BY_SLUG

from app.resume_pdf import RESUME_PDF_FILENAME, RESUME_TEMPLATE, write_resume_pdf


def home(request):
    return render(request, RESUME_TEMPLATE, {})


def posts(request):
    return render(request, "app/posts.html", {"posts": POSTS})


def post(request, slug):
    if slug not in POSTS_BY_SLUG:
        raise Http404
    return render(request, "app/post.html", {"post": POSTS_BY_SLUG[slug]})


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


IMAGE_CONTENT_TYPES = {
    "png": "image/png",
    "gif": "image/gif",
}


def post_image(_request, filename):
    ext = filename.rsplit(".", 1)[-1].lower()
    if ext not in IMAGE_CONTENT_TYPES:
        raise Http404
    try:
        data = open(f"app/static/app/posts/{filename}", "rb").read()
    except FileNotFoundError:
        raise Http404
    return HttpResponse(data, content_type=IMAGE_CONTENT_TYPES[ext])


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
