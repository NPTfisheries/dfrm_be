from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.password_validation import validate_password
from .models import User, Profile


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)  # Password confirmation field

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name", "role", "password", "password2"]

    def validate(self, data):
        # Validate password confirmation
        password = data.get('password')
        password2 = data.get('password2')
        if password != password2:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        # Validate password requirements using Django's default validators
        validate_password(password)
        return data

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            role = validated_data['role']
        )
        password = validated_data['password']
        user.set_password(password)
        user.save()

        # Signal to assign group based on role
        #assign_group(User, user, created=True)

        return user
    
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)

        # Add extra responses here
        data['first_name'] = self.user.first_name
        data['last_name'] = self.user.last_name
        data['email'] = self.user.email
        data['role'] = self.user.role
        data['permissions'] = self.user.user_permissions.values_list('name', flat=True)
        data['groups'] = self.user.groups.values_list('name', flat=True)
        return data

class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('old_password', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError({"old_password": "Old password is not correct"})
        return value

    def update(self, instance, validated_data):

        instance.set_password(validated_data['password'])
        instance.save()

        return instance
    
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('title', 'work_phone', 'mobile_phone', 'city', 'state', 'bio', 'photo')

class UserSerializer(serializers.ModelSerializer):
    #email = serializers.EmailField(required=True)
    profile = ProfileSerializer(required=False)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'profile')
        extra_kwargs = {
            'email': {'required': False},
            'first_name': {'required': False},
            'last_name': {'required': False},
            'profile': {'required': False},
        }

    def validate(self, attrs):
        user = self.context['request'].user
        instance = self.instance
        if instance != user:
            raise serializers.ValidationError("You can only update your own user information.")
        return attrs
    
    # def validate_email(self, value):
    #     user = self.context['request'].user
    #     if User.objects.exclude(pk=user.pk).filter(email=value).exists():
    #         raise serializers.ValidationError({"email": "This email is already in use."})
    #     return value

    def update(self, instance, validated_data):

        profile_data = validated_data.pop('profile',None)

        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()

        if profile_data is not None:
            profile_instance = instance.profile
            for key, value in profile_data.items():
                print(key, value)
                setattr(profile_instance, key, value)
            profile_instance.save()

        return instance