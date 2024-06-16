import re
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import serializers
from authentication.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


# LOGIN VALIDATIONS
def loginValidations(email, password):
    user = authenticate(username=email, password=password)

    if not user:
        message = {"message": "Email or Password incorrect"}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

        # Generate Token
    else:
        refresh = RefreshToken.for_user(user)

        return Response({
            "id": user.id,
            "email": email,
            "access": str(refresh.access_token),
            "refresh": str(refresh),
        }, status=status.HTTP_200_OK)


# USERNAME VALIDATIONS
def BusinessnameValidation(value):
    try:
        business_name = User.objects.get(business_name=value)
        if business_name:
            message = "Business name already used"
            raise serializers.ValidationError(message)
    except User.DoesNotExist:
        pass


# FIRSTNAME VALIDATIONS
def FirstnameValidation(value):
    if re.findall('[()[\]{}|\\`~!@#$%^&*_\+=;:\'",<>./?]', value) or re.findall('\d', value):
        message = {"firstname contain illegal character(s)."}
        raise serializers.ValidationError(message)
    return value


# LASTNAME VALIDATIONS
def LastnameValidation(value):
    if re.findall('[()[\]{}|\\`~!@#$%^&*_\+=;:\'",<>./?]', value) or re.findall('\d', value):
        message = {"lastname contain illegal character(s)."}
        raise serializers.ValidationError(message)


def PhoneValidation(value):
    phone_prefixes = ["024", "054", "055", "025", "059", "020", "050", "026", "056", "027", "057", "023"]
    if value[0:3] not in phone_prefixes or len(value) != 10:
        message = "invalid phone number"
        raise serializers.ValidationError(message)
    else:
        try:
            user = User.objects.get(phone=value)
            if user:
                print(user)
                message = "Phone number already used"
                raise serializers.ValidationError(message)
        except User.DoesNotExist:
            pass

# EMAIL FIELD VALIDATIONS
def EmailValidation(value):
    try:
        email = User.objects.get(email=value)
        if email:
            message = "email already exists"
            raise serializers.ValidationError(message)
    except User.DoesNotExist:
        pass


# THIS CLASS HANDLES PASSWORD UPPERCASE VALIDATIONS
class UppercaseValidator(object):
    def validate(self, password, user=None):
        if not re.findall('[A-Z]', password):
            raise ValidationError(
                _("Your password must contain at least 1 uppercase letter"),
                code='password_no_upper',
            )

    def get_help_text(self):
        return _(
            "Your password must contain at least 1 uppercase letter"
        )


# THIS CLASS HANDLES PASSWORD LOWERCASE VALIDATIONS
class LowercaseValidator(object):
    def validate(self, password, user=None):
        if not re.findall('[a-z]', password):
            raise ValidationError(
                _("Your password must contain at least 1 lowercase letter"),
                code='password_no_lower',
            )

    def get_help_text(self):
        return _(
            "Your password must contain at least 1 lowercase letter"
        )


# THIS CLASS HANDLES PASSWORD NUMBER VALIDATIONS
class NumberValidator(object):
    def validate(self, password, user=None):
        if not re.findall('\d', password):
            raise ValidationError(
                _("Your password must contain at least 1 digit, 0-9."),
                code='password_no_number',
            )

    def get_help_text(self):
        return _(
            "Your password must contain at least 1 digit, 0-9."
        )


# THIS CLASS HANDLES PASSWORD SYMBOL VALIDATIONS
class SymbolValidator(object):
    def validate(self, password, user=None):
        if not re.findall('[()[\]{}|\\`~!@#$%^&*_\-+=;:\'",<>./?]', password):
            raise ValidationError(
                _("Your password must contain at least 1 of the following symbols: " +
                  "()[]{}|\`~!@#$%^&*_-+=;:'\",<>./?"),
                code='password_no_symbol',
            )

    def get_help_text(self):
        return _(
            "Your password must contain at least 1 of the followin symbols: " +
            "()[]{}|\`~!@#$%^&*_-+=;:'\",<>./?"
        )