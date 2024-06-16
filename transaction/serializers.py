from email import feedparser
from rest_framework import serializers
from integration import validators
from transaction.models import Transaction


class MobileMoneyNamecheckSerializer(serializers.ModelSerializer):
    
    phone = serializers.CharField(
        max_length=10, required=True, allow_blank=False, validators=[validators.phone_validator],
        error_messages={
            "blank": "Provide a valid phone number",
            "required": "Phone number is required",
        })
    network = serializers.CharField(
        max_length=15, required=True, allow_blank=False, validators=[validators.network_validator],
        error_messages={
            "blank": "Provide a valid network",
            "required": "Network is required",
        })

    class Meta:
        model = Transaction
        fields = ["api_key", "phone", "network"]
    

class MobileMoneyDebitSerializer(serializers.ModelSerializer):

    # apikey = serializers.CharField(
    #     required=True, max_length=50,
    #     error_messages={
    #         "blank": " API Key cannot be blak",
    #         "required": "API Key is required",
    #     })
    source_phone = serializers.CharField(
        max_length=10, required=True, allow_blank=False, validators=[validators.phone_validator],
        error_messages={
            "blank": "Provide a valid phone number",
            "required": "Phone number is required",
        })
    network = serializers.CharField(
        max_length=15, required=True, allow_blank=False, validators=[validators.network_validator],
        error_messages={
            "blank": "Provide a valid network",
            "required": "Network is required",
        })
    amount = serializers.DecimalField(
        decimal_places=2, max_digits=6, required=True,
        error_messages={
            "blank": "Enter a valid amount",
            "required": "Enter a valid amount",
            "invalid": "Enter a valid amount",
        })
    source_name = serializers.CharField(
        required=True, max_length=100,
        error_messages={
            "blank": "Sender's name cannot be blak",
            "required": "Sender's name is required",
        })
    note = serializers.CharField(
        required=True, max_length=190,
        error_messages={
            "blank": "Note cannot be blank",
            "required": "Note is required",
        })
    client_transaction_id = serializers.CharField(
        required=True, max_length=50,
        error_messages={
            "blank": "Transaction ID cannot be blank",
            "required": "Transaction ID is required",
        })
    debit_callback_url = serializers.CharField(
        required=True, max_length=250,
        error_messages={
            "blank": "Debit callback URL cannot be blank",
            "required": "Debit callback URL is required",
        })

    class Meta:
        model = Transaction
        fields = ["api_key", "source_phone", "network", "amount", "source_name", "note", "client_transaction_id", "debit_callback_url"]


class TransactionSerializer(serializers.ModelSerializer):
    model = Transaction
    fields = [ 
        "__all__"
    ]