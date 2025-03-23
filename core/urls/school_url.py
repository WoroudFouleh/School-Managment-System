
from core.views import *

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'schools',SchoolViewSet, basename='school')

urlpatterns = router.urls