from django.urls import path
from . import views

app_name = "posts"


urlpatterns = [
    # Главная страница
    path("", views.index, name="index"),
    # Отдельная страница сообщества
    path("group/<slug:slug>/", views.posts, name="group_list"),
]
