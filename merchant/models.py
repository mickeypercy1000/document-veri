from django.db import models
import uuid
from django.utils.translation import gettext_lazy as _
from authentication.models import User


def user_directory_path(instance, filename):
    # Get the unique identifier of the user
    business_name = instance.user.business_name.replace(' ', '_')
    # Create the subfolder path
    # subfolder = business_name
    # Combine the subfolder path with the filename
    return f'documents/{business_name}/{filename}'


class MerchantAccount(models.Model):
    id = models.CharField(
        _("id"),
        max_length=50,
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="merchant_account", blank=True, null=True)
    kyc = models.JSONField(_("Compliance"), blank=True, null=True)
    # api_key = models.CharField(_("API key"), max_length=50, null=True, blank=True)
    transaction_limit = models.CharField(max_length=10, null=True, blank=True)
    business_incorporation = models.FileField(_("Business Incorporation"), upload_to=user_directory_path)
    form_a = models.FileField(_("Form A"), upload_to=user_directory_path)
    form_three_and_four = models.FileField(_("Form 3 and Form 4"), upload_to=user_directory_path)
    logo = models.FileField(_("Logo"), upload_to=user_directory_path)
    kyc_completed = models.BooleanField(default=False, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"account_id: {self.id} || user_id: {self.user_id} || email: {self.user}"

        
