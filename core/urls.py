from rest_framework import routers

from core.views.classroom_view import ClassroomViewSet
from core.views.school_view import SchoolViewSet
from core.views.student_view import StudentViewSet

router = routers.DefaultRouter()
router.register(r'students',StudentViewSet, basename='student')
router.register(r'schools',SchoolViewSet, basename='school')
router.register(r'classrooms',ClassroomViewSet, basename='classroom')
urlpatterns = router.urls