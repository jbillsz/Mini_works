class Employee(object):
    """ A class Employee that takes names and gives default raise or custom raise"""

    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary

    def salary_raise(self, exp_raise = None):
        if exp_raise:
            return (self.salary + exp_raise)
        else:
            return float(self.salary + 5000)
