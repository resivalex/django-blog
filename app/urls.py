from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path
from django.views.generic import RedirectView
from django.views.static import serve

from app.views import home, posts, post, resume_pdf

STATIC_DIR = settings.BASE_DIR / "app" / "static"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("posts/", posts, name="posts"),
    path("posts/<slug:slug>/", post, name="post"),
    path("Ivan_Reshetnikov_ML_AI_Engineer.pdf", resume_pdf, name="resume-pdf"),
    path(
        "Ivan_Reshetnikov_Senior_ML_AI_Engineer.pdf",
        RedirectView.as_view(url="/Ivan_Reshetnikov_ML_AI_Engineer.pdf", permanent=True),
    ),
    # ponytail: Django serves the few static files itself; move to WhiteNoise or the proxy if traffic grows.
    re_path(r"^static/(?P<path>.*)$", serve, {"document_root": STATIC_DIR}),
    path(
        "yandex_b7c26d3a89609f98.html",
        serve,
        {"document_root": STATIC_DIR, "path": "yandex_b7c26d3a89609f98.html"},
    ),
]
