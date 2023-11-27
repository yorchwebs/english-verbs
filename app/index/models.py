import peewee

from app.db.database import MySQLDatabaseSingleton


database = MySQLDatabaseSingleton().database


class BaseModel(peewee.Model):
    """
    A base model class that all other models should inherit from.

    Attributes:
        database (Database): The database connection to use for this model.
    """

    class Meta:
        database = database
        
class Verb(BaseModel):
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