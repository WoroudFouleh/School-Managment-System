from sqlalchemy import Column, Integer, String, ForeignKey, Enum, DateTime
from sqlalchemy.orm import relationship
from core.base import Base
from datetime import datetime
from core.models.school_model import School
from core.models.classroom_model import Classroom

class Student(Base):
    """
    Represents a student entity.

    Attributes:
        id (int): Unique identifier for the student.
        first_name (str): First name of the student.
        last_name (str): Last name of the student.
        date_of_birth (datetime | None): Date of birth of the student (optional).
        email (str): Unique email of the student.
        city (str): City where the student resides.
        ID_number (str): Unique identification number for the student.
        address (str): Address of the student.
        school_id (int): Foreign key linking to the 'schools' table.
        classroom_id (int): Foreign key linking to the 'classrooms' table.
        school (relationship): Relationship to the School model.
        classroom (relationship): Relationship to the Classroom model.
    """

    __tablename__ = 'students'

    id: int = Column(Integer, primary_key=True)
    first_name: str = Column(String(255), nullable=False)
    last_name: str = Column(String(255), nullable=False)
    date_of_birth: datetime | None = Column(DateTime, nullable=True)
    email: str = Column(String(255), nullable=False, unique=True)
    city: str = Column(String(255), nullable=False)
    ID_number: str = Column(String(255), nullable=False, unique=True)
    address: str = Column(String(255), nullable=False)

    # Foreign keys
    school_id: int = Column(Integer, ForeignKey('schools.id'))
    classroom_id: int = Column(Integer, ForeignKey('classrooms.id'))

    # Relationships
    school = relationship("School", back_populates="students")
    classroom = relationship('Classroom', back_populates='students')
