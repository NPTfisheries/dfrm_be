from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegistrationView, MyTokenObtainPairView, ChangePasswordView, UserView, UserViewSet

app_name = 'account'

urlpatterns = [
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegistrationView.as_view(), name="sign_up"),
    path('change_password/<int:pk>/', ChangePasswordView.as_view(), name="change_password"),
    path('user/', UserView.as_view(), name="user"),
    path('users/', UserViewSet.as_view({'get':'list'}), name="user_list"),
    path('users/<int:pk>/', UserViewSet.as_view({'get':'retrieve'}), name="user_detail"),
    #path('update_profile/<int:pk>/', UpdateProfileView.as_view(), name="update_profile"),
]

# 'user/' requires authentication: allows: GET, PUT and accepts JSON with email, first_name, last_name, and profile; where
# profile is nested object with profile model fields, pk is not needed because view and serializer
# check for current authenticated user and only allows updates for match user/profile objects

# 'users/' open access: allows GET and returns the full list of users with profiles, if pk is added
# the request returns a single user and profile info