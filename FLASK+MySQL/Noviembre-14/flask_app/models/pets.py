

from dataclasses import dataclass
from datetime import date
from typing import ClassVar
from flask_app.models.default_model import default_model

@dataclass(init=False)
class pets(default_model):

    table_name: ClassVar[str] = 'pets'

    name: str
    birthdate: date
    breed_id: int
    owner_id: int



