from sqlalchemy.orm import Session
from core.models.school_model import SchoolTypeEnum, GenderTypeEnum, School
from typing import List, Optional, Type


class SchoolRepository:
    """
    Repository class for handling School-related database operations.
    """

    @staticmethod
    def get_all_schools(session: Session) -> list[Type[School]]:
        """
        Retrieve all schools.

        Args:
            session (Session): SQLAlchemy database session.

        Returns:
            List[School]: A list of all schools.
        """
        return session.query(School).all()

    @staticmethod
    def get_school_by_id(session: Session, school_id: int) -> Optional[School]:
        """
        Retrieve a school by its ID.

        Args:
            session (Session): SQLAlchemy database session.
            school_id (int): ID of the school.

        Returns:
            Optional[School]: The school object if found, else None.
        """
        return session.query(School).filter_by(id=school_id).one_or_none()

    @staticmethod
    def create_school(session: Session, name: str, address: str, phone_number: str, manager_name: str,
                      type: SchoolTypeEnum, gender_type: GenderTypeEnum) -> School:
        """
        Create a new school.

        Args:
            session (Session): SQLAlchemy database session.
            name (str): Name of the school.
            address (str): Address of the school.
            phone_number (str): Phone number of the school.
            manager_name (str): Name of the school manager.
            type (SchoolTypeEnum): Type of school (Primary, Secondary, High School).
            gender_type (GenderTypeEnum): Gender type of the school (Boys, Girls, Mixed).

        Returns:
            School: The newly created school object.
        """
        school = School(
            name=name,
            address=address,
            phone_number=phone_number,
            manager_name=manager_name,
            type=type,
            gender_type=gender_type
        )
        session.add(school)
        session.commit()
        return school

    @staticmethod
    def update_school(session: Session, school_id: int, name: str, address: str, phone_number: str,
                      manager_name: str, type: SchoolTypeEnum, gender_type: GenderTypeEnum) -> Optional[School]:
        """
        Update an existing school.

        Args:
            session (Session): SQLAlchemy database session.
            school_id (int): ID of the school to update.
            name (str): New name of the school.
            address (str): Updated address of the school.
            phone_number (str): Updated phone number.
            manager_name (str): Updated manager name.
            type (SchoolTypeEnum): Updated type of school.
            gender_type (GenderTypeEnum): Updated gender type.

        Returns:
            Optional[School]: The updated school object if successful, else None.
        """
        updated_rows = session.query(School).filter_by(id=school_id).update({
            "name": name,
            "address": address,
            "phone_number": phone_number,
            "manager_name": manager_name,
            "type": type,
            "gender_type": gender_type
        })
        session.commit()
        return session.query(School).filter_by(id=school_id).one_or_none() if updated_rows else None

    @staticmethod
    def delete_school(session: Session, school_id: int) -> bool:
        """
        Delete a school by its ID.

        Args:
            session (Session): SQLAlchemy database session.
            school_id (int): ID of the school to delete.

        Returns:
            bool: True if deletion was successful, False otherwise.
        """
        deleted_rows = session.query(School).filter_by(id=school_id).delete()
        session.commit()
        return deleted_rows > 0
