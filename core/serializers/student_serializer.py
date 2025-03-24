from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from core.models.student_model import Student


class StudentSchema(SQLAlchemyAutoSchema):
    """
    Schema for serializing and deserializing Student objects.
    """

    class Meta:
        model = Student
        load_instance = True
        include_fk = True
