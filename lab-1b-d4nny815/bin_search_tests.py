import unittest
from bin_search import *
from typing import List

class TestLab1b(unittest.TestCase):

    def test_bin_search_iter_01(self) -> None:
        tlist: List = [5, 9, 18, 23, 55, 72]
        self.assertEqual(bin_search_iter(tlist, 5), 0)
        return None

    def test_bin_search_iter_02(self) -> None:
        tlist = None
        with self.assertRaises(ValueError):  # uses context manager for checking exception
            bin_search_iter(tlist, 5)
        return None
    
    def test_bin_search_iter_03(self) -> None:
        tlist: List = [5, 9, 18, 23, 55, 72]
        self.assertEqual(bin_search_iter(tlist, 72), 5)
        return None
    
    def test_bin_search_iter_04(self) -> None:
        tlist: List = [5, 9, 18, 23, 55, 72]
        self.assertEqual(bin_search_iter(tlist, 23), 3)
        return None
    
    def test_bin_search_iter_05(self) -> None:
        tlist: List = [5, 9, 18, 23, 55, 72]
        self.assertEqual(bin_search_iter(tlist, -1), None)
        return None
    
    def test_bin_search_rec_01(self) -> None:
        tlist: List = [5, 9, 18, 23, 55, 72]
        self.assertEqual(bin_search_rec(tlist, 5), 0)
        return None

    def test_bin_search_rec_02(self) -> None:
        tlist = None
        with self.assertRaises(ValueError):  # uses context manager for checking exception
            bin_search_rec(tlist, 5)
        return None
    
    def test_bin_search_rec_03(self) -> None:
        tlist: List = [5, 9, 18, 23, 55, 72]
        self.assertEqual(bin_search_rec(tlist, 72), 5)
        return None
    
    def test_bin_search_rec_04(self) -> None:
        tlist: List = [5, 9, 18, 23, 55, 72]
        self.assertEqual(bin_search_rec(tlist, -1), None)
        return None
    
    

if __name__ == "__main__":
        unittest.main()
