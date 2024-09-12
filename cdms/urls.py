from django.urls import include, path
from rest_framework import routers
from .views import LocationViewSet, DatasetViewSet, InstrumentViewSet, ActivityViewSet, FieldViewSet

router = routers.DefaultRouter()
# add more viewsets here
router.register(r'locations', LocationViewSet)
router.register(r'datasets', DatasetViewSet)
router.register(r'instruments', InstrumentViewSet)
router.register(r'activities', ActivityViewSet)
router.register(r'fields', FieldViewSet)

app_name = 'cdms'

urlpatterns = [
    path('', include(router.urls)),
]

