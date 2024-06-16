from rest_framework import serializers

from the_mock.models import PayboxCollectionMock


class PayboxCollectionMockSerializer(serializers.ModelSerializer):
    order_id = serializers.CharField(required=True)
    currency = serializers.CharField(required=True)
    amount = serializers.DecimalField(max_digits=10, decimal_places=2, required=True)
    mode = serializers.CharField(required=True)
    mobile_network = serializers.CharField(required=True)
    voucher_code = serializers.CharField(required=True)
    mobile_number = serializers.CharField(required=True)
    key = serializers.CharField(required=True)
    payerName = serializers.CharField(required=True)
    payerPhone = serializers.CharField(required=True)
    payerEmail = serializers.EmailField(required=True)
    customer_id = serializers.CharField(required=True)
    callback_url = serializers.CharField(required=True)

    class Meta:
        model = PayboxCollectionMock
        fields = [
            "order_id",
            "currency",
            "amount",
            "mode",
            "order_id",
            "mobile_network",
            "voucher_code",
            "mobile_number",
            "key",
            "payerName",
            "payerPhone",
            "payerEmail",
            "customer_id",
            "callback_url"            
            ]

class PayboxTransferMockSerializer(serializers.ModelSerializer):
    currency = serializers.CharField(required=True)
    amount = serializers.DecimalField(max_digits=10, decimal_places=2, required=True)
    mode = serializers.CharField(required=True)
    mobile_network = serializers.CharField(required=True)
    mobile_number = serializers.CharField(required=True)
    bank_code = serializers.CharField(required=True)
    bank_account = serializers.CharField(required=True)
    callback_url = serializers.CharField(required=True)

    class Meta:
        model = PayboxCollectionMock
        fields = [
            "currency",
            "amount",
            "mode",
            "mobile_network",
            "mobile_number",
            "bank_code",
            "bank_account",
            "callback_url"            
            ]

class PayboxEinvoiceMockSerializer(serializers.ModelSerializer):
    amount = serializers.DecimalField(max_digits=10, decimal_places=2, required=True)
    currency = serializers.CharField(required=True)
    order_id = serializers.CharField(required=True)
    name = serializers.CharField(required=True)
    email = serializers.CharField(required=True)
    contact = serializers.CharField(required=True)
    customer_id = serializers.CharField(required=True)

    class Meta:
        model = PayboxCollectionMock
        fields = [
            "amount",
            "currency",
            "order_id",
            "name",
            "email",
            "contact",
            "customer_id"
            ]


class PayboxBillPaymentMockSerializer(serializers.ModelSerializer):
    bill_id = serializers.CharField(required=True)
    currency = serializers.CharField(required=True)
    destination_account = serializers.CharField(required=True)
    amount = serializers.DecimalField(max_digits=10, decimal_places=2, required=True)
    
    class Meta:
        model = PayboxCollectionMock
        fields = [
            "bill_id",
            "currency",
            "destination_account",
            "amount",
            ]