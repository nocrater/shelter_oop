class HousingAct:
    def __init__(self, housing, animal, client, employee, type):
        self.housing = housing
        self.employee = employee
        self.animal = animal
        self.client = client
        self.type = type

    def get_housing(self):
        return self.housing

    def get_employee(self):
        return self.employee

    def get_animal(self):
        return self.animal

    def get_client(self):
        return self.client

    def get_type(self):
        return self.type
