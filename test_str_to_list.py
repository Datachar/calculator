from unittest.case import TestCase


class TestStrToList(TestCase):
    def test_str_to_list(self):
        equations = [
            ('6 + 6', ['6', '+', '6']),
            ('2*(25+2)', ['2', '*', '(', '25', '+', '2', ')']),
            ('1 + 2', ['1', '+', '2']),
            ('1 + 2 - 3', ['1', '+', '2', '-', '3']),
            ('(1 + 2)', ['(', '1', '+', '2', ')']),
            (' 6 6 * 0 . 2581', ['6', '6', '*', '0', '.', '2581']),
            ('log(5)', ['log(', '5', ')']),
            ('0..002', ['0..002']),
            ('-4*8', ['(', '-', '4', ')', '*', '8']),
            ('4*(-8)', ['4', '*', '(', '-', '8', ')']),
            ('4*-8', ['4', '*', '-', '8']),

        ]

        for equation, expected_result in equations:
            self.assertEquals(str_to_list(equation), expected_result)
