from animal import Animal
from client import Client
from clinic_position import ClinicPosition
from employee import Employee
from organization import Organization
from shelter_position import ShelterPosition
from enums.species import Species
from enums.state import State
from veterinarian_position import VeterinarianPosition


def main():
    # Получение организации и создание 3 приютов и 2 клиник с рабочими.
    organization = Organization()

    # Приюты
    housing1 = organization.create_housing()
    housing2 = organization.create_housing()
    housing3 = organization.create_housing()

    shelter_position1 = ShelterPosition(housing1)
    shelter_position2 = ShelterPosition(housing2)
    shelter_position3 = ShelterPosition(housing3)

    # Клиники
    clinic1 = organization.create_clinic()
    clinic2 = organization.create_clinic()

    clinic_position1 = ClinicPosition(clinic1)
    clinic_position2 = ClinicPosition(clinic2)

    veterinarian_position1 = VeterinarianPosition(clinic1)
    veterinarian_position2 = VeterinarianPosition(clinic2)

    positions1 = [shelter_position1, clinic_position1]
    positions2 = [shelter_position2, clinic_position2]
    positions3 = [shelter_position3, clinic_position2]
    positions4 = [veterinarian_position1]
    positions5 = [veterinarian_position2]

    # Работники
    john_housing_one = Employee("John", positions1)
    elena_housing_one = Employee("Elena", positions1)
    sergey_housing_one = Employee("Sergey", positions1)

    ivan_housing_two = Employee("Ivan", positions2)

    robert_housing_three = Employee("Robert", positions3)
    alice_housing_three = Employee("Alice", positions3)

    # Ветеринары
    max_clinic_one = Employee("Max", positions4)
    xenia_clinic_one = Employee("Xenia", positions4)

    arnold_clinic_two = Employee("Arnold", positions5)
    sergey_clinic_two = Employee("Sergey", positions5)

    # Создание животных по 3 штуки в каждый приют изначально.
    animal1 = Animal("John", Species.Cat, "Good cat", State.Healthy)
    animal2 = Animal("Ai", Species.Dog, "Good dog", State.Vaccine_Need)
    animal3 = Animal("Okok", Species.Cat, "Good cat", State.Healthy)

    housing1.add_animal(animal1)
    housing1.add_animal(animal2)
    housing1.add_animal(animal3)

    clinic1.add_animal(animal2)

    animal4 = Animal("Kilok", Species.Cat, "Good cat", State.Sick)
    animal5 = Animal("Jim", Species.Cat, "Good cat", State.Vaccine_Need)
    animal6 = Animal("Neutron", Species.Cat, "Good cat", State.Healthy)

    housing2.add_animal(animal4)
    housing2.add_animal(animal5)
    housing2.add_animal(animal6)

    clinic1.add_animal(animal4)
    clinic2.add_animal(animal5)

    animal7 = Animal("Nesq", Species.Dog, "Good dog", State.Sick_And_Vaccine_Need)
    animal8 = Animal("Catee", Species.Dog, "Good dog", State.Healthy)
    animal9 = Animal("Mona", Species.Dog, "Good dog", State.Healthy)

    housing3.add_animal(animal7)
    housing3.add_animal(animal8)
    housing3.add_animal(animal9)

    clinic1.add_animal(animal7)

    # Создание 2 клиентов, один хочет отдать двух животных,
    # другой одного отдать и взять одного с первого приюта.

    client1 = Client("Kik")

    animal_to_give = Animal("Catees", Species.Cat, "Good cat", State.Healthy)
    animal_to_give1 = Animal("Catees2", Species.Cat, "Good cat 2", State.Healthy)

    client1.add_animals_to_give(animal_to_give)
    client1.add_animals_to_give(animal_to_give1)

    client2 = Client("John")

    animal_to_give2 = Animal("Catees", Species.Cat, "Good cat", State.Sick)
    animal_to_take = housing1.get_animals()[0]

    client2.add_animals_to_give(animal_to_give2)
    client2.add_animals_to_take(animal_to_take)

    # Клиенты совершают действия
    client1.act_in_housing(housing1)
    client2.act_in_housing(housing1)

    # Работники делают свои обязанности, проверяют на наличие больных животных,
    # переносят их в клинику при необходимости.
    john_housing_one.do_work()
    ivan_housing_two.do_work()
    alice_housing_three.do_work()

    # Ветеринары проверяют нужно ли кому-то сделать операции и делают при необходимости.
    max_clinic_one.do_work()
    arnold_clinic_two.do_work()

    # Работники еще раз проверяют животных, забирают вылеченных с клиники.
    john_housing_one.do_work()
    ivan_housing_two.do_work()
    alice_housing_three.do_work()


if __name__ == "__main__":
    main()