"""11-3. Employee: Write a class called Employee. The __init__() method should take in a first name, a last name, and an annual salary, and store each of these as attributes. Write a method called give_raise() that adds $5,000 to the annual salary by default but also accepts a different raise amount.

Write a test case for Employee. Write two test methods, test_give_default_raise() and test_give_custom_raise(). Use the setUp() method so you don’t have to create a new employee instance in each test method. Run your test case, and make sure both tests pass."""
import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee = Employee('a', 'b', 1000)

    def test_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.salary, 6000 )

    def test_custom_raise(self):
        self.employee.give_raise(8000)
        self.assertEqual(self.employee.salary, 9000)


if __name__ == '__main__':
    unittest.main()