from django.db import models
import uuid
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Settlement(models.Model):

    class SettlementCodes(models.TextChoices):
        PENDING = 'PENDING', _("Pending")
        APPROVED = 'APPROVED', _("Approved")
        REJECTED = 'REJECTED', _("Rejected")
        FLAGGED = 'FLAGGED', _("Flagged")

    id = models.CharField(
        _("id"),
        max_length=50,
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
    )
    reference_id = models.CharField(max_length=25, blank=True, null=True)
    source_name = models.CharField(max_length=190, blank=True, null=True)
    amount = models.DecimalField(max_digits=19, decimal_places=2)

    fee = models.DecimalField(
        max_digits=19,
        decimal_places=2,
        null=True,
        blank=True,
        default=0.00
    )
    network = models.CharField(verbose_name=_("Network"), null=True, blank=True)
    settlement_status = models.CharField(_("Settlement Status"), choices=SettlementCodes.choices, default=SettlementCodes.PENDING, null=True, blank=True)
    Note = models.TextField(null=True, blank=True)
    reference = models.CharField(_("Reference"), max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated At"), auto_now=True)

    class Meta:
        ordering = ("-updated_at",)

    def __str__(self):
        return f"Settlement_id: {self.id} - Status: {self.settlement_status} - Network: {self.network} - Amount: {self.amount} - Created At: {self.created_at}"
