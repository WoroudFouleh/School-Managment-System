from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
from core.base import Base
import enum


class SchoolTypeEnum(enum.Enum):
    """Enumeration for different types of schools."""
    PRIMARY = "primary"
    SECONDARY = "secondary"
    HIGH_SCHOOL = "high_school"


class GenderTypeEnum(enum.Enum):
    """Enumeration for gender-based school types."""
    BOYS = "boys"
    GIRLS = "girls"
    MIXED = "mixed"


class School(Base):
    """
    Represents a school entity.

    Attributes:
        id (int): Unique identifier for the school.
        name (str): Name of the school.
        address (str): Address of the school.
        phone_number (str): Contact phone number of the school.
        manager_name (str): Name of the school manager.
        type (SchoolTypeEnum): Type of the school (Primary, Secondary, High School).
        gender_type (GenderTypeEnum): Gender classification of the school (Boys, Girls, Mixed).
        classrooms (relationship): Relationship to the Classroom model.
        students (relationship): Relationship to the Student model.
    """

    __tablename__ = 'schools'

    id: int = Column(Integer, primary_key=True)
    name: str = Column(String(255), nullable=False)
    address: str = Column(String(255), nullable=False)
    phone_number: str = Column(String(255), nullable=False)
    manager_name: str = Column(String(255), nullable=False)

    type: SchoolTypeEnum = Column(Enum(SchoolTypeEnum), default=SchoolTypeEnum.PRIMARY, nullable=False)
    gender_type: GenderTypeEnum = Column(Enum(GenderTypeEnum), default=GenderTypeEnum.BOYS, nullable=False)

    # Relationships
    classrooms = relationship("Classroom", back_populates="school")
    # Use a string instead of direct reference
    students = relationship("Student", back_populates="school")