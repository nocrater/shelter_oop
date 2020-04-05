from human import Human


class Employee(Human):
    def __init__(self, name, positions):
        super().__init__(name)
        self.positions = positions

    def do_work(self):
        for position in self.positions:
            position.do_work(self)

    def get_positions(self):
        return self.positions
