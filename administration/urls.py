from django.urls import include, path
from rest_framework import routers
from administration import views

router = routers.DefaultRouter()
router.register(r'department', views.DepartmentViewSet)
router.register(r'division', views.DivisionViewSet)
router.register(r'project', views.ProjectViewSet)
router.register(r'subproject', views.SubprojectViewSet)
router.register(r'task', views.TaskViewSet)
router.register(r'facility', views.FacilityViewSet)
# add more viewsets here

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

app_name = 'administration'

urlpatterns = [
    path('', include(router.urls)),
]


#'department/' get list
#'department/' post new
#'department/slug/' get
#'department/slug/' update
#'department/slug/' delete
# /subproject/?project_id=<project_id> for subprojects for provided <project_id>

