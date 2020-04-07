from position import Position
from enums.state import State
from vaccine import Vaccine
from medical_act import MedicalAct


class VeterinarianPosition(Position):
    def __init__(self, clinic):
        self.clinic = clinic

    def do_work(self, employee):
        print(employee.get_name() + " makes inspection")

        for animal in self.clinic.get_animals():
            if animal.get_state() == State.Sick:
                self.cure(animal, employee)
            elif animal.get_state() == State.Vaccine_Need:
                self.make_vaccine(animal, employee)
            elif animal.get_state() == State.Sick_And_Vaccine_Need:
                self.cure(animal, employee)
                self.make_vaccine(animal, employee)

    def cure(self, animal, employee):
        animal_card = animal.get_card()

        description = "The left paw was cured."

        medical_act = MedicalAct(self.clinic, employee, animal_card, description)

        animal_card.add_medical_act(medical_act)
        self.clinic.add_medical_act(medical_act)

        print(employee.get_name() + " makes medical act with operation '" + description +
              " on " + animal.get_name())

        animal_card.add_medical_act(medical_act)
        self.clinic.add_medical_act(medical_act)

        if animal.get_state() == State.Sick:
            animal.set_state(State.Healthy)
        elif animal.get_state() == State.Sick_And_Vaccine_Need:
            animal.set_state(State.Vaccine_Need)

        print("The animal's state now is " + animal.get_state().name)

    def make_vaccine(self, animal, employee):
        animal_card = animal.get_card()

        description = "The vaccine was injected"

        vaccine = Vaccine("DHPPi")
        animal_card.add_vaccine(vaccine)

        medical_act = MedicalAct(self.clinic, employee, animal_card, description)

        print(employee.get_name() + " makes medical act with operation '" +
              description + "' on " + animal.get_name())

        animal_card.add_medical_act(medical_act)
        self.clinic.add_medical_act(medical_act)

        if animal.get_state() == State.Vaccine_Need:
            animal.set_state(State.Healthy)
        elif animal.get_state() == State.Sick_And_Vaccine_Need:
            animal.set_state(State.Sick)

        print("The animal's state now is " + animal.get_state().name)
