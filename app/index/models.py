# app/index/models.py

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Verb(Base):
    """
    Modelo que representa un verbo.

    Atributos:
        num (int): Clave primaria.
        type (str): Tipo de verbo.
        simple_form (str): Forma simple.
        third_person (str): Tercera persona.
        simple_past (str): Pasado simple.
        past_participle (str): Participio pasado.
        gerund (str): Gerundio.
        meaning (str): Significado.
    """

    __tablename__ = "verbs"

    num = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(String)
    simple_form = Column(String)
    third_person = Column(String)
    simple_past = Column(String)
    past_participle = Column(String)
    gerund = Column(String)
    meaning = Column(String)

    audio_verb = relationship("AudioVerb", back_populates="verb", uselist=False)


class AudioVerb(Base):
    """
    Modelo que representa los audios para cada forma verbal.

    Atributos:
        id (int): Clave primaria.
        simple_form (str): URL del audio de la forma simple.
        third_person (str): URL del audio de la tercera persona.
        simple_past (str): URL del audio del pasado simple.
        past_participle (str): URL del audio del participio.
        gerund (str): URL del audio del gerundio.
        verb_id (int): Relación con el verbo.
    """

    __tablename__ = "audio_verbs"

    id = Column(Integer, primary_key=True)
    simple_form = Column(String)
    third_person = Column(String)
    simple_past = Column(String)
    past_participle = Column(String)
    gerund = Column(String)

    verb_id = Column(Integer, ForeignKey("verbs.num"), unique=True)
    verb = relationship("Verb", back_populates="audio_verb")
