from ast import Return
from rest_framework import generics, status, permissions
from authentication.models import User
from merchant.models import MerchantAccount
from merchant.serializers import ComplianceSerializer, ComplianceDocumentUploadSerializer
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema

# Create your views here.
class Compliance(generics.RetrieveUpdateAPIView):
    queryset = MerchantAccount.objects.all()
    serializer_class = ComplianceSerializer
    lookup_field = "pk"
    perminssion_classes = (permissions.IsAuthenticated, )

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        instance.kyc = dict(serializer.validated_data)
        instance.save()
        kyc_data = ComplianceSerializer(dict(serializer.validated_data), many=False).data

        return Response({
            "account_id": instance.id,
            "name": instance.user.get_fullname(),
            "phone": instance.user.phone,
            "email": instance.user.get_email(),
            "kyc_data": kyc_data
            })


class ComplianceDocumentUpload(generics.UpdateAPIView):
    queryset = MerchantAccount.objects.all()
    serializer_class = ComplianceDocumentUploadSerializer
    parser_classes = (FormParser, MultiPartParser)
    permission_classes = (permissions.IsAuthenticated, )
    lookup_field = "pk"

    def update(self, request, *args, **kwargs):
        """
        This function creates a new document for the authenticated user.
        """
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            instance.business_incorporation = serializer.validated_data.get('business_incorporation')
            instance.form_a = serializer.validated_data.get('form_a')
            instance.form_three_and_four = serializer.validated_data.get('form_three_and_four')
            instance.logo = serializer.validated_data.get('logo')
            instance.save()

            return Response({
                "message": "Documents uploaded successfully",
                "documents": serializer.data
            }, status=status.HTTP_201_CREATED)
        except Exception:
            return Response({"message": "Document upload failed"}, status=status.HTTP_400_BAD_REQUEST)


class GetComplianceData(generics.RetrieveAPIView):
    serializer_class = ComplianceDocumentUploadSerializer, ComplianceSerializer
    queryset = MerchantAccount.objects.all()
    perminssion_classes = (permissions.IsAuthenticated, )
    lookup_field = "pk"

    def get(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
        except MerchantAccount.DoesNotExist:
            return Response({"message": "Account not found"})

        form_a = instance.form_a
        business_incorporation = instance.business_incorporation
        form_three_and_four = instance.form_three_and_four
        logo = instance.logo

        if not form_a:
            form_a = ""

        if not business_incorporation:
            business_incorporation = ""

        if not form_three_and_four:
            form_three_and_four = ""

        if not instance.logo:
            logo = ""
            
        business_documents = {
            "form_a": form_a,
            "business_incorporation": business_incorporation,
            "form_three_and_four": form_three_and_four,
            "logo": logo
        }
        personal_data = {
            "name": instance.user.get_fullname(),
            "email": instance.user.email,
            "phone": instance.user.phone,
        }
        document_serializer = ComplianceDocumentUploadSerializer(business_documents, many=False)
        return Response({
            "personal_data": personal_data,
            "business_data": instance.kyc,
            "business_documents": document_serializer.data
            }, status=status.HTTP_200_OK)