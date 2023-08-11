from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegistrationView, MyTokenObtainPairView, ChangePasswordView, UserView

app_name = 'account'

urlpatterns = [
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegistrationView.as_view(), name="sign_up"),
    path('change_password/<int:pk>/', ChangePasswordView.as_view(), name="change_password"),
    path('user/', UserView.as_view(), name="user"),
    #path('update_profile/<int:pk>/', UpdateProfileView.as_view(), name="update_profile"),
]

# 'user/' allows: GET, PUT and accepts JSON with email, first_name, last_name, and profile; where
# profile is nested object with profile model fields, pk is not needed because view and serializer
# check for current authenticated user and only allows updates for match user/profile objects