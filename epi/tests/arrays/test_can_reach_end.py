import unittest
from src.arrays import can_reach_end


class TestCanReachEnd(unittest.TestCase):

    def test_can_reach_end(self):

        a = [3, 3, 1, 0, 2, 0, 1]
        res = can_reach_end.can_reach_end(a)
        self.assertTrue(res)
