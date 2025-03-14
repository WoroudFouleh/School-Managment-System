from django.http import JsonResponse
from rest_framework.viewsets import ViewSet

from core.components import *


# Create your views here.
class StudentViewSet(ViewSet):
    def list(self, request):
        return JsonResponse(StudentComponent.get_all_students(), safe=False)

    def retrieve(self, request, pk=None):
        student = StudentComponent.get_student_by_id(pk)
        if student is None:
            return JsonResponse({'error': 'Student not found'}, status=404)
        return JsonResponse(student, safe=False)

    def create(self, request):
        return JsonResponse(StudentComponent.create_student(request.data), status=201)

    def update(self, request, pk=None):
        student = StudentComponent.update_student(pk, request.data)
        if student is None:
            return JsonResponse({'error': 'Student not found'}, status=404)
        return JsonResponse(student)

    def destroy(self, request, pk=None):
        if not StudentComponent.delete_student(pk):
            return JsonResponse({'error': 'Student not found'}, status=404)
        return JsonResponse({'status': 'deleted'})


class ClassroomViewSet(ViewSet):
    def list(self, request):
        return JsonResponse(ClassroomComponent.get_all_classrooms(), safe=False)

    def retrieve(self, request, pk=None):
        classroom = ClassroomComponent.get_classroom_by_id(pk)
        if classroom is None:
            return JsonResponse({'error': 'Classroom not found'}, status=404)
        return JsonResponse(classroom, safe=False)

    def create(self, request):
        return JsonResponse(ClassroomComponent.create_classroom(request.data), status=201)

    def update(self, request, pk=None):
        classroom = ClassroomComponent.update_classroom(pk, request.data)
        if classroom is None:
            return JsonResponse({'error': 'Classroom not found'}, status=404)
        return JsonResponse(classroom)

    def destroy(self, request, pk=None):
        if not ClassroomComponent.delete_classroom(pk):
            return JsonResponse({'error': 'Classroom not found'}, status=404)
        return JsonResponse({'status': 'deleted'})

class SchoolViewSet(ViewSet):
    def list(self, request):
        return JsonResponse(SchoolComponent.get_all_schools(), safe=False)

    def retrieve(self, request, pk=None):
        school = SchoolComponent.get_school_by_id(pk)
        if school is None:
            return JsonResponse({'error': 'School not found'}, status=404)
        return JsonResponse(school, safe=False)

    def create(self, request):
        return JsonResponse(SchoolComponent.create_school(request.data), status=201)

    def update(self, request, pk=None):
        school = SchoolComponent.update_school(pk, request.data)
        if school is None:
            return JsonResponse({'error': 'School not found'}, status=404)
        return JsonResponse(school)

    def destroy(self, request, pk=None):
        if not SchoolComponent.delete_school(pk):
            return JsonResponse({'error': 'School not found'}, status=404)
        return JsonResponse({'status': 'deleted'})






