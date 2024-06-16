from django.urls import path

from the_mock.views import PayboxBillsMockView, PayboxCollectionMockView, PayboxTransactionDetailsMockView, PayboxSettlementMockView, PayboxTransactionEInvoiceMockView, PayboxBillsPaymentMockView

urlpatterns = [
    path("paybox/collections", PayboxCollectionMockView.as_view(), name="collections"),
    path("paybox/settlement", PayboxSettlementMockView.as_view(), name="settlement"),
    path("paybox/transaction-details/<str:id>", PayboxTransactionDetailsMockView.as_view(), name="transaction-details"),
    path("paybox/e-invoice/create", PayboxTransactionEInvoiceMockView.as_view(), name="e-invoice/create"),
    path("paybox/get-bills", PayboxBillsMockView.as_view(), name="get-bills"),
    path("paybox/pay-bills", PayboxBillsPaymentMockView.as_view(), name="pay-bills"),
]