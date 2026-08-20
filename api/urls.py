from django.urls import path, include

from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views_api_view import (
    UsersRouteAPIView,
    UsersDetailAPIView,
    PropertysRouteAPIView,
    PropertysDetailAPIView,
    AgreementsRouteAPIView,
    AgreementsDetailAPIView,
    PaymentsRouteAPIView,
    PaymentsDetailAPIView
)

from .views_generics import (
    UserListCreateGeneric,
    UserRetrieveUpdateDestroyGeneric,
    PropertyListCreateGeneric,
    PropertyRetrieveUpdateDestroyGeneric,
    AgreementListCreateGeneric,
    AgreementRetrieveUpdateDestroyGeneric,
    PaymentListCreateGeneric,
    PaymentRetrieveUpdateDestroyGeneric
)

from .views_viewset import (
    UserViewSet,
    PropertyViewSet,
    AgreementViewSet,
    PaymentViewSet
)

router = DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'propertys', PropertyViewSet)
router.register(r'agreements', AgreementViewSet)
router.register(r'payments', PaymentViewSet)

urlpatterns = [
    # -----------------------
    # APIView
    # -----------------------
    path("apiview/users", UsersRouteAPIView.as_view()),
    path("apiview/users/<int:pk>", UsersDetailAPIView.as_view()),
    
    path("apiview/propertys", PropertysRouteAPIView.as_view()),
    path("apiview/propertys/<int:pk>", PropertysDetailAPIView.as_view()),
    
    path("apiview/agreements", AgreementsRouteAPIView.as_view()),
    path("apiview/agreements/<int:pk>", AgreementsDetailAPIView.as_view()),
    
    path("apiview/payments", PaymentsRouteAPIView.as_view()),
    path("apiview/payments/<int:pk>", PaymentsDetailAPIView.as_view()),
    
    path("apiview/token", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("apiview/token/refresh", TokenRefreshView.as_view(), name="token_refresh"),


    # -----------------------
    # Generics
    # -----------------------
    path('generics/users', UserListCreateGeneric.as_view()),
    path('generics/users/<int:pk>', UserRetrieveUpdateDestroyGeneric.as_view()),

    path("generics/propertys", PropertyListCreateGeneric.as_view()),
    path("generics/propertys/<int:pk>", PropertyRetrieveUpdateDestroyGeneric.as_view()),
    
    path("generics/agreements", AgreementListCreateGeneric.as_view()),
    path("generics/agreements/<int:pk>", AgreementRetrieveUpdateDestroyGeneric.as_view()),
    
    path("generics/payments", PaymentListCreateGeneric.as_view()),
    path("generics/payments/<int:pk>", PaymentRetrieveUpdateDestroyGeneric.as_view()),
    
    path("generics/token", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("generics/token/refresh", TokenRefreshView.as_view(), name="token_refresh"),


    # -----------------------
    # ModelViewSet
    # -----------------------
    path('viewset/', include(router.urls))
]