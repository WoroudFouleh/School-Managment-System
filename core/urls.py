from rest_framework.routers import DefaultRouter
from tutorial.quickstart.views import UserViewSet

from .views import *
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'students',StudentViewSet, basename='student')
router.register(r'schools',SchoolViewSet, basename='school')
router.register(r'classrooms',ClassroomViewSet, basename='classroom')
urlpatterns = router.urls