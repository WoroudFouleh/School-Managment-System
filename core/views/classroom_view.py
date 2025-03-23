from django.http import JsonResponse
from rest_framework.viewsets import ViewSet

from core.components.classroom_component import ClassroomComponent


class ClassroomViewSet(ViewSet):
    def list(self, request):
        return JsonResponse(ClassroomComponent.get_all_classrooms(), safe=False)

    def retrieve(self, request, pk=None):
        classroom = ClassroomComponent.get_classroom_by_id(pk)
        if classroom is None:
            return JsonResponse({'error': 'Classroom not found'}, status=404)
        return JsonResponse(classroom, safe=False)

    def create(self, request):
        name = request.data.get("name")
        section = request.data.get("section")
        num_chairs = request.data.get("num_chairs")
        school_id = request.data.get("school_id")

        return JsonResponse(
            ClassroomComponent.create_classroom(name, section, num_chairs, school_id),
            status=201
        )

    def update(self, request, pk=None):
        name = request.data.get("name")
        section = request.data.get("section")
        num_chairs = request.data.get("num_chairs")
        school_id = request.data.get("school_id")

        classroom = ClassroomComponent.update_classroom(pk, name, section, num_chairs, school_id)
        if classroom is None:
            return JsonResponse({'error': 'Classroom not found'}, status=404)
        return JsonResponse(classroom)

    def destroy(self, request, pk=None):
        if not ClassroomComponent.delete_classroom(pk):
            return JsonResponse({'error': 'Classroom not found'}, status=404)
        return JsonResponse({'status': 'deleted'})
