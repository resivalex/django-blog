from django.contrib import admin
from django.urls import path
from app.views import home, posts, post, post_image, resume_pdf, styles, favicon, font, yandex_verification

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("Ivan_Reshetnikov_ML_AI_Engineer.pdf", resume_pdf, name="resume-pdf"),
    path("Ivan_Reshetnikov_Senior_ML_AI_Engineer.pdf", resume_pdf),  # old links
    path("posts/", posts, name="posts"),
    path("posts/<slug:slug>/", post, name="post"),
    path("static/app/posts/<str:filename>", post_image, name="post-image"),
    path("static/app/styles.css", styles, name="styles"),
    path("static/app/favicon.png", favicon, name="favicon"),
    path("static/app/fonts/<str:filename>", font, name="font"),
    path(
        "yandex_b7c26d3a89609f98.html", yandex_verification, name="yandex_verification"
    ),
]
