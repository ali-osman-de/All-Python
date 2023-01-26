from django.urls import path
from . import views

# https://127.0.0:8000/
# https://127.0.0:8000/movies
# https://127.0.0:8000/movies/3
# https://127.0.0:8000/movies/walking-dead

urlpatterns = [
    path("", views.home, name="home"),
    path("home", views.home),
    path("movies", views.movies,name="movies"),
    path("movies/<int:id>", views.moviedetails, name="details")
]