from rest_framework import generics
from .models import Movies
from .serializers import MoviesSerializer

class MoviesListCreateView(generics.ListCreateAPIView):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer

class MoviesRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer