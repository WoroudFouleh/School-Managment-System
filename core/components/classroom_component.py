from core.repositories import *
from core.repositories.classroom_repository import ClassroomRepository
from core.serializers import *
from core.database import get_db_session
from core.serializers.classroom_serializer import ClassRoomSchema


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
    def create_classroom(name: str, section: str, num_chairs: int, school_id: int):
        session = get_db_session()
        classroom = ClassroomRepository.create_classroom(session, name, section, num_chairs, school_id)
        if not classroom:
            return None
        return ClassroomComponent.class_schema.dump(classroom)

    @staticmethod
    def update_classroom(classroom_id: int, name: str, section: str, num_chairs: int, school_id: int):
        session = get_db_session()

        updated_classroom = ClassroomRepository.update_classroom(session, classroom_id, name, section, num_chairs,
                                                                 school_id)

        if not updated_classroom:
            return None

        return ClassroomComponent.classes_schema.dump(updated_classroom)

    @staticmethod
    def delete_classroom(classroom_id: int):
        session = get_db_session()
        return ClassroomRepository.delete_classroom(session, classroom_id)
