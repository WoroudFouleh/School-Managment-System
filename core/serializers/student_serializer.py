from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from core.models.student_model import Student


class StudentSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Student
        load_instance = True
        include_fk = True
