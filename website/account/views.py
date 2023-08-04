from rest_framework import status, generics
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import UpdateModelMixin
from rest_framework.views import APIView
from .serializers import RegistrationSerializer, ChangePasswordSerializer, UpdateUserSerializer, UpdateProfileSerializer
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
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ChangePasswordView(generics.UpdateAPIView):

    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer


class UpdateUserView(generics.UpdateAPIView):

    queryset = User.objects.all()
    permission_classes = (IsAdminUser,)
    serializer_class = UpdateUserSerializer


class UpdateProfileView(generics.UpdateAPIView):

    queryset = Profile.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UpdateProfileSerializer