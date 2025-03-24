from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from core.base import Base
from core.models.school_model import School


class Classroom(Base):
    """
    Represents a classroom within a school.

    Attributes:
        id (int): Primary key for the classroom.
        name (str): The name of the classroom.
        section (str): The section the classroom belongs to.
        num_chairs (int, optional): Number of chairs in the classroom.
        school_id (int): Foreign key referencing the associated school.
        school (relationship): Relationship to the School model.
        students (relationship): Relationship to the Student model.
    """

    __tablename__ = 'classrooms'

    id: int = Column(Integer, primary_key=True)
    name: str = Column(String(255), nullable=False)
    section: str = Column(String(255), nullable=False)
    num_chairs: int = Column(Integer)
    school_id: int = Column(Integer, ForeignKey('schools.id'))

    # Relationships
    school = relationship('School', back_populates='classrooms')
    students = relationship('Student', back_populates='classroom')

