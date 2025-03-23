from datetime import datetime

from core.repositories.student_repository import StudentRepository
from core.database import get_db_session
from core.serializers.student_serializer import StudentSchema


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
    def create_student(first_name: str, last_name: str, date_of_birth: str, email: str, city: str,
                       ID_number: str, address: str, school_id: int, classroom_id: int):
        session = get_db_session()

        date_of_birth = datetime.strptime(date_of_birth, "%Y-%m-%d") if date_of_birth else None

        student = StudentRepository.create_student(session, first_name, last_name, date_of_birth,
                                                   email, city, ID_number, address, school_id, classroom_id)

        if not student:
            return None

        return StudentComponent.student_schema.dump(student)

    @staticmethod
    def update_student(student_id: int, first_name: str, last_name: str, date_of_birth: str, email: str,
                       city: str, ID_number: str, address: str, school_id: int, classroom_id: int):
        session = get_db_session()

        date_of_birth = datetime.strptime(date_of_birth, "%Y-%m-%d") if date_of_birth else None

        updated_student = StudentRepository.update_student(session, student_id, first_name, last_name, date_of_birth,
                                                           email, city, ID_number, address, school_id, classroom_id)

        if not updated_student:
            return None

        return StudentComponent.student_schema.dump(updated_student)

    @staticmethod
    def delete_student(student_id: int):
        session = get_db_session()
        return StudentRepository.delete_student(session, student_id)
