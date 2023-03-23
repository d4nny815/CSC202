import unittest
from graph import *

class TestList(unittest.TestCase):

    def test_01(self) -> None:
        g = Graph('test1.txt')
        self.assertEqual([['v1', 'v2', 'v3', 'v4', 'v5'], ['v6', 'v7', 'v8', 'v9']], g.conn_components())
        self.assertTrue(g.is_bipartite())
        self.assertEqual(g.get_vertex('v1'), 'v1')
        self.assertEqual(g.get_vertex('v100'), None)
        
    def test_02(self) -> None:
        g = Graph('test2.txt')
        self.assertEqual([['v1', 'v2', 'v3'], ['v4', 'v6', 'v7', 'v8']], g.conn_components())
        self.assertFalse(g.is_bipartite())
        
    def test_queue(self) -> None:
        q = Queue(5)
        self.assertTrue(q.is_empty())
        q.enqueue('a')
        q.enqueue('b')
        q.enqueue('c')
        self.assertEqual(q.size(), 3)
        self.assertEqual(q.dequeue(), 'a')
        self.assertEqual(q.dequeue(), 'b')
        self.assertEqual(q.dequeue(), 'c')
        self.assertTrue(q.is_empty())
        with self.assertRaises(IndexError):
            q.dequeue()
        q2 = Queue(3, ['a', 'b', 'c'])
        with self.assertRaises(IndexError):
            q3 = Queue(2, ['a', 'b', 'c'])
        with self.assertRaises(IndexError):
            q2.enqueue('d')
    
    def test_queue_get_items(self) -> None:
        q = Queue(5, ['a', 'b', 'c'])
        self.assertEqual(q.get_items(), ['a', 'b', 'c'])
        q2 = Queue(5)
        self.assertEqual(q2.get_items(), [])
        q.enqueue('d')
        q.enqueue('e')
        q.dequeue()
        self.assertEqual(q.get_items(), ['b', 'c', 'd', 'e'])
    def test_init_eq2(self) -> None:
        q1 = Queue(5, [1, 2, 3, 4, 5])
        q2 = Queue(5, [1, 2, 3, 4, 5])
        self.assertFalse(q1.__eq__(None))
        self.assertEqual(q1, q2)
if __name__ == '__main__':
   unittest.main()
