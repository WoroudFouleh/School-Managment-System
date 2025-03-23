from django.http import JsonResponse
from rest_framework.viewsets import ViewSet

from core.components.school_component import SchoolComponent


class SchoolViewSet(ViewSet):
    def list(self, request):
        return JsonResponse(SchoolComponent.get_all_schools(), safe=False)

    def retrieve(self, request, pk=None):
        school = SchoolComponent.get_school_by_id(pk)
        if school is None:
            return JsonResponse({'error': 'School not found'}, status=404)
        return JsonResponse(school, safe=False)

    def create(self, request):
        name = request.data.get("name")
        address = request.data.get("address")
        phone_number = request.data.get("phone_number")
        manager_name = request.data.get("manager_name")
        type = request.data.get("type")
        gender_type = request.data.get("gender_type")

        return JsonResponse(
            SchoolComponent.create_school(name, address, phone_number, manager_name, type, gender_type),
            status=201
        )

    def update(self, request, pk=None):
        name = request.data.get("name")
        address = request.data.get("address")
        phone_number = request.data.get("phone_number")
        manager_name = request.data.get("manager_name")
        type = request.data.get("type")
        gender_type = request.data.get("gender_type")

        school = SchoolComponent.update_school(pk, name, address, phone_number, manager_name, type, gender_type)
        if school is None:
            return JsonResponse({'error': 'School not found'}, status=404)
        return JsonResponse(school)

    def destroy(self, request, pk=None):
        if not SchoolComponent.delete_school(pk):
            return JsonResponse({'error': 'School not found'}, status=404)
        return JsonResponse({'status': 'deleted'})



