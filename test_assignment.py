
import unittest
from assignment import *

class TestAssignment(unittest.TestCase):
    # Part 1: Python Syntax
    def test_format_string(self):
        self.assertEqual(format_string("Jibril", 25), "My name is Jibril and I am 25 years old")

    def test_conditional_check(self):
        self.assertEqual(conditional_check(5), "Lesser")
        self.assertEqual(conditional_check(10), "Equal")
        self.assertEqual(conditional_check(15), "Greater")

    def test_loop_sum(self):
        self.assertEqual(loop_sum(5), 15)
        self.assertEqual(loop_sum(10), 55)

    # Part 2: Data Structures
    def test_list_operations(self):
        self.assertEqual(list_operations([1, 2, 3, 4]), (10, 4, 1))

    def test_dict_operations(self):
        students = {"Alice": 85, "Bob": 78, "Charlie": 90}
        self.assertEqual(dict_operations(students), ["Alice", "Charlie"])

    def test_set_operations(self):
        self.assertEqual(set_operations([1, 2, 3], [3, 4, 5]), {3})

    # Part 3: Operators
    def test_arithmetic_ops(self):
        self.assertEqual(arithmetic_ops(10, 2), {
            'sum': 12, 'difference': 8, 'product': 20, 'quotient': 5.0
        })
        self.assertEqual(arithmetic_ops(10, 0)['quotient'], 'undefined')

    def test_logical_ops(self):
        self.assertEqual(logical_ops(True, False), {
            'and': False, 'or': True, 'not_x': False
        })

    def test_bitwise_ops(self):
        self.assertEqual(bitwise_ops(6, 3), {
            'and': 2, 'or': 7, 'xor': 5
        })

if __name__ == "__main__":
    unittest.main()
