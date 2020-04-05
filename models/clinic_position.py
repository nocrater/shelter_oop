from position import Position


class ClinicPosition(Position):
    def __init__(self, clinic):
        self.clinic = clinic

    def get_clinic(self):
        return self.clinic

    def do_work(self, employee):
        pass