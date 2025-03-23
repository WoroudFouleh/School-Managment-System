from django.http import JsonResponse
from rest_framework.viewsets import ViewSet

from core.components.student_component import StudentComponent


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
        first_name = request.data.get("first_name")
        last_name = request.data.get("last_name")
        date_of_birth = request.data.get("date_of_birth")
        email = request.data.get("email")
        city = request.data.get("city")
        ID_number = request.data.get("ID_number")
        address = request.data.get("address")
        school_id = request.data.get("school_id")
        classroom_id = request.data.get("classroom_id")

        return JsonResponse(
            StudentComponent.create_student(first_name, last_name, date_of_birth, email, city,
                                            ID_number, address, school_id, classroom_id),
            status=201
        )

    def update(self, request, pk=None):
        first_name = request.data.get("first_name")
        last_name = request.data.get("last_name")
        date_of_birth = request.data.get("date_of_birth")
        email = request.data.get("email")
        city = request.data.get("city")
        ID_number = request.data.get("ID_number")
        address = request.data.get("address")
        school_id = request.data.get("school_id")
        classroom_id = request.data.get("classroom_id")

        student = StudentComponent.update_student(pk, first_name, last_name, date_of_birth, email, city,
                                                  ID_number, address, school_id, classroom_id)
        if student is None:
            return JsonResponse({'error': 'Student not found'}, status=404)
        return JsonResponse(student)

    def destroy(self, request, pk=None):
        if not StudentComponent.delete_student(pk):
            return JsonResponse({'error': 'Student not found'}, status=404)
        return JsonResponse({'status': 'deleted'})

