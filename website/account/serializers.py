from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import User, Profile


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)  # Password confirmation field

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name", "password", "password2"]

    def validate(self, data):
        # Validate password confirmation
        password = data.get('password')
        password2 = data.get('password2')
        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        # Validate password requirements using Django's default validators
        validate_password(password)
        return data

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        password = validated_data['password']
        user.set_password(password)
        user.save()

        profile = Profile.objects.create(user=user)

        return user
   
    # def create(self, validated_data):
    #     user = User.objects.create(email=validated_data['email'],
    #                                    first_name=validated_data['first_name'],
    #                                    last_name=validated_data['last_name']
    #                                      )
    #     user.set_password(validated_data['password'])
    #     user.save()
    #     return user