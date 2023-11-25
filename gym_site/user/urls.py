from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("userprofile", views.index, name="index"),
    path('update/', views.user_update, name='user_update'),
    path('password/', views.user_password, name='user_password'),
    path('comments/', views.user_comments, name='user_comments'),
    path('deletecomment/<int:id>', views.user_deletecomment, name='user_deletecomment'),
]