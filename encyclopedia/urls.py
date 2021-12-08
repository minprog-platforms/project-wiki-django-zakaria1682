from django.urls import path

from . import views



appname = "ecyclopedia"
urlpatterns = [

    path("wiki/", views.index, name="wiki"),
    path("wiki/<title>/", views.entry, name="entry"),
    path("search", views.search, name="search"), 
    path("create/", views.create, name="create"),
    
]
 