import unittest
from stack_nodelist import *
        
class TestLab2(unittest.TestCase):

    def test_node_init(self) -> None:
        node1 = Node(1, None)
        self.assertEqual(node1.value, 1)
        self.assertEqual(node1.rest, None)

        node2 = Node(2, node1)
        self.assertEqual(node2.value, 2)
        self.assertEqual(node2.rest, node1)

    def test_node_eq(self) -> None:
        node1a = Node(1, None)
        node1b = Node(1, None)
        node2a = Node(2, node1a)
        node2b = Node(2, node1b)

        self.assertEqual(node1a, node1b)
        self.assertNotEqual(node1a, node2a)
        self.assertEqual(node2a, node2b)
        node1a = Node(3, None)
        self.assertNotEqual(node1a, node1b)

        self.assertFalse(node1a.__eq__(None))

    def test_node_repr(self) -> None:
        node = Node(2, Node(1, None))
        self.assertEqual(node.__repr__(), "Node(2, Node(1, None))")

    def test_stack_init(self) -> None:
        stack = Stack()
        self.assertEqual(stack.top, None)

        init_stack = Node(2, Node(1, None))
        stack = Stack(init_stack)
        self.assertEqual(stack.top, init_stack)

    def test_stack_eq(self) -> None:
        stack1 = Stack()
        stack2 = Stack()
        init_stack = Node(2, Node(1, None))
        stack4 = Stack(init_stack)
        self.assertEqual(stack1, stack2)
        self.assertNotEqual(stack1, stack4)
        self.assertFalse(stack1.__eq__(None))

    def test_stack_repr(self) -> None:
        init_stack = Node(2, Node(1, None))
        stack = Stack(init_stack)
        self.assertEqual(stack.__repr__(), "Stack(Node(2, Node(1, None)))")
        
    def test_isempty(self) -> None:
        stack1 = Stack()
        init_stack = Node(2, Node(1, None))
        stack2 = Stack(init_stack)
        self.assertTrue(stack1.is_empty())
        self.assertFalse(stack2.is_empty())
        return
    
    def test_push(self) -> None:
        stack1 = Stack()
        stack1.push(1)
        self.assertFalse(stack1.is_empty())
        self.assertEqual(stack1.peek(), 1)
        return
    
    def test_pop(self) -> None:
        stack1 = Stack(Node(1, None))
        self.assertEqual(stack1.pop(), 1)
        with self.assertRaises(IndexError):
            stack1.pop()
        return
    
    def test_peek(self) -> None:
        stack1 = Stack(Node(1, None))
        stack2 = Stack()
        self.assertEqual(stack1.peek(), 1)
        with self.assertRaises(IndexError):
            stack2.peek()
        return

    def test_size(self) -> None:
        stack1 = Stack(Node(1, None))
        stack2 = Stack()
        self.assertEqual(stack1.size(), 1)
        self.assertEqual(stack2.size(), 0)
        return
# WRITE TESTS FOR STACK OPERATIONS - PUSH, POP, PEEK, etc.

if __name__ == '__main__': 
    unittest.main()
