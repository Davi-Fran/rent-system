from rest_framework.urls import path

from .views import *

urlpatterns = [
    path("users", UsersRouteAPIView.as_view()),
    path("users/<int:pk>", UsersDetailAPIView.as_view()),
    path("propertys", PropertysRouteAPIView.as_view()),
    path("propertys/<int:pk>", PropertysDetailAPIView.as_view()),
    path("agreements", AgreementsRouteAPIView.as_view()),
    path("agreements/<int:pk>", AgreementsDetailAPIView.as_view())
]