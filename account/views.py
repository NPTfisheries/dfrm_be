from rest_framework import status, generics, mixins, viewsets
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import RegistrationSerializer, MyTokenObtainPairSerializer, ChangePasswordSerializer, UserSerializer, ProfileSerializer, UpdateProfilePhotoSerializer, ObjectPermissionsSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from .models import User, Profile

from django.core.files.storage import default_storage


# view for registering users
class RegistrationView(APIView):
    permission_classes = (IsAdminUser,)

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class ChangePasswordView(generics.UpdateAPIView):

    #queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer

    def get_object(self):
        return self.request.user  

class UserView(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user  

class UserViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        return super().get_permissions()

    def get_queryset(self):
        queryset = super().get_queryset()
        
        # Filter out the specific user by their username
        # AnonymousUser.id:1 // we don't want this in user lists
        queryset = queryset.exclude(id=1)
        # filter out inactive users
        queryset = queryset.filter(is_active=True)
        
        return queryset

class UpdateProfileView(generics.UpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.profile

    def perform_update(self, serializer):
        if self.request.user != self.get_object().user:
            raise serializers.ValidationError("You can only update your own profile.")
        serializer.save()

class UpdateProfilePhotoView(generics.UpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = UpdateProfilePhotoSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.profile

    def perform_update(self, serializer):
        if self.request.user != self.get_object().user:
            raise serializers.ValidationError("You can only update your own profile photo.")

        existing_photo = self.get_object().photo
        if 'profile_default.JPG' not in existing_photo.name:
            # Delete the existing photo if not the default. Prevent clutter.
            default_storage.delete(existing_photo.name)

        serializer.save()

class ObjectPermissionsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        serializer = ObjectPermissionsSerializer()
        permissions = serializer.get_permissions(user)
        
        if permissions:
            return Response(permissions, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)