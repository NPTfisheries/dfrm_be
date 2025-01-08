from django.urls import include, path
from rest_framework import routers
from .views import InstrumentViewSet #, ActivityViewSet, FieldViewSet

router = routers.DefaultRouter()
# # add more viewsets here
router.register(r'instruments', InstrumentViewSet)
# router.register(r'activities', ActivityViewSet)
# router.register(r'fields', FieldViewSet)

app_name = 'data'

urlpatterns = [
    path('', include(router.urls)),
]

