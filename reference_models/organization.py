from housing import Housing
from clinic import Clinic


class Organization:
    instance = None

    housings = []
    clinics = []
    clients = []

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    @classmethod
    def get_housings(cls):
        return cls.housings

    @classmethod
    def create_housing(cls):
        housing = Housing(cls)
        cls.housings.append(housing)
        return housing

    @classmethod
    def remove_housing(cls, housing):
        cls.housings.remove(housing)

    @classmethod
    def get_clinics(cls):
        return cls.clinics

    @classmethod
    def create_clinic(cls):
        clinic = Clinic(cls)
        cls.clinics.append(clinic)
        return clinic

    @classmethod
    def remove_clinic(cls, clinic):
        cls.clinics.remove(clinic)

    @classmethod
    def get_clients(cls):
        return cls.clients

    @classmethod
    def add_client(cls, client):
        cls.clinics.append(client)

    @classmethod
    def remove_client(cls, client):
        cls.clients.remove(client)