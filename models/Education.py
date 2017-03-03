from ming import Field, schema
from ming.declarative import Document
from db import connection


class Education(Document):

    class __mongometa__:
        session = connection.connection
        name = 'educations'

    _id = Field(schema.ObjectId)
    attended = Field(schema.String)
    institution = Field(schema.String)
    description = Field(schema.String)
    degree = Field(schema.String)
