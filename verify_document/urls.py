# from django.contrib import admin
from django.urls import path

from verify_document.views import Test

# from verify_document.views import VerifyGhanaCard

urlpatterns = [

    path("test/", Test, name = "test")
#     path("document/", VerifyGhanaCard.as_view(), name = "verify_doc")
]
