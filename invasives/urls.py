from django.urls import include, path
from rest_framework import routers
from invasives.views import InvasiveSpeciesViewSet

router = routers.DefaultRouter()
router.register(r'invasivespecies', InvasiveSpeciesViewSet)

app_name = 'invasives'

urlpatterns = [
    path('', include(router.urls)),
]
