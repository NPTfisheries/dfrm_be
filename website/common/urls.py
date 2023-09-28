from django.urls import include, path
from rest_framework import routers
from common import views

router = routers.DefaultRouter()
router.register(r'lookup', views.ObjectLookUpView)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

app_name = 'common'

urlpatterns = [
    path('', include(router.urls)),
]

#'lookup/' get list