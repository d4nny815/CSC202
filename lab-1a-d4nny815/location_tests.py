# CPE 202 Location Class Test Cases, Lab 1

import unittest
from location import *

class TestLocation(unittest.TestCase):

    def test_repr(self) -> None:
        loc = Location('SLO', 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")
        return None
    
    def test_eq(self) -> None:
        loc1 = Location('SLO', 35.3, -120.7)
        loc2 = Location("Paris", 48.9, 2.4)
        loc3 = Location('SLO', 35.3, -120.7)
        self.assertFalse(loc1 == loc2)
        self.assertTrue(loc1 == loc3)
        self.assertFalse(loc1 == None)
        return None

if __name__ == "__main__":
        unittest.main()
