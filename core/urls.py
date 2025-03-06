from .views import *
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    # students API
    path('students/', csrf_exempt(StudentView.as_view()), name='student-list'),
    path('students/<int:student_id>/', csrf_exempt(StudentView.as_view()), name='student-detail'),
    # classroom API
    path('classrooms/', csrf_exempt(ClassroomView.as_view()), name='classroom-list'),
    path('classrooms/<int:class_id>/', csrf_exempt(ClassroomView.as_view()), name='classroom-detail'),
    # school API
    path('schools/', csrf_exempt(SchoolView.as_view()), name='school-list'),
    path('schools/<int:school_id>/', csrf_exempt(SchoolView.as_view()), name='school-detail'),

]