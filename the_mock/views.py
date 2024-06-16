from decimal import Decimal
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from the_mock.models import PayboxCollectionMock, PayboxLadderWalletMock, PayboxUserWalletMock
from the_mock.serializers import PayboxBillPaymentMockSerializer, PayboxCollectionMockSerializer, PayboxEinvoiceMockSerializer, PayboxTransferMockSerializer


class PayboxCollectionMockView(generics.GenericAPIView):
    serializer_class = PayboxCollectionMockSerializer
    # authentication_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            order_id = serializer.validated_data["order_id"]
            currency = serializer.validated_data["currency"]
            amount = float(serializer.validated_data["amount"])
            mode = serializer.validated_data["mode"]
            mobile_network = serializer.validated_data["mobile_network"]
            voucher_code = serializer.validated_data["voucher_code"]
            mobile_number = serializer.validated_data["mobile_number"]
            key = serializer.validated_data["key"]
            payerName = serializer.validated_data["payerName"]
            payerPhone = serializer.validated_data["payerPhone"]
            payerEmail = serializer.validated_data["payerEmail"]
            customer_id = serializer.validated_data["customer_id"]
            # callback_url = serializer.validated_data["callback_url"]

            request_data = {
                "order_id": order_id,
                "currency": currency,
                "amount": amount,
                "mode": mode,
                "mobile_network": mobile_network,
                "voucher_code": voucher_code,
                "mobile_number": mobile_number,
                "key": key,
                "payerName": payerName,
                "payerPhone": payerPhone,
                "payerEmail": payerEmail,
                "customer_id": customer_id,
                # "callback_url": callback_url   
            }

            user = request.user
            user_wallet = PayboxUserWalletMock.objects.get(user=user)
            balance_before = float(user_wallet.user_wallet_balance)
            fee = amount*0.019
            balance_after = balance_before - amount - fee

            collections = PayboxCollectionMock.objects.create(
                source_data=request_data,
                user=user,
                fee=fee,
                amount=amount,
                wallet_balance_before=balance_before,
                wallet_balance_after=balance_after,
                )
            collections.save()

            user_wallet.user_wallet_balance = balance_after
            user_wallet.save()

            ladder_paybox_balance = PayboxLadderWalletMock.objects.filter().first()
            new_balance = float(ladder_paybox_balance.ladder_balance)
            final_balance = new_balance + amount

            ladder_paybox_balance.ladder_balance = final_balance
            ladder_paybox_balance.save()

            response_data = {
                "status": "Success",
                "message": "PayBox Gateway Response",
                "token": "8nqF9Zt5s1",
                "timestamp": str(collections.created_at),
                "currency": "GHS",
                "amount": amount,
                "fee": fee,
                "Ladder_balance": str(final_balance),
                "user_balance_after": str(balance_after),
                "user_balance_before": str(balance_before),
                "mode": "Test",
                "payment_processor": "Test",
                "transaction": "Credit",
                "payload": "{\"key\":\"data\"}",
                "order_id": order_id,
                "environment": "Development",
                "callback_url": "null",
                "redirect_url": "null",
                "payer_name": payerName,
                "payer_email": payerEmail,
                "payer_phone": payerPhone,
                "customer_id": customer_id
            }
            collections.response_data = response_data
            collections.save()

            return Response({
                "message": response_data
            })


class PayboxSettlementMockView(generics.GenericAPIView):
    serializer_class = PayboxTransferMockSerializer
    # authentication_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            currency = serializer.validated_data["currency"]
            amount = float(serializer.validated_data["amount"])
            mode = serializer.validated_data["mode"]
            mobile_network = serializer.validated_data["mobile_network"]
            mobile_number = serializer.validated_data["mobile_number"]
            bank_code = serializer.validated_data["bank_code"]
            bank_account = serializer.validated_data["bank_account"]
            callback_url = serializer.validated_data["callback_url"]

            ladder_paybox_balance = PayboxLadderWalletMock.objects.filter().first()
            new_balance = float(ladder_paybox_balance.ladder_balance)
            final_balance = new_balance - amount

            ladder_paybox_balance.ladder_balance = final_balance
            ladder_paybox_balance.save()

            return Response({
                "status": "Success",
                "message": "PayBox Gateway Response",
                "token": "jVJUaZPVhH",
                "timestamp": "2022-02-10T15:19:45.000000Z",
                "currency": "GHS",
                "amount": amount,
                "ladder_balance": final_balance,
                "fee": 0,
                "mode": "Test",
                "payload": "null",
                "order_id": "null",
                "environment": "Development",
                "callback_url": "null"
            })


class PayboxTransactionDetailsMockView(generics.RetrieveAPIView):
    queryset = PayboxCollectionMock.objects.all()
    serializer_class = PayboxCollectionMockSerializer
    lookup_field = "id"
    # authentication_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        instance = self.get_object()

        return Response({
            "status": instance.response_data["status"],
            "token": "Vt3OUJh6qw",
            "timestamp": instance.created_at,
            "currency": instance.currency,
            "amount": instance.amount,
            "fee": instance.fee,
            "mode": instance.response_data["mode"],
            "payload": "null",
            "order_id": instance.response_data["order_id"],
            "payer_name": instance.response_data["payer_name"],
            "payer_email": instance.response_data["payer_email"],
            "payer_phone": instance.response_data["payer_phone"],
            "customer_id": instance.response_data["customer_id"]
        })


class PayboxBillsMockView(generics.ListAPIView):
    # authentication_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return Response({
            "data": [
                {
                    "id": "99de00a1-a252-42f0-80f3-0d0db82caa89",
                    "name": "GBC TV",
                    "alias": "GBCTV",
                    "category": "TV"
                },
                {
                    "id": "71fd4bcb-c998-4b09-afce-195f31b41a15",
                    "name": "GOTVMAX",
                    "alias": "GOTVMAX",
                    "category": "TV"
                },
                {
                    "id": "fb2315ed-2f37-4e57-99d1-7f3233b531ba",
                    "name": "DSTV",
                    "alias": "DSTV",
                    "category": "TV"
                },
                {
                    "id": "c2fffaff-df4e-4796-8189-ec48662cbb10",
                    "name": "Kwese TV",
                    "alias": "KWESETV",
                    "category": "TV"
                },
                {
                    "id": "eaad31cc-53af-459f-8095-464232b485b2",
                    "name": "Vodafone Postpaid",
                    "alias": "VPP",
                    "category": "Postpaid"
                },
                {
                    "id": "1211b46f-0d84-49df-8939-61cf8df15c93",
                    "name": "MTN Postpaid",
                    "alias": "MTNPOSTPAID",
                    "category": "Postpaid"
                },
                {
                    "id": "f65055c0-6b5f-4d3d-837a-43d2d5c89ccd",
                    "name": "Surfline Data",
                    "alias": "SURF",
                    "category": "Internet Data"
                },
                {
                    "id": "937dda6d-7154-4181-b25b-499091709153",
                    "name": "Telesol Data",
                    "alias": "TELESOL",
                    "category": "Internet Data"
                },
                {
                    "id": "a1259862-2910-4287-8f40-c5c8a0bf81f1",
                    "name": "Busy Internet",
                    "alias": "BUSY",
                    "category": "Internet Data"
                },
                {
                    "id": "dae3f1ee-d628-4a3f-9c62-b5620e457654",
                    "name": "MTN Data",
                    "alias": "MTNDATA",
                    "category": "Internet Data"
                },
                {
                    "id": "b790d050-68b3-4d16-9530-942f8f0d7cea",
                    "name": "MTN",
                    "alias": "MTN",
                    "category": "Airtime"
                },
                {
                    "id": "0666efcf-ad7b-4d52-9d8d-5e26a42c113c",
                    "name": "VODAFONE",
                    "alias": "VODAFONE",
                    "category": "Airtime"
                },
                {
                    "id": "99dfa5f8-0ab8-4826-be97-f7455fd88f27",
                    "name": "Airtel-Tigo",
                    "alias": "TIGO",
                    "category": "Airtime"
                },
                {
                    "id": "227faedd-fd30-4d04-a485-10fcf1d0cbe3",
                    "name": "GLO",
                    "alias": "GLO",
                    "category": "Airtime"
                },
                {
                    "id": "6e1748b0-1f96-40b6-bd8c-2dfe4792b177",
                    "name": "AMA Property Rate",
                    "alias": "AMA",
                    "category": "Property Rate"
                },
                {
                    "id": "f0a3d561-5343-44a5-a295-2f536997a276",
                    "name": "Electricity Company Of Ghana",
                    "alias": "ECG",
                    "category": "BILL"
                },
                {
                    "id": "31432ca8-28fc-4918-b252-39bc9eb22612",
                    "name": "Ghana Water Company",
                    "alias": "GWCL",
                    "category": "BILL"
                }
            ]
        })


class PayboxTransactionEInvoiceMockView(generics.GenericAPIView):
    serializer_class = PayboxEinvoiceMockSerializer
    # authentication_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            amount = serializer.validated_data["amount"]
            currency = serializer.validated_data["currency"]
            order_id = serializer.validated_data["order_id"]
            name = serializer.validated_data["name"]
            email = serializer.validated_data["email"]
            contact = serializer.validated_data["contact"]
            customer_id = serializer.validated_data["customer_id"]

            return Response({
                "token": "BOwt8PX96h",
                "status": "Pending",
                "message": "Notification Sent Pending Payment",
                "amount": amount,
                "currency": "GHS",
                "order_id": order_id,
                "customer_id": customer_id,
                "name": name,
                "email": email,
                "contact": contact,
                "url": "https://paybox.com.co/invoice/BOwt8PX96h"
            })


class PayboxBillsPaymentMockView(generics.GenericAPIView):
    serializer_class = PayboxBillPaymentMockSerializer
    # authentication_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            bill_id = serializer.validated_data["bill_id"]
            currency = serializer.validated_data["currency"]
            amount = float(serializer.validated_data["amount"])
            destination_account = serializer.validated_data["destination_account"]
            
            request_data = {
                "bill_id": bill_id,
                "currency": currency,
                "amount": amount,
                "destination_account": destination_account, 
            }

            user = request.user
            user_wallet = PayboxUserWalletMock.objects.get(user=user)
            balance_before = float(user_wallet.user_wallet_balance)
            fee = amount*0.019
            balance_after = balance_before - amount - fee

            collections = PayboxCollectionMock.objects.create(
                source_data=request_data,
                user=user,
                fee=fee,
                amount=amount,
                wallet_balance_before=balance_before,
                wallet_balance_after=balance_after,
                )
            collections.save()

            user_wallet.user_wallet_balance = balance_after
            user_wallet.save()

            ladder_paybox_balance = PayboxLadderWalletMock.objects.filter().first()
            new_balance = float(ladder_paybox_balance.ladder_balance)
            # final_balance = new_balance + amount

            # ladder_paybox_balance.ladder_balance = final_balance
            # ladder_paybox_balance.save()

            response_data = {
                "status": "Success",
                "token": "8nqF9Zt5s1",
                "timestamp": str(collections.created_at),
                "currency": "GHS",
                "amount": amount,
                "fee": fee,
                "Ladder_balance": str(new_balance),
                "user_balance_after": str(balance_after),
                "user_balance_before": str(balance_before),
                "mode": "Paybox",
                "message": "Transaction Successfull Ref:09FG02171944431650526",
                "bill": "Bill Payment",
                "destination_account": destination_account
            }
            collections.response_data = response_data
            collections.save()

            return Response({
                "message": response_data
            })