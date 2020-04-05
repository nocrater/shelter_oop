from human import Human


class Client(Human):
    def __init__(self, name):
        super().__init__(name)

        self.animals_to_give = []
        self.animals_to_take = []

    def act_in_housing(self, housing):
        housing.make_housing_acts(self)

    def get_animals_to_give(self):
        return self.animals_to_give

    def add_animals_to_give(self, animal):
        self.animals_to_give.append(animal)

    def remove_animals_to_give(self, animal):
        self.animals_to_give.remove(animal)

    def get_animals_to_take(self):
        return self.animals_to_take

    def add_animals_to_take(self, animal):
        self.animals_to_take.append(animal)

    def remove_animals_to_take(self, animal):
        self.animals_to_take.remove(animal)
