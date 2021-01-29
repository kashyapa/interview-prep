import unittest
from src.arrays import even_odd


class TestEvenOdd(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        arr = [1, 2, 345, 563, 534, 3234, 54, 76, 98]
        even_odd.print_hello_world()
        cls.arr = even_odd.even_odd(arr)
        cls.length = len(arr)

    def test_even_odd(self):
        is_odd = False
        last_even_index = 0
        for i in range(0, self.length):
            if is_odd is True:
                self.assertTrue(i > last_even_index)
            if is_odd is False and self.arr[i] % 2 == 1:
                is_odd = True
                last_even_index = i - 1
            if is_odd is False:
                self.assertEqual(self.arr[i]%2, 0)
            else:
                self.assertEqual(self.arr[i]%2, 1)
