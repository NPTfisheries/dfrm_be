from django.urls import include, path
from rest_framework import routers
from administration import views

router = routers.DefaultRouter()
router.register(r'departments', views.DepartmentViewSet)
router.register(r'divisions', views.DivisionViewSet)
router.register(r'projects', views.ProjectViewSet)
router.register(r'tasks', views.TaskViewSet)
router.register(r'facilities', views.FacilityViewSet)
# add more viewsets here

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

app_name = 'administration'

urlpatterns = [
    path('', include(router.urls)),
]
