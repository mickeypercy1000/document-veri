from django.contrib import admin

from the_mock.models import (
    PayboxCollectionMock,
    PayboxLadderWalletMock,
    PayboxUserWalletMock,
)

admin.site.register(PayboxCollectionMock)
admin.site.register(PayboxUserWalletMock)
admin.site.register(PayboxLadderWalletMock)
