from rest_framework.routers import DefaultRouter
from tutorial.quickstart.views import UserViewSet

from core.views import *

from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'classrooms',ClassroomViewSet, basename='classroom')
urlpatterns = router.urls