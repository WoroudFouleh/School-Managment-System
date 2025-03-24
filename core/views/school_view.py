from typing import Optional, Dict, Any
from django.http import JsonResponse, HttpRequest
from rest_framework.viewsets import ViewSet
from core.components.school_component import SchoolComponent


class SchoolViewSet(ViewSet):
    """
    ViewSet for managing school-related API operations.

    - `list()`: Retrieve all schools.
    - `retrieve()`: Retrieve a specific school by ID.
    - `create()`: Create a new school.
    - `update()`: Update an existing school.
    - `destroy()`: Delete a school.
    """

    def list(self, request: HttpRequest) -> JsonResponse:
        """ Retrieve a list of all schools. """
        return JsonResponse(SchoolComponent.get_all_schools(), safe=False)

    def retrieve(self, request: HttpRequest, pk: Optional[int] = None) -> JsonResponse:
        """ Retrieve a specific school by ID. """
        school: Optional[Dict[str, Any]] = SchoolComponent.get_school_by_id(pk)
        if school is None:
            return JsonResponse({'error': 'School not found'}, status=404)
        return JsonResponse(school, safe=False)

    def create(self, request: HttpRequest) -> JsonResponse:
        """ Create a new school with the provided data. """
        name: str = request.data.get("name")
        address: str = request.data.get("address")
        phone_number: str = request.data.get("phone_number")
        manager_name: str = request.data.get("manager_name")
        school_type: str = request.data.get("type")
        gender_type: str = request.data.get("gender_type")

        school: Dict[str, Any] = SchoolComponent.create_school(
            name, address, phone_number, manager_name, school_type, gender_type
        )
        return JsonResponse(school, status=201)

    def update(self, request: HttpRequest, pk: Optional[int] = None) -> JsonResponse:
        """ Update an existing school by ID. """
        name: str = request.data.get("name")
        address: str = request.data.get("address")
        phone_number: str = request.data.get("phone_number")
        manager_name: str = request.data.get("manager_name")
        school_type: str = request.data.get("type")
        gender_type: str = request.data.get("gender_type")

        school: Optional[Dict[str, Any]] = SchoolComponent.update_school(
            pk, name, address, phone_number, manager_name, school_type, gender_type
        )
        if school is None:
            return JsonResponse({'error': 'School not found'}, status=404)
        return JsonResponse(school)

    def destroy(self, request: HttpRequest, pk: Optional[int] = None) -> JsonResponse:
        """ Delete a school by ID. """
        if not SchoolComponent.delete_school(pk):
            return JsonResponse({'error': 'School not found'}, status=404)
        return JsonResponse({'status': 'deleted'})
