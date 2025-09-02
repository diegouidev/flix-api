from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from actors.models import Actor
from core.permissions import GlobalDefaultPermission
from actors.serializers import ActorSerializer

class ActorListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, IsAdminUser, GlobalDefaultPermission)
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

class ActorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer