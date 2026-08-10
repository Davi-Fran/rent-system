from rest_framework.urls import path

from .views import *

urlpatterns = [
    path("users", UsersRouteAPIView.as_view()),
    path("users/<int:pk>", UsersDetailAPIView.as_view())
]