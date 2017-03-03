from ming import Field, schema
from ming.declarative import Document
from db import connection


class Learning(Document):

    class __mongometa__:
        session = connection.connection
        name = 'learnings'

    _id = Field(schema.ObjectId)
    skill = Field(schema.String)
    progress = Field(schema.String)
