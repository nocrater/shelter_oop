class Clinic:
    def __init__(self, organization):
        self.organization = organization

        self.medical_acts = []
        self.animals = []

    def get_medical_acts(self):
        return self.medical_acts

    def add_medical_act(self, medical_act):
        self.medical_acts.append(medical_act)

    def remove_medical_act(self, medical_act):
        self.medical_acts.remove(medical_act)

    def get_animals(self):
        return self.animals

    def add_animal(self, animal):
        self.animals.append(animal)

    def remove_animal(self, animal):
        self.animals.remove(animal)

    def get_organization(self):
        return self.organization
