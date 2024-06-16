from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from settlements.models import Settlement
from settlements.serializers import SettlementSerializer
from transaction.models import Transaction

# Create your views here.
def SettlementView(transaction):
    settlement = Settlement.objects.create(
        settlement_status = transaction.source_data['status'] ,
        name = transaction.source_data['source_name'] ,
        reference = transaction.source_data['reference'] ,
        amount = transaction.source_data['amount'] ,
        fee = transaction.source_data['fee'] ,
        network = transaction.source_data['network'] ,
        phone = transaction.source_data['source_phone'] ,
    )
    settlement.save()
    return Response({"settlement": True})


class GetAllSettlements(generics.RetrieveUpdateAPIView):
    queryset = Settlement.objects.all()
    serializer_class = SettlementSerializer

