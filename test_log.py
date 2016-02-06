from unittest.case import TestCase
from log import log
import math

class TestStrToList(TestCase):
    def test_str_to_list(self):
        equations = [
            (10, math.log(10)),
            (100, math.log(100)),
            (0.012358, math.log(0.012358)),
            (1, math.log(1)),
            (12345, math.log(12345)),
            (9.999999999999, math.log(9.999999999999)),
            (18012.3254, math.log(18012.3254)),
            (0.00008, math.log(0.00008))
        ]

        for equation, expected_result in equations:
            self.assertEquals(format(log(equation),'.10f'), format(expected_result,'.10f'))
