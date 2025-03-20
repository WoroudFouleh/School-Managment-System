from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from .models import *

class StudentSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Student
        load_instance = True
        include_fk = True

class SchoolSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = School
        load_instance = True
        include_relationships = True

class ClassRoomSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Classroom
        load_instance = True
        include_fk = True
        include_relationships = True