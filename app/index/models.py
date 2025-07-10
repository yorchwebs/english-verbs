"""This module contains the models for the index page."""

import peewee

from app.db.database import DatabaseSingleton

database = DatabaseSingleton().database


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

    NUM = peewee.PrimaryKeyField()
    TYPE = peewee.CharField()
    SIMPLE_FORM = peewee.CharField()
    THIRD_PERSON = peewee.CharField()
    SIMPLE_PAST = peewee.CharField()
    PAST_PARTICIPLE = peewee.CharField()
    GERUND = peewee.CharField()
    MEANING = peewee.CharField()

    class Meta:
        table_name = "verbs"


# class AudioVerb(BaseModel):
#     """A model representing an audio verb.

#     Attributes:
#         simple_form (str): The simple form of the verb.
#         third_person (str): The third person form of the verb.
#         simple_past (str): The simple past form of the verb.
#         past_participle (str): The past participle form of the verb.
#         gerund (str): The gerund form of the verb.
#     """

#     SIMPLE_FORM = peewee.CharField()
#     THIRD_PERSON = peewee.CharField()
#     SIMPLE_PAST = peewee.CharField()
#     PAST_PARTICIPLE = peewee.CharField()
#     GERUND = peewee.CharField()
#     VERBS = peewee.ForeignKeyField('Verb', backref='audio_verbs', on_delete='CASCADE', unique=True)

#     class Meta:
#         table_name = "audio_verbs"
