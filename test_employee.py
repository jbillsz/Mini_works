import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.employee = Employee("Kwamz", "Amadi",2500)

    def test_custom_raise(self):
        exp_amount = 7500
        new_raise = self.employee.salary_raise(exp_amount)
        self.assertEqual(10000, new_raise)

    def test_default_raise(self):
        self.assertEqual(7500, self.employee.salary_raise())
unittest.main()
