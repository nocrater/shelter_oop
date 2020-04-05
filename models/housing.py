from shelter_position import ShelterPosition


class Housing:
    def __init__(self, organization):
        self.organization = organization

        self.employees = []
        self.housing_acts = []
        self.animals = []

    def make_housing_acts(self, client):
        for employee in self.employees:
            for postion in employee.get_postions():
                if isinstance(postion, ShelterPosition):
                    postion.make_housing_acts(client, employee)

    def get_employees(self):
        return self.employees

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, employee):
        self.employees.remove(employee)

    def get_housing_acts(self):
        return self.housing_acts

    def add_housing_act(self, housing_act):
        self.housing_acts.append(housing_act)

    def remove_housing_act(self, housing_act):
        self.housing_acts.remove(housing_act)

    def get_animals(self):
        return self.animals

    def add_animal(self, animal):
        self.animals.append(animal)

    def remove_animal(self, animal):
        self.animals.remove(animal)
