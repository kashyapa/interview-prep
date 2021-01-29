import unittest
from src.arrays import delete_duplicates


class TestDeleteDuplicates(unittest.TestCase):

    def test_delete_duplicates(self):
        arr = [2, 3, 5, 5, 7, 11, 11, 13]
        w = delete_duplicates.delete_duplicates(arr)
        print(arr[:w])
        arr = [2, 3, 5, 5, 7, 11, 11, 13, 13]
        w = delete_duplicates.delete_duplicates(arr)
        print(arr[:w])
        arr = [2, 3, 5, 5,  11, 11]
        w = delete_duplicates.delete_duplicates(arr)
        print(arr[:w])