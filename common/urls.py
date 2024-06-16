from django.contrib import admin
from django.urls import path

from verify_document.views import CountryView, DocumentTypeView

urlpatterns = [
    path("document_type/", DocumentTypeView.as_view(), name = "document-type"),
    path("countries/", CountryView.as_view(), name = "countries"),
]
