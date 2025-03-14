from .models import *
class StudentRepository:
    @staticmethod
    def get_all_students():
        return Student.objects.all()

    @staticmethod
    def get_student_by_id(student_id):
        try:
            return Student.objects.get(pk=student_id)
        except Student.DoesNotExist:
            return None

    @staticmethod

    def create_student(data):
        try:
            school = School.objects.get(pk=data.pop("school"))
            classroom = Classroom.objects.get(pk=data.pop("classroom"))
        except (School.DoesNotExist, Classroom.DoesNotExist):
            return None

        return Student.objects.create(school=school, classroom=classroom, **data)

    @staticmethod
    def update_student(student, data):
        for key, value in data.items():
            setattr(student, key, value)
        student.save()
        return student

    @staticmethod
    def delete_student(student):
        student.delete()

class ClassroomRepository:
    @staticmethod
    def get_all_classrooms():
        return Classroom.objects.all()

    @staticmethod
    def get_classroom_by_id(classroom_id):
        try:
            return Classroom.objects.get(pk=classroom_id)
        except Classroom.DoesNotExist:
            return None

    @staticmethod
    def create_classroom(data):
        try:
            school = School.objects.get(pk=data.pop("school"))
        except (School.DoesNotExist):
            return None
        return Classroom.objects.create(school=school,**data)

    @staticmethod
    def update_classroom(classroom, data):
        for key, value in data.items():
            setattr(classroom, key, value)
        classroom.save()
        return classroom

    @staticmethod
    def delete_classroom(classroom):
        classroom.delete()

class SchoolRepository:
    @staticmethod
    def get_all_schools():
        return School.objects.all()

    @staticmethod
    def get_school_by_id(school_id):
        try:
            return School.objects.get(pk=school_id)
        except School.DoesNotExist:
            return None

    @staticmethod
    def create_school(data):
        return School.objects.create(**data)

    @staticmethod
    def update_school(school, data):
        for key, value in data.items():
            setattr(school, key, value)
        school.save()
        return school

    @staticmethod
    def delete_school(school):
        school.delete()

