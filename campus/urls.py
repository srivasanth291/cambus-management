
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/',include('account.urls',namespace='account')),
    path('api/',include('account.api_urls'))
]
