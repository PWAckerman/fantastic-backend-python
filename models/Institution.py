from ming import Field, schema
from ming.declarative import Document
from db import connection


class Institution(Document):

    class __mongometa__:
        session = connection.connection
        name = 'institutions'

    _id = Field(schema.ObjectId)
    name = Field(schema.String)
    image = Field(schema.String)
    location = Field(schema.String)
    type = Field(schema.String)
