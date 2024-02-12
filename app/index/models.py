"""This module contains the models for the index page."""
import peewee

from app.db.database import MySQLDatabaseSingleton


database = MySQLDatabaseSingleton().database


class BaseModel(peewee.Model):
    """A base model class that all other models should inherit from.

    Attributes:
        database (Database): The database connection to use for this model.
    """

    class Meta:
        database = database


class Verb(BaseModel):
    """A model representing a verb.

    Attributes:
        num_id (int): The number ID of the verb.
        verb_type (str): The type of the verb (present, past, etc.).
        simple_form (str): The simple form of the verb.
        third_person (str): The third person form of the verb.
        simple_past (str): The simple past form of the verb.
        past_participle (str): The past participle form of the verb.
        gerund (str): The gerund form of the verb.
        meaning (str): The meaning of the verb.
    """

    num_id = peewee.PrimaryKeyField()
    verb_type = peewee.CharField()
    simple_form = peewee.CharField()
    third_person = peewee.CharField()
    simple_past = peewee.CharField()
    past_participle = peewee.CharField()
    gerund = peewee.CharField()
    meaning = peewee.CharField()

    class Meta:

        table_name = 'verbs'
