class AnimalCard:
    def __init__(self, species, state, animal):
        self.species = species
        self.state = state
        self.animal = animal

        self.vaccines = []
        self.medical_acts = []

    def get_species(self):
        return self.species

    def get_animal(self):
        return self.animal

    def get_state(self):
        return self.state

    def get_vaccines(self):
        return self.vaccines

    def add_vaccine(self, vaccine):
        self.vaccines.append(vaccine)

    def get_medical_acts(self):
        return self.medical_acts

    def add_medical_act(self, medical_act):
        self.medical_acts.append(medical_act)
