import datetime
from sqlalchemy.orm import Session
from core.models.student_model import Student

class StudentRepository:
    @staticmethod
    def get_all_students(session: Session):
        return session.query(Student).all()

    @staticmethod
    def get_student_by_id(session: Session, student_id: int):
        return session.query(Student).filter_by(id=student_id).one()

    @staticmethod
    def create_student(session: Session, first_name: str, last_name: str, date_of_birth: datetime,
                       email: str, city: str, ID_number: str, address: str, school_id: int, classroom_id: int):
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
    def update_student(session: Session, student_id: int, first_name: str, last_name: str, date_of_birth: datetime,
                       email: str, city: str, ID_number: str, address: str, school_id: int, classroom_id: int):
        student = session.query(Student).filter_by(id=student_id).update({
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
        return session.query(Student).filter_by(id=student_id).one()

    @staticmethod
    def delete_student(session: Session, student_id: int):
        deleted_rows = session.query(Student).filter_by(id=student_id).delete()
        session.commit()
        return deleted_rows > 0
