import unittest
from concordance import *

class TestList(unittest.TestCase):

    def test_01(self) -> None:
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("file1.txt")
        conc.write_concordance("file1_con.txt")
        self.assertTrue(compare_files("file1_con.txt", "file1_sol.txt"))

    def test_02(self) -> None:
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("file2.txt")
        conc.write_concordance("file2_con.txt")
        self.assertTrue(compare_files("file2_con.txt", "file2_sol.txt"))

    def test_03(self) -> None:
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("declaration.txt")
        conc.write_concordance("declaration_con.txt")
        self.assertTrue(compare_files("declaration_con.txt", "declaration_sol.txt"))
        
    def test_04(self) -> None:
        conc = Concordance()
        with self.assertRaises(FileNotFoundError):
            conc.load_stop_table("not_real.txt")
            
    def test_05(self) -> None:
        conc = Concordance()
        conc.load_concordance_table("file2.txt")
        
    def test_06(self) -> None:
        ht = HashTable(7)
        ht.insert("cat", [5])
        self.assertEqual(ht.get_index("cat"), 3)

        ht.insert("dog", [8])
        self.assertEqual(ht.get_num_items(), 2)
        self.assertEqual(ht.get_index("dog"), 6)
        self.assertAlmostEqual(ht.get_load_factor(), 2 / 7)

        ht.insert("mouse", [10])
        self.assertEqual(ht.get_num_items(), 3)
        self.assertEqual(ht.get_index("mouse"), 4)
        self.assertAlmostEqual(ht.get_load_factor(), 3 / 7)

        ht.insert("elephant", [12]) # hash table should be resized
        self.assertEqual(ht.get_num_items(), 4)
        self.assertEqual(ht.get_table_size(), 15)
        self.assertAlmostEqual(ht.get_load_factor(), 4 / 15)
        self.assertEqual(ht.get_index("cat"), 12)
        self.assertEqual(ht.get_index("dog"), 14)
        self.assertEqual(ht.get_index("mouse"), 13)
        self.assertEqual(ht.get_index("elephant"), 9)
        keys = ht.get_all_keys()
        keys.sort()
        self.assertEqual(keys, ["cat", "dog", "elephant", "mouse"])
        ht.insert("wolf", [12])
        ht.insert("pig", [12])
        self.assertEqual(ht.get_index("pig"), 6)
        self.assertEqual(ht.get_index("fox"), None)
        self.assertEqual(ht.get_value("fox"), None)
        
# Compare files - takes care of CR/LF, LF issues
def compare_files(file1: str, file2: str) -> bool:
    match = True
    done = False
    with open(file1, "r") as f1:
        with open(file2, "r") as f2:
            while not done:
                line1 = f1.readline().strip()
                line2 = f2.readline().strip()
                if line1 == '' and line2 == '':
                    done = True
                if line1 != line2: # pragma: no cover
                    print("line1: ",line1)
                    print("line2: ",line2)
                    done = True
                    match = False
    return match

if __name__ == '__main__':
   unittest.main(warnings="ignore")
