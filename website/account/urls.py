from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegistrationView, MyTokenObtainPairView, ChangePasswordView, UpdateUserView

app_name = 'account'

urlpatterns = [
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegistrationView.as_view(), name="sign_up"),
    path('change_password/<int:pk>/', ChangePasswordView.as_view(), name="change_password"),
    path('update_user/<int:pk>/', UpdateUserView.as_view(), name="update_user"),
    #path('update_profile/<int:pk>/', UpdateProfileView.as_view(), name="update_profile"),
]

# 'update_user/<int:pk>/' accepts JSON with email, first_name, last_name, and profile; where
# profile is nested object with profile model fields