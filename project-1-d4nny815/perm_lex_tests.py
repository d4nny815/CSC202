import unittest
import perm_lex
from typing import List

# Starter test cases - write more!

class TestAssign1(unittest.TestCase):

    def test_perm_gen_lex_1(self) -> None:
        self.assertEqual(perm_lex.perm_gen_lex('ab'),['ab','ba'])
        return None
    
    def test_perm_gen_lex_2(self) -> None:
        self.assertEqual(perm_lex.perm_gen_lex('abc'),['abc','acb','bac','bca','cab','cba'])
        return None
    
    def test_perm_gen_lex_3(self) -> None:
        self.assertEqual(perm_lex.perm_gen_lex('a'),['a'])
        return None

if __name__ == "__main__":
        unittest.main()
