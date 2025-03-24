from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from core.models.classroom_model import Classroom
from marshmallow_sqlalchemy.fields import Nested
from marshmallow import fields


class ClassRoomSchema(SQLAlchemyAutoSchema):
    """
    Schema for serializing and deserializing Classroom objects.
    """

    school_id = fields.Integer(required=True)

    class Meta:
        model = Classroom
        load_instance = True
        include_fk = True
        include_relationships = True

    school = Nested("SchoolSchema", only=("id", "name"), dump_only=True)
