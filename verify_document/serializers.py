# from rest_framework import serializers

# from common.models import Country, Document, DocumentType
# from verify_document.services import CommonValidations

# class VerifyGhanaCardSerializer(serializers.ModelSerializer):
#     id = serializers.ReadOnlyField()
#     country = serializers.UUIDField(required=True) 
#     document_type = serializers.UUIDField(required=True)
#     ghana_card_front = serializers.FileField(required=True, validators = [CommonValidations.validate_file_extension])
#     ghana_card_back = serializers.FileField(required=True, validators = [CommonValidations.validate_file_extension])
#     passport_pic = serializers.FileField(required=True, validators = [CommonValidations.validate_file_extension])

#     def validate(self, data):
#         try:
#             country = Country.objects.get(id=data.get("country"))
#         except Country.DoesNotExist:
#             raise serializers.ValidationError("Unsupported Country")

#         try:
#             document_type = DocumentType.objects.get(id=data.get("document_type"))
#         except DocumentType.DoesNotExist:
#             raise serializers.ValidationError("Invalid ID Type")

#         data['country'] = country
#         data['document_type'] = document_type
#         return data

#     def create(self, validated_data):
#         return Document.objects.create(**validated_data)
    
#     class Meta:
#         model = Document
#         fields = ["id", "passport_pic", "ghana_card_front", "ghana_card_back", "document_type", "country"]
