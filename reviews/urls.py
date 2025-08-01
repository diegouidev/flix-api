from django.urls import path
from .views import ReviewCreateList, ReviewRetrieveUpdateDestroy

urlpatterns = [
    path('reviews/', ReviewCreateList.as_view(), name='review-create-list'),
    path('reviews/<int:pk>/', ReviewRetrieveUpdateDestroy.as_view(), name='review-detail'),
]
