from ming import Field, schema
from ming.declarative import Document
from db import connection


class Project(Document):

    class __mongometa__:
        session = connection.connection
        name = 'projects'

    _id = Field(schema.ObjectId)
    title = Field(schema.String)
    platforms = Field(schema.Array(schema.String))
    description = Field(schema.String)
    screenshot = Field(schema.String)
    technologies = Field(schema.Array(schema.String))
