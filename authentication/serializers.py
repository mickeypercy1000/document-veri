import re
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from authentication import validators
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.exceptions import ValidationError

from authentication.models import User


class CreateUserSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    email = serializers.EmailField(
        max_length=100, required=True, validators=[validators.EmailValidation],
        error_messages={
            'invalid': 'Provide a valid email address',
            'blank': 'Provide a valid email address',
            'required': 'Provide a valid email address',
            })
    business_name = serializers.CharField(
        max_length=100, required=True, validators=[validators.BusinessnameValidation],
        error_messages={
            'blank': 'Please provide a business name',
            'required': 'Please provide a business name',
            })
    phone = serializers.CharField(
        max_length=10, required=True, validators=[validators.PhoneValidation],
        error_messages={
            'blank': 'Please provide a phone number',
            'required': 'Please provide a phone number',
            })
    firstname = serializers.CharField(max_length=100, required=True, allow_blank=False, validators=[validators.FirstnameValidation])
    lastname = serializers.CharField(max_length=100, required=True, allow_blank=False, validators=[validators.LastnameValidation])
    country = serializers.CharField(max_length=100, required=True, allow_blank=False, validators=[validators.LastnameValidation])
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ["id", "email", "phone", "business_name", "firstname", "lastname", "country", "password"]

    def create(self, validated_data):
        email = validated_data.get('email').lower()  # Convert email to lowercase
        phone = validated_data.get('phone').lower()  # Convert email to lowercase
        firstname = validated_data.get('firstname', '').capitalize()  # Convert first letter to capital
        business_name = validated_data.get('business_name', '').capitalize()  # Convert first letter to capital
        lastname = validated_data.get('lastname', '').capitalize()  # Convert first letter to capital
        password = validated_data.get('password')

        user = User.objects.create(email=email, firstname=firstname, lastname=lastname, phone=phone, business_name=business_name)
        user.set_password(password)
        user.save()
        return user


class VerifyOTPSerializer(serializers.ModelSerializer):
    user_id = serializers.CharField(
        max_length=50, required=True,
        error_messages={
            'blank': 'Provide User ID',
            'required': 'User ID is required',
            })
    otp = serializers.CharField(
        max_length=8, required=True,
        error_messages={
            'blank': 'Provide OTP',
            'required': 'OTP is required',
            })

    class Meta:
        model = User
        fields = ["user_id", "otp"]


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(
        error_messages={
            'blank': 'Email is required',
            'required': 'Email is required',
            })
    password = serializers.CharField(
        error_messages={
            'blank': 'Password is required',
            'required': 'Password is required',
            })

    class Meta:
        model = User
        fields = ["email", "password"]

    def validate(self, data):

        email = data.get('email')
        password = data.get('password')
        user = authenticate(email=email, password=password)
        if not user:
            message = {"login_error": "Email or password is incorrect"}
            raise serializers.ValidationError(message)
        data['user'] = user
        return data




class LogoutUserSerializer(serializers.ModelSerializer):

    refresh = serializers.CharField()

    class Meta:
        model = User
        fields = ['refresh', ]
        
    def validate(self, attrs):
        try:
            token = RefreshToken(attrs['refresh'])
            token.blacklist()
        except TokenError:
            raise ValidationError({'message': 'Invalid refresh token'})
        return {}


class UpdateRetrieveUserSerializer(serializers.ModelSerializer):
    """
    Update user profile,
    Retrieve user detail,
    """
    id = serializers.CharField(read_only=True)
    firstname = serializers.CharField(max_length=100, required=False, allow_blank=True, validators=[validators.FirstnameValidation])
    lastname = serializers.CharField(max_length=100, required=False, allow_blank=True, validators=[validators.LastnameValidation])

    class Meta:
        model = User
        fields = ["id", "firstname", "lastname", "email"]

    def update(self, instance, validated_data):
        instance.firstname = validated_data.get("firstname", instance.firstname)
        instance.lastname = validated_data.get("lastname", instance.lastname)

        instance.save()
        return instance

    def get(self, validated_data):
        print("data", validated_data)
