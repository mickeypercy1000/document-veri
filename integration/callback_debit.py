import requests
from rest_framework.response import Response
from settlements.views import Settlement
from transaction.models import Transaction
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view


@csrf_exempt
@api_view(["POST", "GET"])
def get_data_by_reference_id(request):
    referenceid = request.data.get('reference')
    print(referenceid)
    if referenceid:
        transaction = Transaction.objects.get(reference=referenceid)
        if transaction:
            transaction.callback_data = request.data
            transaction.save()
            if request.data.get('status') == "SUCCESSFUL" or request.data.get('message') == "Transaction successful":
                transaction.status = Transaction.STATUS_CODES.SUCCESSFUL
                transaction.status_message = Transaction.STATUS_MESSAGES.SUCCESSFUL
                transaction.save()

            elif request.data.get('status') == "FAILED" or request.data.get('message') == "Transaction failed":
                transaction.status = Transaction.STATUS_CODES.FAILED
                transaction.status_message = Transaction.STATUS_MESSAGES.FAILED
                transaction.save()
            if Settlement(status, transaction):
                return True

        else:
            return Response({"error": "transaction doesn't exist"})
    return Response({"error": "reference doesn't exist"})
