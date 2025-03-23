from sqlalchemy.orm import Session
from core.models.school_model import SchoolTypeEnum, GenderTypeEnum, School


class SchoolRepository:
    @staticmethod
    def get_all_schools(session: Session):
        return session.query(School).all()

    @staticmethod
    def get_school_by_id(session: Session, school_id: int):
        return session.query(School).filter_by(id=school_id).one()

    @staticmethod
    def create_school(session: Session, name: str, address: str, phone_number: str, manager_name: str,
                      type: SchoolTypeEnum, gender_type: GenderTypeEnum):
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
                      manager_name: str, type: SchoolTypeEnum, gender_type: GenderTypeEnum):
        updated_rows = session.query(School).filter_by(id=school_id).update({
            "name": name,
            "address": address,
            "phone_number": phone_number,
            "manager_name": manager_name,
            "type": type,
            "gender_type": gender_type
        })
        session.commit()
        return session.query(School).filter_by(id=school_id).one() if updated_rows else None

    @staticmethod
    def delete_school(session: Session, school_id: int):
        deleted_rows = session.query(School).filter_by(id=school_id).delete()
        session.commit()
        return deleted_rows > 0
