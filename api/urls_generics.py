from rest_framework.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views_generics import *

urlpatterns = [
    path('users', UserListCreateGeneric.as_view()),
    path('users/<int:pk>', UserRetrieveUpdateDestroyGeneric.as_view()),

    path("propertys", PropertyListCreateGeneric.as_view()),
    path("propertys/<int:pk>", PropertyRetrieveUpdateDestroyGeneric.as_view()),
    
    path("agreements", AgreementListCreateGeneric.as_view()),
    path("agreements/<int:pk>", AgreementRetrieveUpdateDestroyGeneric.as_view()),
    
    path("payments", PaymentListCreateGeneric.as_view()),
    path("payments/<int:pk>", PaymentRetrieveUpdateDestroyGeneric.as_view()),
    
    path("token", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh", TokenRefreshView.as_view(), name="token_refresh"),
]