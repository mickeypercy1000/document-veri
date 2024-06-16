import re
from rest_framework import serializers


def phone_validator(value):
    phone_prefixes = ["024", "054", "059", "055", "025", "026", "027", "056", "057", "020", "050"]
    if not re.findall('^\d{10}$', value):
        message = "Invalid Phone number."
        raise serializers.ValidationError(message)
    elif value[:3] not in phone_prefixes:
        message = "Invalid phone number"
        raise serializers.ValidationError(message)
    return value


def network_validator(value):
    if re.findall('[()[\]{}|\\`~!@#$%^&*\+=;:\'",<>./?]', value) or re.findall('\d', value):
        message = "Network contain illegal character(s)."
        raise serializers.ValidationError(message)
    return value


def amount_validator(value):
    if not re.findall('\d', value):
        message = "Network contain illegal character(s)."
        raise serializers.ValidationError(message)
    return value


def number_validator(value):
    if not re.findall('\d', value):
        message = "this field must contain only numbers "
        raise serializers.ValidationError(message)