from django.db import models
import enum
from sqlalchemy import Column, Integer, String, ForeignKey, Enum, DateTime
from sqlalchemy.orm import relationship
from core.base import Base
from core.database import engine

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