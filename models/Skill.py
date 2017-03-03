from ming import Field, schema
from ming.declarative import Document
from db import connection


class Skill(Document):

    class __mongometa__:
        session = connection.connection
        name = 'skills'

    _id = Field(schema.ObjectId)
    name = Field(schema.String)
    icon = Field(schema.String)
    type = Field(schema.String)
