from ming import Field, schema
from ming.declarative import Document
from db import connection


class Blurb(Document):

    class __mongometa__:
        session = connection.connection
        name = 'blurbs'

    _id = Field(schema.ObjectId)
    user = Field(schema.String)
    blurb = Field(schema.String)
