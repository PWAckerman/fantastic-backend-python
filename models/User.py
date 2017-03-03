from ming import Field, schema
from ming.declarative import Document
from db import connection


class User(Document):

    class __mongometa__:
        session = connection.connection
        name = 'users'

    _id = Field(schema.ObjectId)
    title = Field(schema.String)
    text = Field(schema.String)
    name = Field(schema.String)
    projects = Field(schema.Array(schema.String))
    education = Field(schema.Array(schema.String))
    skills = Field(schema.Array(schema.String))
    learnings = Field(schema.Array(schema.String))
    commits = Field(schema.Int)
    stack = Field(schema.Object(fields={'score': schema.Int, 'badges': schema.Int }))
    githubname = Field(schema.String)
    stackurl = Field(schema.String)
    linkedinurl = Field(schema.String)
    githuburl = Field(schema.String)
    email = Field(schema.String)
    avatar = Field(schema.String)
