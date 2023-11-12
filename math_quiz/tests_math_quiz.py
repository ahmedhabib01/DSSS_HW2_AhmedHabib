import unittest
from math_quiz import Function_A, Function_B, Function_C

class TestMathGame(unittest.TestCase):
    def test_function_A(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = Function_A(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_function_B(self):
        # TODO
        operators = set(['+', '-', '*'])
        for _ in range(1000):
            operator = Function_B()
            self.assertIn(operator, operators)
        
    def test_function_C(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (4, 3, '*', '4 * 3', 12),
                (100, 50, '-', '100 - 50', 50)
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                #TODO
                Problem, result = Function_C(num1, num2, operator)
                self.assertEqual(Problem, expected_problem)
                self.assertEqual(result, expected_answer)

if __name__ == "__main__":
    unittest.main()