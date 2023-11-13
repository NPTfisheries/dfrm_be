from django.urls import include, path
from rest_framework import routers
from files import views

router = routers.DefaultRouter()
router.register(r'image', views.ImageViewSet)
router.register(r'document', views.FileViewSet)


app_name = 'files'

urlpatterns = [
    path('', include(router.urls)),
]

#'image/' get list
#'image/' post new
#'image/slug/' get
#'image/slug/' update
#'image/slug/' delete