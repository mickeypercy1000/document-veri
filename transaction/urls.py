from django.urls import path
from integration.callback_debit import get_data_by_reference_id
from transaction.views import GetAllTransactions, MobileMoneyNamecheck, MobileMoneyDebit


urlpatterns = [
    path("mobile-money/namecheck", MobileMoneyNamecheck.as_view(), name="namecheck"),
    path("mobile-money/debit-transfer", MobileMoneyDebit.as_view(), name="debit_transfer"),
    path('debit-callback/', get_data_by_reference_id, name='debit_callback'),
    # path('all-transactions/', GetAllTransactions.as_view(), name='all-transactions'),
    ]