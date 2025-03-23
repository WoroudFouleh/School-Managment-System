from core.models.school_model import SchoolTypeEnum, GenderTypeEnum
from core.repositories import *
from core.repositories.school_repository import SchoolRepository
from core.serializers import *
from core.database import get_db_session
from core.serializers.school_serializer import SchoolSchema


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
    def create_school(name: str, address: str, phone_number: str, manager_name: str,
                      type: str, gender_type: str):
        session = get_db_session()

        school_type = SchoolTypeEnum[type.upper()]
        gender = GenderTypeEnum[gender_type.upper()]

        school = SchoolRepository.create_school(session, name, address, phone_number, manager_name, school_type, gender)

        if not school:
            return None

        return SchoolComponent.school_schema.dump(school)

    @staticmethod
    def update_school(school_id: int, name: str, address: str, phone_number: str,
                      manager_name: str, type: SchoolTypeEnum, gender_type: GenderTypeEnum):
        session = get_db_session()

        updated_school = SchoolRepository.update_school(session, school_id, name, address, phone_number,
                                                        manager_name, type, gender_type)

        if not updated_school:
            return None

        return SchoolComponent.school_schema.dump(updated_school)

    @staticmethod
    def delete_school(school_id: int):
        session = get_db_session()
        return SchoolRepository.delete_school(session, school_id)
