from django.urls import path
from integration.callback_debit import get_data_by_reference_id
from settlements.views import GetAllSettlements
from transaction.views import MobileMoneyNamecheck, MobileMoneyDebit


urlpatterns = [
    path("all", GetAllSettlements.as_view(), name="all-settlements")
    ]