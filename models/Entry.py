from ming import Field, schema
from ming.declarative import Document
from datetime import datetime
from db import connection


class Entry(Document):

    class __mongometa__:
        session = connection.connection
        name = 'entries'

    _id = Field(schema.ObjectId)
    user = Field(schema.String)
    date = Field(datetime, if_missing=datetime.utcnow)
    text = Field(schema.String)
