from peewee import *

db = SqliteDatabase('people.db')
class BaseModel(Model):
    class Meta:
        database = db # This model uses the "people.db" database.

class Person(BaseModel):
    name = CharField()
    birthday = DateField()
    is_relative = BooleanField()