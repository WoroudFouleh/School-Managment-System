from .repositories import *
from .serializers import *

class StudentComponent:
    @staticmethod
    def get_all_students():
        students = StudentRepository.get_all_students()
        return StudentSerializer(students, many=True).data

    @staticmethod
    def get_student_by_id(student_id):
        student = StudentRepository.get_student_by_id(student_id)
        if not student:
            return None
        return StudentSerializer(student).data

    @staticmethod
    def create_student(data):
        student = StudentRepository.create_student(data)
        return StudentSerializer(student).data

    @staticmethod
    def update_student(student_id, data):
        student = StudentRepository.get_student_by_id(student_id)
        if not student:
            return None
        updated_student = StudentRepository.update_student(student, data)
        return StudentSerializer(updated_student).data

    @staticmethod
    def delete_student(student_id):
        student = StudentRepository.get_student_by_id(student_id)
        if not student:
            return False
        StudentRepository.delete_student(student)
        return True

class ClassroomComponent:
    @staticmethod
    def get_all_classrooms():
        classrooms = ClassroomRepository.get_all_classrooms()
        return ClassroomSerializer(classrooms, many=True).data

    @staticmethod
    def get_classroom_by_id(classroom_id):
        classroom = ClassroomRepository.get_classroom_by_id(classroom_id)
        if not classroom:
            return None
        return ClassroomSerializer(classroom).data

    @staticmethod
    def create_classroom(data):
        classroom = ClassroomRepository.create_classroom(data)
        return ClassroomSerializer(classroom).data

    @staticmethod
    def update_classroom(classroom_id, data):
        classroom = ClassroomRepository.get_classroom_by_id(classroom_id)
        if not classroom:
            return None
        updated_classroom = ClassroomRepository.update_classroom(classroom, data)
        return ClassroomSerializer(updated_classroom).data

    @staticmethod
    def delete_classroom(classroom_id):
        classroom = ClassroomRepository.get_classroom_by_id(classroom_id)
        if not classroom:
            return False
        ClassroomRepository.delete_classroom(classroom)
        return True

class SchoolComponent:
    @staticmethod
    def get_all_schools():
        schools = SchoolRepository.get_all_schools()
        return SchoolSerializer(schools, many=True).data

    @staticmethod
    def get_school_by_id(school_id):
        school = SchoolRepository.get_school_by_id()(school_id)
        if not school:
            return None
        return SchoolSerializer(school).data

    @staticmethod
    def create_school(data):
        school = SchoolRepository.create_school(data)
        return SchoolSerializer(school).data

    @staticmethod
    def update_school(school_id, data):
        school = SchoolRepository.get_school_by_id(school_id)
        if not school:
            return None
        updated_school = SchoolRepository.update_school(school, data)
        return SchoolSerializer(updated_school).data

    @staticmethod
    def delete_school(school_id):
        school = SchoolRepository.get_school_by_id(school_id)
        if not school:
            return False
        SchoolRepository.delete_school(school)
        return True