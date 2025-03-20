
from django.db import models
import enum
from sqlalchemy import Column, Integer, String, ForeignKey, Enum, DateTime
from sqlalchemy.orm import relationship
from .base import Base
from .database import engine

class SchoolTypeEnum(enum.Enum):
    PRIMARY = "primary"
    SECONDARY = "secondary"
    HIGH_SCHOOL = "high_school"

class GenderTypeEnum(enum.Enum):
    BOYS = "boys"
    GIRLS = "girls"
    MIXED = "mixed"

class School(Base):
    __tablename__ = 'schools'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    address = Column(String(255), nullable=False)
    phone_number = Column(String(255), nullable=False)
    manager_name = Column(String(255), nullable=False)

    type = Column(Enum(SchoolTypeEnum), default=SchoolTypeEnum.PRIMARY, nullable=False)
    gender_type = Column(Enum(GenderTypeEnum), default=GenderTypeEnum.BOYS, nullable=False)

    classrooms = relationship("Classroom", back_populates="school")
    students = relationship("Student", back_populates="school")

class Classroom(Base):
    __tablename__ = 'classrooms'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    section = Column(String(255), nullable=False)
    num_chairs = Column(Integer)
    school_id = Column(Integer, ForeignKey('schools.id'))
    school = relationship('School', back_populates='classrooms')
    students = relationship('Student', back_populates='classrooms')

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






