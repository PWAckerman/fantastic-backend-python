from ming import Field, schema
from ming.declarative import Document
from datetime import datetime
from db import connection


class Email(Document):

    class __mongometa__:
        session = connection.connection
        name = 'emails'

    _id = Field(schema.ObjectId)
    fromw = Field(schema.String)
    date = Field(datetime, if_missing=datetime.utcnow)
    subject = Field(schema.String)
    text = Field(schema.String)
    user = Field(schema.String)
    to = Field(schema.String)
