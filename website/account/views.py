from rest_framework import status, generics
from rest_framework.generics import GenericAPIView, RetrieveUpdateAPIView
from rest_framework.mixins import UpdateModelMixin
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import RegistrationSerializer, MyTokenObtainPairSerializer, ChangePasswordSerializer, UpdateUserSerializer, ProfileSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import User, Profile

# view for registering users
class RegistrationView(APIView):
    #permission_classes = (AllowAny,)
    permission_classes = (IsAdminUser,)

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class ChangePasswordView(generics.UpdateAPIView):

    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer


class UpdateUserView(generics.RetrieveUpdateAPIView):

    queryset = User.objects.all()
    permission_classes = (IsAdminUser,)
    serializer_class = UpdateUserSerializer


class UpdateProfileView(generics.UpdateAPIView):
    queryset = Profile.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ProfileSerializer

# class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
#     queryset = User.objects.all()
#     permission_classes = (IsAuthenticated,)
#     serializer_class = UserSerializer

# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     permission_classes = (IsAuthenticated,)
#     serializer_class = UserSerializer

# class UserList(generics.ListCreateAPIView):
#     permission_classes = (IsAuthenticated,)
#     serializer_class = UserSerializer

#     def post(self, request, format=None):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)