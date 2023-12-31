from django.urls import include, path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("feature", views.feature, name="feature"),
    path("classes", views.classes, name="classes"),
    path("contact", views.contact, name="contact"),
    path("blog", views.blog, name="blog"),
    path("single", views.single, name="single"),


    path('login', views.login_view, name='login_view'),
    path('logout',views.logout_view, name= 'logout_view'),
    path('signup', views.signup_view, name='signup_view'),

    path('addcomment', views.addcomment, name="addcomment"),
    path('replycomment/<int:comment_id>', views.replyComment, name="reply_comment"),

]
