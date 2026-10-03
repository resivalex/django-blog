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
