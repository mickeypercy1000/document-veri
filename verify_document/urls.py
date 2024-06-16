from django.contrib import admin
from django.urls import path

from verify_document.views import VerifyGhanaCard

urlpatterns = [
    path("document/", VerifyGhanaCard.as_view(), name = "verify_doc")
]
