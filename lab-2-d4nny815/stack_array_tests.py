import unittest
from stack_array import Stack
        
class TestLab2(unittest.TestCase):

    def test_init(self) -> None:
        stack = Stack(5)
        self.assertEqual(stack.items, [None]*5)
        self.assertEqual(stack.capacity, 5)

        stack = Stack(5, [1, 2])
        self.assertEqual(stack.items[0:2], [1, 2])
        self.assertEqual(stack.capacity, 5)

        with self.assertRaises(IndexError):
            Stack(5, [1, 2, 3, 4, 5, 6])

    def test_eq(self) -> None:
        stack1 = Stack(5)
        stack2 = Stack(5)
        stack3 = Stack(10)
        stack4 = Stack(5,[1, 2])
        self.assertEqual(stack1, stack2)
        self.assertNotEqual(stack1, stack3)
        self.assertNotEqual(stack1, stack4)
        self.assertFalse(stack1.__eq__(None))

    def test_repr(self) -> None:
        stack = Stack(5, [1, 2])
        self.assertEqual(stack.__repr__(), "Stack(5, [1, 2])")
    
    def test_isempty(self) -> None:
        stack1 = Stack(5)
        stack2 = Stack(5, [1, 2, 3])
        self.assertTrue(stack1.is_empty())
        self.assertFalse(stack2.is_empty())
        return
    
    def test_isfull(self) -> None:
        stack1 = Stack(5, [1, 2, 3, 4, 5])
        stack2 = Stack(5)
        self.assertTrue(stack1.is_full())
        self.assertFalse(stack2.is_full())
        return
    
    def test_push(self) -> None:
        stack1 = Stack(5, [1, 2, 3, 4])
        stack1.push(5)
        self.assertEqual(stack1.peek(), 5)
        with self.assertRaises(IndexError):
            stack1.push(1)
        return
    
    def test_pop(self) -> None:
        stack1 = Stack(5, [1, 2])
        self.assertEqual(stack1.pop(), 2)
        self.assertEqual(stack1.pop(), 1)
        with self.assertRaises(IndexError):
            stack1.pop()
        return
    
    def test_peek(self) -> None:
        stack1 = Stack(5, [1, 2])
        stack2 = Stack(5)
        self.assertEqual(stack1.peek(), 2)
        with self.assertRaises(IndexError):
            stack2.peek()
        return
    
    def test_size(self) -> None:
        stack1 = Stack(5, [1, 2])
        self.assertEqual(stack1.size(), 2)
        return
    

# WRITE TESTS FOR STACK OPERATIONS - PUSH, POP, PEEK, etc.

if __name__ == '__main__': 
    unittest.main()
