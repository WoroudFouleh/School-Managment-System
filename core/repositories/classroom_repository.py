from sqlalchemy.orm import Session
from core.models.classroom_model import  Classroom

class ClassroomRepository:
    @staticmethod
    def get_all_classrooms(session: Session):
        return session.query(Classroom).all()

    @staticmethod
    def get_classroom_by_id(session: Session, classroom_id: int):
        return session.query(Classroom).filter_by(id=classroom_id).one()

    @staticmethod
    def create_classroom(session: Session, name: str, section: str, num_chairs: int, school_id: int):
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
    def update_classroom(session: Session, classroom_id: int, name: str, section: str, num_chairs: int, school_id: int):
        updated_rows = session.query(Classroom).filter_by(id=classroom_id).update({
            "name": name,
            "section": section,
            "num_chairs": num_chairs,
            "school_id": school_id
        })
        session.commit()
        return session.query(Classroom).filter_by(id=classroom_id).one() if updated_rows else None

    @staticmethod
    def delete_classroom(session: Session, classroom_id: int):
        deleted_rows = session.query(Classroom).filter_by(id=classroom_id).delete()
        session.commit()
        return deleted_rows > 0

