import unittest
from binary_search_tree import *


class TestLab4(unittest.TestCase):

    def test_00(self) -> None:
        tn1 = TreeNode(1, None)
        tn2 = TreeNode(1, None)
        self.assertFalse(tn1.__eq__(None))
        self.assertEqual(tn1, tn2)
        self.assertEqual(tn1.__repr__(), "TreeNode(1, None, None, None)")

    def test_01_simple(self) -> None:
        bst = BinarySearchTree()
        self.assertEqual(bst.tree_height(), None)
        self.assertTrue(bst.is_empty())

    def test_02_insert_search(self) -> None:
        bst = BinarySearchTree()
        values = [99, -4, 167, 139, 55, -89, 13, 78, 128, 119]

        for val in values:
            bst.insert(val)
        for val in values:
            self.assertTrue(bst.search(val))
            self.assertFalse(bst.search(val - 1))
            self.assertFalse(bst.search(val + 1))
        self.assertEqual(bst.find_min(), (-89, None))

    def test_03_search_empty_list(self) -> None:
        bst = BinarySearchTree()
        self.assertFalse(bst.search(999))

    def test_04_pre_in_level_order_empty_list(self) -> None:
        bst = BinarySearchTree()
        self.assertEqual(bst.preorder_list(), [])
        self.assertEqual(bst.inorder_list(), [])
        self.assertEqual(bst.level_order_list(), [])

    def test_07_test_min_max_empty(self) -> None:
        bst = BinarySearchTree()
        self.assertEqual(None, bst.find_max())
        self.assertEqual(None, bst.find_min())

    def test_08_test_inorder(self) -> None:
        bst = BinarySearchTree()
        keys = [99, -4, 167, 139, 55, -89, 13, 78, 178, 174]

        for i in range(len(keys)):
            bst.insert(keys[i])

        self.assertEqual(bst.inorder_list(), [-89, -4, 13, 55, 78, 99, 139, 167, 174, 178])

    def test_09_test_preorder(self) -> None:
        bst = BinarySearchTree()
        keys = [99, -4, 167, 139, 55, -89, 13, 78, 178, 174]

        for i in range(len(keys)):
            bst.insert(keys[i])

        self.assertEqual(bst.preorder_list(), [99, -4, -89, 55, 13, 78, 167, 139, 178, 174])

    def test_09_test_level_order(self) -> None:
        keys = [99, -4, 167, 139, 55, -89, 13, 78, 178, 174]

        bst = BinarySearchTree()
        for i in range(len(keys)):
            bst.insert(keys[i])

        self.assertEqual(bst.level_order_list(), [99, -4, 167, -89, 55, 139, 178, 13, 78, 174])

    def test_14_insert_replace(self) -> None:
        bst = BinarySearchTree()
        bst.insert(30, 'aaa')
        bst.insert(40, 'bbb')
        bst.insert(35, 'ccc')
        bst.insert(50, 'ddd')
        bst.insert(60, 'eee')
        bst.insert(45, 'zzz')
        bst.insert(60, 'zzz')
        bst.insert(35, 'zzz')
        self.assertEqual(bst.find_max(), (60, 'zzz'))
        self.assertEqual(bst.find_min(), (30, 'aaa'))
        self.assertEqual(bst.tree_height(), 3)

    def test_16_test_tree_height(self) -> None:
        bst = BinarySearchTree()
        keys = [99, -4, 167, 139, 55, -89, 13, 78, 178, 174]

        for i in range(len(keys)):
            bst.insert(keys[i])
        self.assertEqual(bst.tree_height(), 3)

    def test_array(self) -> None:
        q = Queue(5)
        self.assertEqual(q.items, [None, None, None, None, None])
        self.assertEqual(q.get_items(), [])
        q.enqueue(1)
        self.assertEqual(q.items, [1, None, None, None, None])
        q.enqueue(2)
        self.assertEqual(q.items, [1, 2, None, None, None])

    def test_init_eq(self) -> None:
        with self.assertRaises(IndexError):
            q = Queue(5, [1, 2, 3, 4, 5, 6])
        q1 = Queue(5, [1, 2, 3, 4])
        self.assertEqual(q1.get_items(), [1, 2, 3, 4])
        q2 = Queue(5, [1, 2, 3, 4])
        self.assertEqual(q1, q2)

    def test_init_eq2(self) -> None:
        q1 = Queue(5, [1, 2, 3, 4, 5])
        q2 = Queue(5, [1, 2, 3, 4, 5])
        self.assertFalse(q1.__eq__(None))
        self.assertEqual(q1, q2)

    def test_repr(self) -> None:
        q1 = Queue(5, [])
        self.assertEqual(q1.__repr__(), "Queue(5, [])")

    def test_queue_simple(self) -> None:
        q = Queue(5)
        q.enqueue(1)
        self.assertEqual(q.size(), 1)
        q.enqueue(2)
        q.enqueue(3)
        q.enqueue(4)
        q.enqueue(5)
        with self.assertRaises(IndexError):
            q.enqueue(1)
        self.assertEqual(q.size(), 5)
        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.dequeue(), 2)
        self.assertEqual(q.dequeue(), 3)
        self.assertEqual(q.dequeue(), 4)
        self.assertEqual(q.size(), 1)
        self.assertEqual(q.dequeue(), 5)
        with self.assertRaises(IndexError):
            q.dequeue()


if __name__ == '__main__':
    unittest.main()
