import datetime
from sqlalchemy.orm import Session
from core.models.student_model import Student
from typing import List, Optional, Type


class StudentRepository:
    """
    Repository class for handling Student-related database operations.
    """

    @staticmethod
    def get_all_students(session: Session) -> list[Type[Student]]:
        """
        Retrieve all students.

        Args:
            session (Session): SQLAlchemy database session.

        Returns:
            List[Student]: A list of all students.
        """
        return session.query(Student).all()

    @staticmethod
    def get_student_by_id(session: Session, student_id: int) -> Optional[Student]:
        """
        Retrieve a student by their ID.

        Args:
            session (Session): SQLAlchemy database session.
            student_id (int): ID of the student.

        Returns:
            Optional[Student]: The student object if found, else None.
        """
        return session.query(Student).filter_by(id=student_id).one_or_none()

    @staticmethod
    def create_student(session: Session, first_name: str, last_name: str, date_of_birth: datetime.date,
                       email: str, city: str, ID_number: str, address: str, school_id: int, classroom_id: int) -> Student:
        """
        Create a new student.

        Args:
            session (Session): SQLAlchemy database session.
            first_name (str): First name of the student.
            last_name (str): Last name of the student.
            date_of_birth (datetime.date): Date of birth.
            email (str): Email address.
            city (str): City of residence.
            ID_number (str): Unique ID number of the student.
            address (str): Address of the student.
            school_id (int): Associated school ID.
            classroom_id (int): Associated classroom ID.

        Returns:
            Student: The newly created student object.
        """
        student = Student(
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            email=email,
            city=city,
            ID_number=ID_number,
            address=address,
            school_id=school_id,
            classroom_id=classroom_id
        )
        session.add(student)
        session.commit()
        return student

    @staticmethod
    def update_student(session: Session, student_id: int, first_name: str, last_name: str, date_of_birth: datetime.date,
                       email: str, city: str, ID_number: str, address: str, school_id: int, classroom_id: int) -> Optional[Student]:
        """
        Update an existing student.

        Args:
            session (Session): SQLAlchemy database session.
            student_id (int): ID of the student to update.
            first_name (str): Updated first name.
            last_name (str): Updated last name.
            date_of_birth (datetime.date): Updated date of birth.
            email (str): Updated email.
            city (str): Updated city.
            ID_number (str): Updated ID number.
            address (str): Updated address.
            school_id (int): Updated school ID.
            classroom_id (int): Updated classroom ID.

        Returns:
            Optional[Student]: The updated student object if successful, else None.
        """
        updated_rows = session.query(Student).filter_by(id=student_id).update({
            "first_name": first_name,
            "last_name": last_name,
            "date_of_birth": date_of_birth,
            "email": email,
            "city": city,
            "ID_number": ID_number,
            "address": address,
            "school_id": school_id,
            "classroom_id": classroom_id
        })
        session.commit()
        return session.query(Student).filter_by(id=student_id).one_or_none() if updated_rows else None

    @staticmethod
    def delete_student(session: Session, student_id: int) -> bool:
        """
        Delete a student by their ID.

        Args:
            session (Session): SQLAlchemy database session.
            student_id (int): ID of the student to delete.

        Returns:
            bool: True if deletion was successful, False otherwise.
        """
        deleted_rows = session.query(Student).filter_by(id=student_id).delete()
        session.commit()
        return deleted_rows > 0
