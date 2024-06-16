from urllib import response
from rest_framework import generics, permissions, status
from merchant.models import MerchantAccount
from transaction.serializers import MobileMoneyDebitSerializer, MobileMoneyNamecheckSerializer
from integration.views import wingipay_name_check, wingipayDebitCustomer
from transaction.models import Transaction
from rest_framework.response import Response
from transaction.serializers import TransactionSerializer



# Create your views here.
class MobileMoneyNamecheck(generics.GenericAPIView):
    serializer_class = MobileMoneyNamecheckSerializer
    queryset = Transaction.objects.all()
    # permission_classes = [permissions.IsAuthenticated, ]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone = serializer.validated_data.get('phone')
        network = serializer.validated_data.get('network')
        namecheck = wingipay_name_check(phone, network)
        return Response({
            "message": namecheck
        })


class MobileMoneyDebit(generics.GenericAPIView):
    serializer_class = MobileMoneyDebitSerializer
    queryset = Transaction.objects.all()
    # permission_classes = [permissions.IsAuthenticated, ]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        apikey = serializer.validated_data["api_key"]
        source_phone = serializer.validated_data["source_phone"]
        network = serializer.validated_data["network"].upper()
        amount = float(serializer.validated_data["amount"])
        source_name = serializer.validated_data["source_name"]
        note = serializer.validated_data["note"]
        client_transaction_id = serializer.validated_data["client_transaction_id"]
        debit_callback_url = str(serializer.validated_data["debit_callback_url"])

        try:
            # user = request.user
            request_data = {
                "apikey": apikey,
                "source_phone": source_phone,
                "network": network,
                "amount": amount,
                "note": note,
                "source_name": source_name,
                "client_transaction_id": client_transaction_id,
                "debit_callback_url": debit_callback_url,
            }
            merchant_transaction_limit = MerchantAccount.objects.get(id="0f32020d-1334-4331-a5d4-3ac40ee6a36a")
            limit = float(merchant_transaction_limit.transaction_limit)
            if amount > limit:
                return Response({"message": f"Transaction limit exceeded. You cannot send more than GHS{limit}"})
            
            transaction = Transaction.objects.create(
                source_data=request_data,
                amount=amount,
                network=network,
                status_code=Transaction.StatusCodes.PENDING,
                status_message=Transaction.StatusMessages.PENDING,
                api_key=apikey,

                )
            transaction.save()
            debit_call = wingipayDebitCustomer(transaction)
            response_data = {
                "source_name": transaction.source_data["source_name"],
                "network": transaction.source_data["network"],
                "phone": transaction.source_data["source_phone"],
                "note": transaction.source_data["note"],
                "status": debit_call["debit_call_response"]["status"],
                "transaction_date": debit_call["debit_call_response"]["date"],
                "transaction_message": debit_call["debit_call_response"]["message"],
                "reference": debit_call["debit_call_response"]["reference"],
                "external_transaction_id": debit_call["debit_call_response"]["external_transaction_ref"],
            }
            transaction.reference = debit_call["debit_call_response"]["reference"]
            transaction.save()
            return Response({
                "debit_call_response": response_data,
            })
            
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class GetAllTransactions(generics.RetrieveUpdateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
