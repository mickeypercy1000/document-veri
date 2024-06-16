import os
from rest_framework import serializers

class CommonValidations:
    
    @staticmethod
    def validate_file_extension(value):
        ext = os.path.splitext(value.name)[1]
        valid_extensions = ['.jpg', '.jpeg', '.png']
        if not ext.lower() in valid_extensions:
            raise serializers.ValidationError('Unsupported file extension.')
        return value
        