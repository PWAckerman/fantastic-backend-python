from ming import Field, schema
from ming.declarative import Document
from db import connection


class Platform(Document):

    class __mongometa__:
        session = connection.connection
        name = 'platforms'

    _id = Field(schema.ObjectId)
    title = Field(schema.String)
    text = Field(schema.String)
