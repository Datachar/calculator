from unittest.case import TestCase
from log import ln
import math

class TestStrToList(TestCase):
    def test_str_to_list(self):
        equations = [
            (10, math.log(10)),
            (100, math.log(100)),
            (0.012358, math.log(0.012358)),
            (1, math.log(1)),
            (12345, math.log(12345)),
            (9.999999999999, math.log(9.999999999999))
            #(704645, math.log(704645)),
            #(0.0000000001, math.log(0.0000000001))
        ]

        for equation, expected_result in equations:
            self.assertEquals(format(ln(equation),'.10f'), format(expected_result,'.10f'))
