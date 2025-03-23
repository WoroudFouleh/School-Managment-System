
from sqlalchemy import Column, Integer, String, ForeignKey, Enum, DateTime
from sqlalchemy.orm import relationship
from core.base import Base

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    date_of_birth = Column(DateTime)
    email = Column(String(255), nullable=False, unique=True)
    city = Column(String(255), nullable=False)
    ID_number = Column(String(255),nullable=False, unique=True)
    address = Column(String(255), nullable=False)
    school_id = Column(Integer, ForeignKey('schools.id'))
    classroom_id = Column(Integer, ForeignKey('classrooms.id'))
    school = relationship('School', back_populates='students')
    classrooms = relationship('Classroom', back_populates='students')
