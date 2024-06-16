from django.urls import path
from merchant.views import Compliance, ComplianceDocumentUpload, GetComplianceData

urlpatterns = [
    path("compliance-data/<str:pk>", Compliance.as_view(), name="compliance-data"),
    path("compliance-data/file-upload/<str:pk>", ComplianceDocumentUpload.as_view(), name="compliance-file-upload"),
    path("compliance-data/<str:pk>/get_data", GetComplianceData.as_view(), name="get-compliance-data"),
]