from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework import generics
from .models import CustomUser


class CustomUserSerializers(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('email','first_name','password','last_name','is_renter')

    def validate_password(self, value):
        validate_password(value)
        return value

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)

class ShortCustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email','first_name','phone')


class CustomUserUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('first_name','last_name',"phone")
