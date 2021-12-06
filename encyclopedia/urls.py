from django.urls import path

from . import views


appname = "ecyclopedia"
urlpatterns = [
    path("index/", views.index, name="index"),
    path("CSS/", views.css, name="CSS"),
    path("Django/", views.django, name="Django"),
    path("Git/", views.git, name="Git"),
    path("HTML/", views.html, name="HTML"),
    path("Python/", views.python, name="Python"),

]
