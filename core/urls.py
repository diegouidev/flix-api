from django.contrib import admin
from django.urls import path
from genres.views import GenreRetrieveUpdateDestroyView, GenreListCreateView
from actors.views import ActorListCreateView, ActorRetrieveUpdateDestroyView
from movies.views import MoviesListCreateView, MoviesRetrieveUpdateDestroyView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('genres', GenreListCreateView.as_view(), name='genre-create-list'),
    path('genres/<int:pk>', GenreRetrieveUpdateDestroyView.as_view(), name='genre-detail'),

    path('actors/', ActorListCreateView.as_view(), name='actor-create-list'),
    path('actors/<int:pk>/', ActorRetrieveUpdateDestroyView.as_view(), name='actor-detail'),


    path('movies/', MoviesListCreateView.as_view(), name='movies-create-list'),
    path('movies/<int:pk>/', MoviesRetrieveUpdateDestroyView.as_view(), name='movies-detail'),
]
