from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from core.models.classroom_model import Classroom


class ClassRoomSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Classroom
        load_instance = True
        include_fk = True
        include_relationships = True