from pony.orm import *
from .base import db


class Human(db.Entity):
    name = Required(str)
