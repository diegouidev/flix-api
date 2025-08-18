from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Movies
from .serializers import MoviesSerializer

class MoviesListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer

class MoviesRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer