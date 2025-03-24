from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from core.models.school_model import School


class SchoolSchema(SQLAlchemyAutoSchema):
    """
    Schema for serializing and deserializing School objects.
    """

    class Meta:
        model = School
        load_instance = True
        include_relationships = True
