from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('product/', include('product.urls')),
    path("about", views.about, name="about"),
    path("feature", views.feature, name="feature"),
    path("classes", views.classes, name="classes"),
    path("contact", views.contact, name="contact"),
    path("blog", views.blog, name="blog"),
    path("single", views.single, name="single"),
]
