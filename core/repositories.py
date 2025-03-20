from sqlalchemy.orm import Session
from .models import School, Classroom, Student

class StudentRepository:
    @staticmethod
    def get_all_students(session: Session):
        return session.query(Student).all()

    @staticmethod
    def get_student_by_id(session: Session, student_id: int):
        return session.query(Student).filter_by(id=student_id).first()

    @staticmethod
    def create_student(session: Session, data: dict):
        student = Student(**data)
        session.add(student)
        session.commit()
        return student

    @staticmethod
    def update_student(session: Session, student_id: int, data: dict):
        student = session.query(Student).filter_by(id=student_id).first()
        if not student:
            return None
        for key, value in data.items():
            setattr(student, key, value)
        session.commit()
        return student

    @staticmethod
    def delete_student(session: Session, student_id: int):
        student = session.query(Student).filter_by(id=student_id).first()
        if student:
            session.delete(student)
            session.commit()
            return True
        return False

class ClassroomRepository:
    @staticmethod
    def get_all_classrooms(session: Session):
        return session.query(Classroom).all()

    @staticmethod
    def get_classroom_by_id(session: Session, classroom_id: int):
        return session.query(Classroom).filter_by(id=classroom_id).first()

    @staticmethod
    def create_classroom(session: Session, data: dict):
        classroom = Classroom(**data)
        session.add(classroom)
        session.commit()
        return classroom

    @staticmethod
    def update_classroom(session: Session, classroom_id: int, data: dict):
        classroom = session.query(Classroom).filter_by(id=classroom_id).first()
        if not classroom:
            return None
        for key, value in data.items():
            setattr(classroom, key, value)
            session.commit()
            return classroom

    @staticmethod
    def delete_classroom(session: Session, classroom_id: int):
        classroom = session.query(Classroom).filter_by(id=classroom_id).first()
        if classroom:
            session.delete(classroom)
            session.commit()
            return True
        return False

class SchoolRepository:
    @staticmethod
    def get_all_schools(session: Session):
        return session.query(School).all()

    @staticmethod
    def get_school_by_id(session: Session, school_id: int):
        return session.query(School).filter_by(id=school_id).first()

    @staticmethod
    def create_school(session: Session, data: dict):
        school = School(**data)
        session.add(school)
        session.commit()
        return school

    @staticmethod
    def update_school(session: Session, school_id: int, data: dict):
        school = session.query(School).filter_by(id=school_id).first()
        if not school:
            return None
        for key, value in data.items():
            setattr(school, key, value)
            session.commit()
            return school

    @staticmethod
    def delete_school(session: Session, school_id: int):
        school = session.query(School).filter_by(id=school_id).first()
        if school:
            session.delete(school)
            session.commit()
            return True
        return False
