from pony.orm import *
from .base import db

from models import Human


class Client(Human):
    animals_to_give = Set('Animal')
    animals_to_take = Set('Animal')

