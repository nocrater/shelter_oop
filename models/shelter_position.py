from position import Position
from housing_act_type import HousingActType
from where_now import WhereNow
from state import State
from clinic_position import ClinicPosition


class ShelterPosition(Position):
    def __init__(self, housing):
        self.housing = housing

    def get_housing(self):
        return self.housing

    def make_housing_acts(self, client, employee):
        for animal in client.get_animals_to_give():
            self.make_giving_housing_act(animal, client, employee)
        for animal in client.get_animals_to_take():
            self.make_taking_housing_act(animal, client, employee)

    def make_giving_housing_act(self, animal, client, employee):
        print(employee.get_name() + " makes HousingAct of giving type with client " + client.get_name())
        housing_act = HousingAct(self, animal, client, employee, HousingActType.GivingAnimals)

        client.add_animals_to_take(animal)
        print("Client " + client.get_name() + " takes animal " + animal.get_name() +
              " with characteristics " + animal.get_description())

        self.housing.add_animal(animal)
        self.housing.add_housing_act(housing_act)

    def make_taking_housing_act(self, animal, client, employee):
        print(employee.get_name() + " makes HousingAct of taking type with client " + client.get_name())
        housing_act = HousingAct(self, animal, client, employee, HousingActType.TakingAnimals)

        client.remove_animals_to_give(animal)
        print("Client " + client.get_name() + " gives animal " + animal.get_name() +
              " with characteristics " + animal.get_description())

        self.housing.remove_animal(animal)
        self.housing.add_housing_act(housing_act)

    def do_work(self, employee):
        print(employee.get_name() + " makes inspection")

        for animal in self.housing.animals:
            if animal.where_now == WhereNow.Housing and animal.get_state() != State.Healthy:
                carried_to_clinic = False

                for position in employee.get_positions():
                    if isinstance(position, ClinicPosition):
                        self.carry_to_clinic(animal, position.get_clinic(), employee)
                        carried_to_clinic = True
                        break

                if not carried_to_clinic:
                    print(employee.get_name() + " don't know to which clinic to go")

            if animal.where_now == WhereNow.Clinic and animal.get_state() == State.Healthy:
                for position in employee.get_positions():
                    if isinstance(position, ClinicPosition):
                        clinic = position.get_clinic()
                        if animal in clinic.get_animals():
                            self.take_from_clinic(animal, clinic, employee)
                            break

    def carry_to_clinic(self, animal, clinic, employee):
        print(employee.get_name() + " carries to clinic " + animal.get_name())

        animal.set_where_now(WhereNow.Clinic)

        clinic.add_animal(animal)

    def take_from_clinic(self, animal, clinic, employee):
        print(employee.get_name() + " takes from clinic " + animal.get_name())

        animal.set_where_now(WhereNow.Housing)

        clinic.remove_animal(animal)
