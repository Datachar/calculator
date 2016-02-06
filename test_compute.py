from unittest.case import TestCase
from compute import calculate


class TestCompute(TestCase):
    def test_calculate(self):
        test_data_simple = [
            (['(', '7', '+', '3', ')', '*', '4'], 40),
            (['(', '2', '*', '4', '+', '8', ')', '/', '4'], 4),
            (['3', '*', 'x', '=', '6'], 'x = 2'),
            (['(', '7', '+', '1', ')', '*', 'x', '=', '6'], 'x = 0.75'),
            (['1', '+', '(', '7', '-', '2', ')'], 6),
            (['6', '+', '6'], 12),
            (['2', '*', '(', '25', '+', '2', ')'], 54),
            (['0', '*', '0.002'], 0),
            (['(', '-', '4', ')', '*', '8'], -32),
        ]

        test_data_complex = [
            (['log(', '5', ')'], 1.6094379124341003),
        ]

        test_wrong_data = [
            ['4', '+', '*', '8'],
            [('-', '4'), '(', '*', '8'],
        ]

        for input_data, expected_result in test_data_simple:
            self.assertEquals(calculate(input_data), expected_result)

        for input_data, expected_result in test_data_complex:
            self.assertAlmostEqual(calculate(input_data), expected_result)

        for input_data in test_wrong_data:
            self.assertRaises(calculate(input_data), Exception)
