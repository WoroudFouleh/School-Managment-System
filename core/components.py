from .repositories import *
from .serializers import *
from .database import get_db_session

class StudentComponent:
    student_schema = StudentSchema()
    students_schema = StudentSchema(many=True)

    @staticmethod
    def get_all_students():
        session = get_db_session()
        students = StudentRepository.get_all_students(session)
        return StudentComponent.students_schema.dump(students)

    @staticmethod
    def get_student_by_id(student_id):
        session = get_db_session()
        student = StudentRepository.get_student_by_id(session,student_id)
        if not student:
            return None
        return StudentComponent.student_schema.dump(student)

    @staticmethod
    def create_student(data):
        session = get_db_session()
        student = StudentRepository.create_student(session,data)
        if not student:
            return None
        return StudentComponent.student_schema.dump(student)

    @staticmethod
    def update_student(student_id, data):
        session = get_db_session()
        student = StudentRepository.get_student_by_id(session, student_id)
        if not student:
            return None
        updated_student = StudentRepository.update_student(session, student_id, data)
        return StudentComponent.student_schema.dump(updated_student)

    @staticmethod
    def delete_student(student_id):
        session = get_db_session()
        student = StudentRepository.get_student_by_id(session, student_id)
        if not student:
            return False
        StudentRepository.delete_student(session, student_id)
        return True

class SchoolComponent:
    school_schema = SchoolSchema()
    schools_schema = SchoolSchema(many=True)

    @staticmethod
    def get_all_schools():
        session = get_db_session()
        schools = SchoolRepository.get_all_schools(session)
        return SchoolComponent.schools_schema.dump(schools)

    @staticmethod
    def get_school_by_id(school_id):
        session = get_db_session()
        school = SchoolRepository.get_school_by_id(session,school_id)
        if not school:
            return None
        return SchoolComponent.school_schema.dump(school)

    @staticmethod
    def create_school(data):
        session = get_db_session()
        school = SchoolRepository.create_school(session, data)
        if not school:
            return None
        return SchoolComponent.school_schema.dump(school)

    @staticmethod
    def update_school(school_id, data):
        session = get_db_session()
        school = SchoolRepository.get_school_by_id(session, school_id)
        if not school:
            return None
        updated_school = SchoolRepository.update_school(session, school_id, data)
        return SchoolComponent.school_schema.dump(updated_school)

    @staticmethod
    def delete_school(school_id):
        session = get_db_session()
        school = SchoolRepository.get_school_by_id(session, school_id)
        if not school:
            return False
        SchoolRepository.delete_school(session, school_id)
        return True

class ClassroomComponent:
    class_schema = ClassRoomSchema()
    classes_schema = ClassRoomSchema(many=True)

    @staticmethod
    def get_all_classrooms():
        session = get_db_session()
        classrooms = ClassroomRepository.get_all_classrooms(session)
        return ClassroomComponent.classes_schema.dump(classrooms)

    @staticmethod
    def get_classroom_by_id(class_id):
        session = get_db_session()
        classroom = ClassroomRepository.get_classroom_by_id(session, class_id)
        if not classroom:
            return None
        return ClassroomComponent.class_schema.dump(classroom)

    @staticmethod
    def create_classroom(data):
        session = get_db_session()
        classroom = ClassroomRepository.create_classroom(session, data)
        if not classroom:
            return None
        return ClassroomComponent.class_schema.dump(classroom)

    @staticmethod
    def update_classroom(class_id, data):
        session = get_db_session()
        classroom = ClassroomRepository.get_classroom_by_id(session, class_id)
        if not classroom:
            return None
        updated_classroom = ClassroomRepository.update_classroom(session, class_id, data)
        return ClassroomComponent.class_schema.dump(updated_classroom)

    @staticmethod
    def delete_classroom(class_id):
        session = get_db_session()
        classroom = ClassroomRepository.get_classroom_by_id(session, class_id)
        if not classroom:
            return False
        ClassroomRepository.delete_classroom(session, class_id)
        return True