from enum import Enum


class State(Enum):
    Healthy, Sick, Vaccine_Need, Sick_And_Vaccine_Need = range(4)
