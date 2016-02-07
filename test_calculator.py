from unittest.case import TestCase
from calculator import calculator

class TestCalc(TestCase):
    def test_calc(self):
        test_data_simple = [
            ('( 7 + 3 ) *4', 40),
            ('(2 * 4 + 8 ) / 4', 4),
            ('2 * ( 25 + 2 )', 54),
            ('( - 4 ) * 8', -32),
            ('0 * 0.002', 0),
            ('+5', 5),
            ('(32 * (23 +8 * 4) - 25 /84 + (15 *554))', 10069.702380952382),
        ]
        test_data_complex = [
            ('log(5)', 1.6094379124341003),
        ]
        test_wrong_data = [
            '4 + * 8',
            '(- 4) ( * 8',
            '5 / 0',
            '( 5 - 1',
        ]

        for input_data, expected_result in test_data_simple:
            self.assertEquals(calculator(input_data), expected_result)

        for input_data, expected_result in test_data_complex:
            self.assertAlmostEqual(calculator(input_data), expected_result)


        for input_data in test_wrong_data:
            self.assertRaises(Exception, calculator(input_data))

