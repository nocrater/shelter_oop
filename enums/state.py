from enum import Enum

from pony.orm.dbapiprovider import StrConverter


class State(Enum):
    Healthy, Sick, Vaccine_Need, Sick_And_Vaccine_Need = range(4)


class StateConverter(StrConverter):

    def validate(self, val, obj):
        if not isinstance(val, State):
            raise ValueError('Must be an State.  Got {}'.format(type(val)))
        return val

    def py2sql(self, val):
        return val.name

    def sql2py(self, value):
        # Any enum type can be used, so py_type ensures the correct one is used to create the enum instance
        return self.py_type[value]