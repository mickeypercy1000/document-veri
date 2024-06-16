from django.db import models
import uuid
from django.utils.translation import gettext_lazy as _
from authentication.models import User


class PayboxLadderWalletMock(models.Model):
    ladder_balance = models.DecimalField(decimal_places=2, max_digits=10)
    currency = models.CharField(max_length=50, default='GHS')


class PayboxCollectionMock(models.Model):
    source_data = models.JSONField(null=True, blank=True)
    response_data = models.JSONField(null=True, blank=True)
    wallet_balance_before = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
    wallet_balance_after = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
    paybox_ladder_balance = models.ForeignKey(PayboxLadderWalletMock, on_delete=models.CASCADE, null=True, blank=True)
    fee = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    currency = models.CharField(max_length=50, default="GHS")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class PayboxUserWalletMock(models.Model):
    user_wallet_balance = models.DecimalField(decimal_places=2, max_digits=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
