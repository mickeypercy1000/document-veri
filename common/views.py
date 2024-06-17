from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView

from common.models import Country, DocumentType
from common.serializers import CountrySerializer, DucumentTypeSerializer

class DocumentTypeView(ListCreateAPIView):
    serializer_class = DucumentTypeSerializer
    queryset = DocumentType.objects.all()
    
class CountryView(ListCreateAPIView):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()