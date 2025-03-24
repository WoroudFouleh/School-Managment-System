from typing import List, Optional
from core.models.school_model import SchoolTypeEnum, GenderTypeEnum
from core.repositories.school_repository import SchoolRepository
from core.database import get_db_session
from core.serializers.school_serializer import SchoolSchema


class SchoolComponent:
    """
    Component layer for handling school-related business logic.
    """

    school_schema = SchoolSchema()
    schools_schema = SchoolSchema(many=True)

    @staticmethod
    def get_all_schools() -> List[dict]:
        """
        Retrieve all schools.

        :return: A list of all schools serialized as dictionaries.
        """
        session = get_db_session()
        schools = SchoolRepository.get_all_schools(session)
        return SchoolComponent.schools_schema.dump(schools)

    @staticmethod
    def get_school_by_id(school_id: int) -> Optional[dict]:
        """
        Retrieve a school by its ID.

        :param school_id: The ID of the school to retrieve.
        :return: The school data as a dictionary if found, otherwise None.
        """
        session = get_db_session()
        school = SchoolRepository.get_school_by_id(session, school_id)
        if not school:
            return None
        return SchoolComponent.school_schema.dump(school)

    @staticmethod
    def create_school(name: str, address: str, phone_number: str, manager_name: str,
                      type: str, gender_type: str) -> Optional[dict]:
        """
        Create a new school.

        :param name: Name of the school.
        :param address: Address of the school.
        :param phone_number: Contact phone number.
        :param manager_name: Name of the school manager.
        :param type: Type of the school (must match `SchoolTypeEnum`).
        :param gender_type: Gender type of the school (must match `GenderTypeEnum`).
        :return: The created school serialized as a dictionary if successful, otherwise None.
        """
        session = get_db_session()

        school_type = SchoolTypeEnum[type.upper()]
        gender = GenderTypeEnum[gender_type.upper()]

        school = SchoolRepository.create_school(session, name, address, phone_number, manager_name, school_type, gender)

        if not school:
            return None

        return SchoolComponent.school_schema.dump(school)

    @staticmethod
    def update_school(school_id: int, name: str, address: str, phone_number: str,
                      manager_name: str, type: SchoolTypeEnum, gender_type: GenderTypeEnum) -> Optional[dict]:
        """
        Update an existing school's details.

        :param school_id: The ID of the school to update.
        :param name: Updated name of the school.
        :param address: Updated address of the school.
        :param phone_number: Updated contact phone number.
        :param manager_name: Updated name of the school manager.
        :param type: Updated school type (`SchoolTypeEnum`).
        :param gender_type: Updated gender type (`GenderTypeEnum`).
        :return: The updated school serialized as a dictionary if successful, otherwise None.
        """
        session = get_db_session()

        updated_school = SchoolRepository.update_school(session, school_id, name, address, phone_number,
                                                        manager_name, type, gender_type)

        if not updated_school:
            return None

        return SchoolComponent.school_schema.dump(updated_school)

    @staticmethod
    def delete_school(school_id: int) -> bool:
        """
        Delete a school by its ID.

        :param school_id: The ID of the school to delete.
        :return: True if the school was successfully deleted, False otherwise.
        """
        session = get_db_session()
        return SchoolRepository.delete_school(session, school_id)
