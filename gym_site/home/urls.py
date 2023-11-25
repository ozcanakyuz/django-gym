from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("feature", views.feature, name="feature"),
    path("classes", views.classes, name="classes"),
    path("contact", views.contact, name="contact"),
    path("blog", views.blog, name="blog"),
]
