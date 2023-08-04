from django.urls import path
from .views import RegistrationView, ChangePasswordView, UpdateUserView, UpdateProfileView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = 'account'

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegistrationView.as_view(), name="sign_up"),
    path('change_password/<int:pk>/', ChangePasswordView.as_view(), name="change_password"),
    path('update_user/<int:pk>/', UpdateUserView.as_view(), name="update_user"),
    path('update_profile/<int:pk>/', UpdateProfileView.as_view(), name="update_profile"),
]