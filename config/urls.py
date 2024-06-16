"""config URL Configuration
"""


from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', include('swagger.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include("authentication.urls")),
    path('account/', include("merchant.urls")),
    path('transfers/', include("transaction.urls")),
    path('settlements/', include("settlements.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)