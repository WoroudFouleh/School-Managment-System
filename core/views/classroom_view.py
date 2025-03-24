from typing import Optional, Dict, Any
from django.http import JsonResponse, HttpRequest
from rest_framework.viewsets import ViewSet
from core.components.classroom_component import ClassroomComponent


class ClassroomViewSet(ViewSet):
    """
    ViewSet for managing classroom-related API operations.

    - `list()`: Retrieve all classrooms.
    - `retrieve()`: Retrieve a specific classroom by ID.
    - `create()`: Create a new classroom.
    - `update()`: Update an existing classroom.
    - `destroy()`: Delete a classroom.
    """

    def list(self, request: HttpRequest) -> JsonResponse:
        """ Retrieve a list of all classrooms. """
        return JsonResponse(ClassroomComponent.get_all_classrooms(), safe=False)

    def retrieve(self, request: HttpRequest, pk: Optional[int] = None) -> JsonResponse:
        """ Retrieve a specific classroom by ID. """
        classroom: Optional[Dict[str, Any]] = ClassroomComponent.get_classroom_by_id(pk)
        if classroom is None:
            return JsonResponse({'error': 'Classroom not found'}, status=404)
        return JsonResponse(classroom, safe=False)

    def create(self, request: HttpRequest) -> JsonResponse:
        """ Create a new classroom with the provided data. """
        name: str = request.data.get("name")
        section: str = request.data.get("section")
        num_chairs: int = request.data.get("num_chairs")
        school_id: int = request.data.get("school_id")

        classroom: Dict[str, Any] = ClassroomComponent.create_classroom(name, section, num_chairs, school_id)
        return JsonResponse(classroom, status=201)

    def update(self, request: HttpRequest, pk: Optional[int] = None) -> JsonResponse:
        """ Update an existing classroom by ID. """
        name: str = request.data.get("name")
        section: str = request.data.get("section")
        num_chairs: int = request.data.get("num_chairs")
        school_id: int = request.data.get("school_id")

        classroom: Optional[Dict[str, Any]] = ClassroomComponent.update_classroom(pk, name, section, num_chairs, school_id)
        if classroom is None:
            return JsonResponse({'error': 'Classroom not found'}, status=404)
        return JsonResponse(classroom)

    def destroy(self, request: HttpRequest, pk: Optional[int] = None) -> JsonResponse:
        """ Delete a classroom by ID. """
        if not ClassroomComponent.delete_classroom(pk):
            return JsonResponse({'error': 'Classroom not found'}, status=404)
        return JsonResponse({'status': 'deleted'})
