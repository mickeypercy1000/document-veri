from rest_framework import serializers
from merchant.models import MerchantAccount


class ComplianceSerializer(serializers.ModelSerializer):
    
    gps_address = serializers.CharField(max_length=255, required=False)
    physical_address = serializers.CharField(max_length=255, required=False)
    business_email = serializers.EmailField(required=False)
    business_phone = serializers.CharField(max_length=10, required=False)
    business_tax_ID = serializers.CharField(max_length=255, required=False)
    postal_address = serializers.CharField(max_length=255, required=False)
    id_first_director = serializers.CharField(max_length=255, required=False)
    id_second_director = serializers.CharField(max_length=255, required=False)
    expected_monthly_turnover = serializers.CharField(max_length=255, required=False)
    business_description = serializers.CharField(max_length=255, required=False)
    bank_account_number = serializers.CharField(max_length=255, required=False)
    bank_branch = serializers.CharField(max_length=255, required=False)
    bank = serializers.CharField(max_length=255, required=False)

    class Meta:
        model = MerchantAccount
        fields = [
            "gps_address",
            "physical_address",
            "business_email",
            "business_phone",
            "business_tax_ID",
            "postal_address",
            "id_first_director",
            "id_second_director",
            "expected_monthly_turnover",
            "business_description",
            "bank_account_number",
            "bank_branch",
            "bank"
            ]
    

class ComplianceDocumentUploadSerializer(serializers.ModelSerializer):
    
    business_incorporation = serializers.FileField(required=False)
    form_a = serializers.FileField(required=False)
    form_three_and_four = serializers.FileField(required=False)
    logo = serializers.FileField(required=False)
    
    class Meta:
        model = MerchantAccount
        fields = [
            "id",
            "business_incorporation",
            "form_a",
            "form_three_and_four",
            "logo"
            ]