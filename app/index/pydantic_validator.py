from pydantic import BaseModel


class VerbFormModel(BaseModel):
    verb: str
