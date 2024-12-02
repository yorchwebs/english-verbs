"""This module contains the Pydantic data validator for the form."""
from pydantic import BaseModel


class VerbFormModel(BaseModel):
    """Pydantic model for the VerbForm class."""
    verb: str
