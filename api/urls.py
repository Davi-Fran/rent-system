from rest_framework.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import *

urlpatterns = [
    path("users", UsersRouteAPIView.as_view()),
    path("users/<int:pk>", UsersDetailAPIView.as_view()),

    path("propertys", PropertysRouteAPIView.as_view()),
    path("propertys/<int:pk>", PropertysDetailAPIView.as_view()),

    path("agreements", AgreementsRouteAPIView.as_view()),
    path("agreements/<int:pk>", AgreementsDetailAPIView.as_view()),

    path("payments", PaymentsRouteAPIView.as_view()),
    path("payments/<int:pk>", PaymentsDetailAPIView.as_view()),

    path("token", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh", TokenRefreshView.as_view(), name="token_refresh")
]