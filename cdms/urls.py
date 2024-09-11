from django.urls import include, path
from rest_framework import routers
from .views import CdmsDataView

router = routers.DefaultRouter()
# add more viewsets here

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

app_name = 'cdms'

urlpatterns = [
    path('cdms-data/', CdmsDataView.as_view(), name='cdms_data'),
]

