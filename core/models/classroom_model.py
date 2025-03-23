from sqlalchemy import Column, Integer, String, ForeignKey, Enum, DateTime
from sqlalchemy.orm import relationship
from core.base import Base

class Classroom(Base):
    __tablename__ = 'classrooms'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    section = Column(String(255), nullable=False)
    num_chairs = Column(Integer)
    school_id = Column(Integer, ForeignKey('schools.id'))
    school = relationship('School', back_populates='classrooms')
    students = relationship('Student', back_populates='classrooms')