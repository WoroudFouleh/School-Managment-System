from datetime import datetime
from typing import List, Optional

from core.repositories.student_repository import StudentRepository
from core.database import get_db_session
from core.serializers.student_serializer import StudentSchema


class StudentComponent:
    """
    Component layer for handling student-related business logic.
    """

    student_schema = StudentSchema()
    students_schema = StudentSchema(many=True)

    @staticmethod
    def get_all_students() -> List[dict]:
        """
        Retrieve all students.

        :return: A list of all students serialized as dictionaries.
        """
        session = get_db_session()
        students = StudentRepository.get_all_students(session)
        return StudentComponent.students_schema.dump(students)

    @staticmethod
    def get_student_by_id(student_id: int) -> Optional[dict]:
        """
        Retrieve a student by their ID.

        :param student_id: The ID of the student to retrieve.
        :return: The student data as a dictionary if found, otherwise None.
        """
        session = get_db_session()
        student = StudentRepository.get_student_by_id(session, student_id)
        if not student:
            return None
        return StudentComponent.student_schema.dump(student)

    @staticmethod
    def create_student(first_name: str, last_name: str, date_of_birth: str, email: str, city: str,
                       ID_number: str, address: str, school_id: int, classroom_id: int) -> Optional[dict]:
        """
        Create a new student.

        :param first_name: First name of the student.
        :param last_name: Last name of the student.
        :param date_of_birth: Date of birth in "YYYY-MM-DD" format.
        :param email: Student's email address.
        :param city: Student's city of residence.
        :param ID_number: Student's unique identification number.
        :param address: Student's address.
        :param school_id: The ID of the school the student is enrolled in.
        :param classroom_id: The ID of the classroom the student belongs to.
        :return: The created student serialized as a dictionary if successful, otherwise None.
        """
        session = get_db_session()

        date_of_birth_parsed = datetime.strptime(date_of_birth, "%Y-%m-%d") if date_of_birth else None

        student = StudentRepository.create_student(session, first_name, last_name, date_of_birth_parsed,
                                                   email, city, ID_number, address, school_id, classroom_id)

        if not student:
            return None

        return StudentComponent.student_schema.dump(student)

    @staticmethod
    def update_student(student_id: int, first_name: str, last_name: str, date_of_birth: str, email: str,
                       city: str, ID_number: str, address: str, school_id: int, classroom_id: int) -> Optional[dict]:
        """
        Update an existing student's details.

        :param student_id: The ID of the student to update.
        :param first_name: Updated first name.
        :param last_name: Updated last name.
        :param date_of_birth: Updated date of birth in "YYYY-MM-DD" format.
        :param email: Updated email address.
        :param city: Updated city.
        :param ID_number: Updated identification number.
        :param address: Updated address.
        :param school_id: Updated school ID.
        :param classroom_id: Updated classroom ID.
        :return: The updated student serialized as a dictionary if successful, otherwise None.
        """
        session = get_db_session()

        date_of_birth_parsed = datetime.strptime(date_of_birth, "%Y-%m-%d") if date_of_birth else None

        updated_student = StudentRepository.update_student(session, student_id, first_name, last_name,
                                                           date_of_birth_parsed, email, city, ID_number,
                                                           address, school_id, classroom_id)

        if not updated_student:
            return None

        return StudentComponent.student_schema.dump(updated_student)

    @staticmethod
    def delete_student(student_id: int) -> bool:
        """
        Delete a student by their ID.

        :param student_id: The ID of the student to delete.
        :return: True if the student was successfully deleted, False otherwise.
        """
        session = get_db_session()
        return StudentRepository.delete_student(session, student_id)
