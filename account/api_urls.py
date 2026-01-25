from django.urls import path
from .api_views import HealthCheckAPI

urlpatterns = [
    path("health/",HealthCheckAPI.as_view(),name='api_health')
]