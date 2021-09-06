import unittest
from src.strings import strstr


class TestStrStr(unittest.TestCase):

    def test_str_str(self):

        haystack = "Hello"
        needle = "ll"

        res = strstr.strStr(haystack, needle)
        self.assertEqual(res, 2)
