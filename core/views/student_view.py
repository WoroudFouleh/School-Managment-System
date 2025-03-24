from typing import Optional, Dict, Any
from django.http import JsonResponse, HttpRequest
from rest_framework.viewsets import ViewSet
from core.components.student_component import StudentComponent


class StudentViewSet(ViewSet):
    """
    ViewSet for managing student-related API operations.

    - `list()`: Retrieve all students.
    - `retrieve()`: Retrieve a specific student by ID.
    - `create()`: Create a new student.
    - `update()`: Update an existing student.
    - `destroy()`: Delete a student.
    """

    def list(self, request: HttpRequest) -> JsonResponse:
        """ Retrieve a list of all students. """
        return JsonResponse(StudentComponent.get_all_students(), safe=False)

    def retrieve(self, request: HttpRequest, pk: Optional[int] = None) -> JsonResponse:
        """ Retrieve a specific student by ID. """
        student: Optional[Dict[str, Any]] = StudentComponent.get_student_by_id(pk)
        if student is None:
            return JsonResponse({'error': 'Student not found'}, status=404)
        return JsonResponse(student, safe=False)

    def create(self, request: HttpRequest) -> JsonResponse:
        """ Create a new student with the provided data. """
        first_name: str = request.data.get("first_name")
        last_name: str = request.data.get("last_name")
        date_of_birth: str = request.data.get("date_of_birth")  # Assuming it is a string, should be converted to date
        email: str = request.data.get("email")
        city: str = request.data.get("city")
        ID_number: str = request.data.get("ID_number")
        address: str = request.data.get("address")
        school_id: int = int(request.data.get("school_id"))
        classroom_id: int = int(request.data.get("classroom_id"))

        student: Dict[str, Any] = StudentComponent.create_student(
            first_name, last_name, date_of_birth, email, city,
            ID_number, address, school_id, classroom_id
        )
        return JsonResponse(student, status=201)

    def update(self, request: HttpRequest, pk: Optional[int] = None) -> JsonResponse:
        """ Update an existing student by ID. """
        first_name: str = request.data.get("first_name")
        last_name: str = request.data.get("last_name")
        date_of_birth: str = request.data.get("date_of_birth")  # Convert to datetime if necessary
        email: str = request.data.get("email")
        city: str = request.data.get("city")
        ID_number: str = request.data.get("ID_number")
        address: str = request.data.get("address")
        school_id: int = int(request.data.get("school_id"))
        classroom_id: int = int(request.data.get("classroom_id"))

        student: Optional[Dict[str, Any]] = StudentComponent.update_student(
            pk, first_name, last_name, date_of_birth, email, city,
            ID_number, address, school_id, classroom_id
        )
        if student is None:
            return JsonResponse({'error': 'Student not found'}, status=404)
        return JsonResponse(student)

    def destroy(self, request: HttpRequest, pk: Optional[int] = None) -> JsonResponse:
        """ Delete a student by ID. """
        if not StudentComponent.delete_student(pk):
            return JsonResponse({'error': 'Student not found'}, status=404)
        return JsonResponse({'status': 'deleted'})
