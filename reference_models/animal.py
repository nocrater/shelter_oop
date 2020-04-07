from enums.where_now import WhereNow
from animal_card import AnimalCard


class Animal:
    def __init__(self, name, species, description, state):
        self.name = name
        self.species = species
        self.description = description
        self.state = state

        self.where_now = WhereNow.Housing

        self.card = AnimalCard(species, state, self)

    def get_card(self):
        return self.card

    def set_card(self, card):
        self.card = card

    def get_name(self):
        return self.name

    def get_species(self):
        return self.species

    def get_description(self):
        return self.description

    def set_where_now(self, where_now):
        self.where_now = where_now

    def get_where_now(self):
        return self.where_now

    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state
