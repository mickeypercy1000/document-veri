from django.db import models
import uuid
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Transaction(models.Model):

    SERVICES = [
        ['MTN', 'MTN MOBILE MONEY'],
        ['VODAFONE', 'VODAFONE CASH'],
        ['AIRTELTIGO', 'AIRTELTIGO CASH']
    ]

    class StatusCodes(models.TextChoices):
        PENDING = 'PENDING', 'Pending'
        SUCCESSFUL = 'SUCCESSFUL', 'Successful'
        FAILED = 'FAILED', 'Failed'

    class StatusMessages(models.TextChoices):
        PENDING = 'PENDING', 'Transaction Pending'
        SUCCESSFUL = 'SUCCESSFUL', 'Transaction Successful'
        FAILED = 'FAILED', 'Transaction Failed'

    id = models.CharField(
        _("id"),
        max_length=50,
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
    )
    # reference_id = models.CharField(max_length=25, blank=True, null=True)
    amount = models.DecimalField(max_digits=19, decimal_places=2)
    # fee_rate = models.ForeignKey(
    #     FeeRate,
    #     related_name="transaction_charge",
    #     on_delete=models.SET_NULL,
    #     blank=True,
    #     null=True
    # )

    # fee = models.DecimalField(
    #     max_digits=19,
    #     decimal_places=2,
    #     null=True,
    #     blank=True,
    #     default=0.00
    # )
    is_fee_deducted = models.BooleanField(default=False, blank=True, null=True)
    network = models.TextField(verbose_name=_("Network"), null=True, blank=True)
    status_code = models.CharField(verbose_name=_("Status Code"), max_length=25, null=True, blank=True)
    status_message = models.TextField(null=True, blank=True)
    is_live = models.BooleanField(default=False)
    source_data = models.JSONField(_("Source Transaction Data"), null=True, blank=True)
    destination_data = models.JSONField(_("Destination Transaction Data"), null=True, blank=True)
    device_info = models.JSONField(_("Device Info"), null=True, blank=True)
    api_key = models.CharField(_("API prefix"), max_length=50, null=True, blank=True)
    reference = models.CharField(_("Reference"), max_length=50, null=True, blank=True)
    source_name = models.CharField(_("Source Name"), max_length=150, null=True, blank=True)
    source_phone = models.CharField(_("Phone"), max_length=10, null=True, blank=True)
    callback_data = models.JSONField(_("Callback Data"), null=True, blank=True)

    # apikey = models.ForeignKey(AccountAPIKey, on_delete=models.SET_NULL, null=True, blank=True)

    # batch = models.ForeignKey(
    #     Batch,
    #     verbose_name=_("Batch"),
    #     related_name="batch_transaction",
    #     on_delete=models.SET_NULL,
    #     null=True,
    #     blank=True,
    # )
    # is_payout = models.BooleanField(default=False)
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    update_at = models.DateTimeField(_("Updated At"), auto_now=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return f"Trans_id: {self.id} - Status: {self.status_code} - Network: {self.network} - Amount: {self.amount} - Created At: {self.created_at}"
