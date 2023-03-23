import unittest
from chain_ht_linkedlist import *
from linked import *

class TestList(unittest.TestCase):

   def test_linked_1(self) -> None:
      list1 = LinkedList()
      self.assertTrue(list1.is_empty())
      list1.add(1)
      list1.add(2)
      list1.add(-1)
      list1.add(3)
      list1.remove(-1)
      self.assertEqual(list1.python_list(), [1, 2, 3])
      list1.add(-5)
      self.assertTrue(list1.search(2))
      self.assertFalse(list1.search(-2))
      # self.assertEqual(list1.index(3), 2)
      self.assertEqual(list1.size(), 4)
      self.assertEqual(list1.pop(2), 3)
      return  
   
   def test_insert1(self) -> None:
      hash1 = MyHashTable(5)
      hash1.insert(11, "a") 
      hash1.insert(3, "b")
      self.assertEqual(hash1.size(), 2)
      with self.assertRaises(ValueError):
         hash1.insert(-5, "c")
      hash1.insert(1, "a") 
      hash1.insert(2, "b") 
      hash1.insert(13, "d") 
      hash1.insert(3, "c") 
      hash1.insert(3, "d")
      hash1.insert(4, "d") 
      hash1.insert(5, "e") 
      hash1.insert(12, "f") 
      hash1.insert(11, "g") 
      hash1.insert(17, "h")
      hash1.insert(13, "h")

   def test_get1(self) -> None:
      hash1 = MyHashTable(5)
      hash1.insert(11, "a")
      hash1.insert(3, "b")
      self.assertEqual(hash1.get_item(3), 'b')
      self.assertEqual(hash1.get_item(11), 'a')
      # 
   def test_get2(self) -> None:
      hash1 = MyHashTable(5)
      hash1.insert(11, "a")
      with self.assertRaises(LookupError):
            hash1.get_item(6)

   def test_remove1(self) -> None:
      hash1 = MyHashTable(5)
      hash1.insert(11, "a")
      self.assertEqual(hash1.remove(11), (11, 'a'))
      self.assertEqual(hash1.size(), 0)
      hash1.insert(3, "b")
      with self.assertRaises(LookupError):
            hash1.remove(6)
      

   def test_load_factor1(self) -> None:
      hash1 = MyHashTable(5)
      hash1.insert(11, "a")
      hash1.insert(3, "b")
      hash1.insert(1, "c")
      hash1.insert(8, "d")
      hash1.insert(4, "e")
      hash1.insert(5, "f")
      hash1.insert(1, "g")
      hash1.insert(2, "h")
      self.assertEqual(hash1.load_factor(), 1.4)

   def test_collisions2(self) -> None:
      hash1 = MyHashTable(5)
      hash1.insert(11, "a") 
      hash1.insert(3, "b") 
      hash1.insert(1, "c") 
      hash1.insert(8, "d") 
      hash1.insert(4, "e") 
      hash1.insert(5, "f") 
      hash1.insert(1, "g") 
      hash1.insert(2, "h")
      print(hash1)
      self.assertEqual(hash1.collisions(), 2)
      

      

if __name__ == '__main__': 
   unittest.main()


