from typing import List, Optional
from core.repositories.classroom_repository import ClassroomRepository
from core.database import get_db_session
from core.serializers.classroom_serializer import ClassRoomSchema


class ClassroomComponent:
    """
    Component layer for handling classroom-related business logic.
    """

    class_schema = ClassRoomSchema()
    classes_schema = ClassRoomSchema(many=True)

    @staticmethod
    def get_all_classrooms() -> List[dict]:
        """
        Retrieve all classrooms.

        :return: A list of all classrooms serialized as dictionaries.
        """
        session = get_db_session()
        classrooms = ClassroomRepository.get_all_classrooms(session)
        return ClassroomComponent.classes_schema.dump(classrooms)

    @staticmethod
    def get_classroom_by_id(class_id: int) -> Optional[dict]:
        """
        Retrieve a classroom by its ID.

        :param class_id: The ID of the classroom to retrieve.
        :return: The classroom data as a dictionary if found, otherwise None.
        """
        session = get_db_session()
        classroom = ClassroomRepository.get_classroom_by_id(session, class_id)
        if not classroom:
            return None
        return ClassroomComponent.class_schema.dump(classroom)

    @staticmethod
    def create_classroom(name: str, section: str, num_chairs: int, school_id: int) -> Optional[dict]:
        """
        Create a new classroom.

        :param name: Name of the classroom.
        :param section: Section identifier.
        :param num_chairs: Number of chairs available in the classroom.
        :param school_id: The associated school ID.
        :return: The created classroom serialized as a dictionary if successful, otherwise None.
        """
        session = get_db_session()
        classroom = ClassroomRepository.create_classroom(session, name, section, num_chairs, school_id)
        if not classroom:
            return None
        return ClassroomComponent.class_schema.dump(classroom)

    @staticmethod
    def update_classroom(classroom_id: int, name: str, section: str, num_chairs: int, school_id: int) -> Optional[dict]:
        """
        Update an existing classroom's details.

        :param classroom_id: The ID of the classroom to update.
        :param name: Updated name of the classroom.
        :param section: Updated section identifier.
        :param num_chairs: Updated number of chairs.
        :param school_id: Updated associated school ID.
        :return: The updated classroom serialized as a dictionary if successful, otherwise None.
        """
        session = get_db_session()
        updated_classroom = ClassroomRepository.update_classroom(session, classroom_id, name, section, num_chairs, school_id)
        if not updated_classroom:
            return None
        return ClassroomComponent.class_schema.dump(updated_classroom)

    @staticmethod
    def delete_classroom(classroom_id: int) -> bool:
        """
        Delete a classroom by its ID.

        :param classroom_id: The ID of the classroom to delete.
        :return: True if the classroom was successfully deleted, False otherwise.
        """
        session = get_db_session()
        return ClassroomRepository.delete_classroom(session, classroom_id)
