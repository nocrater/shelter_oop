from pony.orm import *
from .base import db

from enums.species import Species
from enums.state import State
from enums.where_now import WhereNow


class Animal(db.Entity):
    name = Required(str)
    description = Required(LongUnicode)

    species = Required(Species)
    state = Required(State)
    where_now = Required(WhereNow)

    giving_client = Optional("Client", reverse='animals_to_give')
    taking_client = Optional("Client", reverse='animals_to_take')
