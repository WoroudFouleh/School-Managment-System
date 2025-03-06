from django.shortcuts import render
from .models import Student, Classroom, School
from django.views import View
from .serializers import SchoolSerializer, StudentSerializer, ClassroomSerializer
from django.http import JsonResponse
import json

# Create your views here.
class StudentView(View):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)

    def post(self, request):
        try:
            data = json.loads(request.body)
            serializer = StudentSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
            return JsonResponse(serializer.errors, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    def put(self, request, student_id):
        try:
            student = Student.objects.get(pk=student_id)
            data = json.loads(request.body)
            for key, value in data.items():
                setattr(student, key, value)

            student.save()
            serializer = StudentSerializer(student)
            return JsonResponse(serializer.data, status=200)

        except Student.DoesNotExist:
            return JsonResponse({'error': 'Student not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    def delete(self, request, student_id):
        try:
            student = Student.objects.get(pk=student_id)
            student.delete()
            return JsonResponse({'message': 'Student deleted successfully'}, status=204)
        except Student.DoesNotExist:
            return JsonResponse({'error': 'Student not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

class ClassroomView(View):
    def get(self, request):
        classrooms = Classroom.objects.all()
        serializer = ClassroomSerializer(classrooms, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)

    def post(self, request):
        try:
            data = json.loads(request.body)
            serializer = ClassroomSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
            return JsonResponse(serializer.errors, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    def put(self, request, class_id):
        try:
            classroom = Classroom.objects.get(pk=class_id)
            data = json.loads(request.body)
            for key, value in data.items():
                setattr(classroom, key, value)

            classroom.save()
            serializer = ClassroomSerializer(classroom)
            return JsonResponse(serializer.data, status=200)

        except Classroom.DoesNotExist:
            return JsonResponse({'error': 'Classroom not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    def delete(self, request, class_id):
        try:
            classroom = Classroom.objects.get(pk=class_id)
            classroom.delete()
            return JsonResponse({'message': 'Class deleted successfully'}, status=204)
        except Classroom.DoesNotExist:
            return JsonResponse({'error': 'Class not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)


class SchoolView(View):
    def get(self, request):
        schools = School.objects.all()
        serializer = SchoolSerializer(schools, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)

    def post(self, request):
        try:
            data = json.loads(request.body)
            serializer = SchoolSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
            return JsonResponse(serializer.errors, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    def put(self, request, school_id):
        try:
            school = School.objects.get(pk=school_id)
            data = json.loads(request.body)
            for key, value in data.items():
                setattr(school, key, value)

            school.save()
            serializer = SchoolSerializer(school)
            return JsonResponse(serializer.data, status=200)

        except School.DoesNotExist:
            return JsonResponse({'error': 'School not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    def delete(self, request, school_id):
        try:
            school = School.objects.get(pk=school_id)
            school.delete()
            return JsonResponse({'message': 'School deleted successfully'}, status=204)
        except School.DoesNotExist:
            return JsonResponse({'error': 'School not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

