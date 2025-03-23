

from core.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'students',StudentViewSet, basename='student')

urlpatterns = router.urls