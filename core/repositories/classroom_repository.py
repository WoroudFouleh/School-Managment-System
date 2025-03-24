from sqlalchemy.orm import Session
from core.models.classroom_model import Classroom
from typing import List, Optional, Type


class ClassroomRepository:
    """
    Repository class for handling Classroom-related database operations.
    """

    @staticmethod
    def get_all_classrooms(session: Session) -> list[Type[Classroom]]:
        """
        Retrieve all classrooms.

        Args:
            session (Session): SQLAlchemy database session.

        Returns:
            List[Classroom]: A list of all classrooms.
        """
        return session.query(Classroom).all()

    @staticmethod
    def get_classroom_by_id(session: Session, classroom_id: int) -> Optional[Classroom]:
        """
        Retrieve a classroom by its ID.

        Args:
            session (Session): SQLAlchemy database session.
            classroom_id (int): ID of the classroom.

        Returns:
            Optional[Classroom]: The classroom object if found, else None.
        """
        return session.query(Classroom).filter_by(id=classroom_id).one_or_none()

    @staticmethod
    def create_classroom(session: Session, name: str, section: str, num_chairs: int, school_id: int) -> Classroom:
        """
        Create a new classroom.

        Args:
            session (Session): SQLAlchemy database session.
            name (str): Name of the classroom.
            section (str): Section of the classroom.
            num_chairs (int): Number of chairs in the classroom.
            school_id (int): ID of the school associated with the classroom.

        Returns:
            Classroom: The newly created classroom object.
        """
        classroom = Classroom(
            name=name,
            section=section,
            num_chairs=num_chairs,
            school_id=school_id
        )
        session.add(classroom)
        session.commit()
        return classroom

    @staticmethod
    def update_classroom(session: Session, classroom_id: int, name: str, section: str, num_chairs: int, school_id: int) -> Optional[Classroom]:
        """
        Update an existing classroom.

        Args:
            session (Session): SQLAlchemy database session.
            classroom_id (int): ID of the classroom to update.
            name (str): New name of the classroom.
            section (str): New section of the classroom.
            num_chairs (int): Updated number of chairs in the classroom.
            school_id (int): Updated school ID associated with the classroom.

        Returns:
            Optional[Classroom]: The updated classroom object if successful, else None.
        """
        updated_rows = session.query(Classroom).filter_by(id=classroom_id).update({
            "name": name,
            "section": section,
            "num_chairs": num_chairs,
            "school_id": school_id
        })
        session.commit()
        return session.query(Classroom).filter_by(id=classroom_id).one_or_none() if updated_rows else None

    @staticmethod
    def delete_classroom(session: Session, classroom_id: int) -> bool:
        """
        Delete a classroom by its ID.

        Args:
            session (Session): SQLAlchemy database session.
            classroom_id (int): ID of the classroom to delete.

        Returns:
            bool: True if deletion was successful, False otherwise.
        """
        deleted_rows = session.query(Classroom).filter_by(id=classroom_id).delete()
        session.commit()
        return deleted_rows > 0
