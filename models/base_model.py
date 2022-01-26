#!/usr/bin/python3
import uuid
import datetime


class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime

    def __str__(self):
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"
