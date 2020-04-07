class MedicalAct:
    def __init__(self, clinic, employee, animal_card, description):
        self.clinic = clinic
        self.employee = employee
        self.animal_card = animal_card
        self.description = description

    def get_clinic(self):
        return self.clinic

    def get_employee(self):
        return self.employee

    def get_animal_card(self):
        return self.animal_card

    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description
