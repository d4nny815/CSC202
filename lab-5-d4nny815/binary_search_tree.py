from __future__ import annotations

from typing import Optional, Any, Tuple, List

from queue_array import Queue

# mypy: ignore-errors


class TreeNode:
    def __init__(self, key: Any, data: Any, left: Optional[TreeNode] = None, right: Optional[TreeNode] = None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right

    def __eq__(self, other: object) -> bool:
        if isinstance(other, TreeNode):
            return (self.key == other.key
                    and self.data == other.data
                    and self.left == other.left
                    and self.right == other.right)
        else:
            return False

    def __repr__(self) -> str:
        return "TreeNode({!r}, {!r}, {!r}, {!r})".format(self.key, self.data, self.left, self.right)


class BinarySearchTree:
    def __init__(self, root_node: Optional[TreeNode] = None):  # Returns empty BST
        self.root: Optional[TreeNode] = root_node

    # returns True if tree is empty, else False
    def is_empty(self) -> bool:
        return self.root is None

    # returns True if key is in a node of the tree, else False
    def search(self, key: Any) -> bool:
        if self.is_empty():
            return False
        else:
            return self.search_helper(key, self.root)

    def search_helper(self, key: Any, node: Optional[TreeNode]) -> bool:
        # print(f"node key: {node.key}, key: {key} ")
        if key < node.key:
            if node.left is None:
                # print("Not found")
                return False
            else:
                # print("go left") 
                return self.search_helper(key, node.left)
        elif key > node.key:
            if node.right is None:
                # print("Not found")
                return False
            else:
                # print("go right") 
                return self.search_helper(key, node.right)
        else:
            # print("found")
            return True

    # Inserts new node w/ key and data
    # If an item with the given key is already in the BST,
    # the data in the tree will be replaced with the new data
    # Example creation of node: temp = TreeNode(key, data)
    # On insert, can assume key not already in BST
    def insert(self, key: Any, data: Any = None) -> None:
        if self.is_empty():
            self.root = TreeNode(key, data)
        else:
            self.insert_helper(key, data, self.root, None)

    def insert_helper(self, key: Any, data: Any, node: Optional[TreeNode], parent: Optional[TreeNode]):
        if key < node.key:
            if node.left is None:
                node.left = TreeNode(key, data)
                # print(node.left, "left")
            else:
                # print("go left") 
                self.insert_helper(key, data, node.left, node)
        elif key > node.key:
            if node.right is None:
                node.right = TreeNode(key, data)
                # print(node.right, "right")
            else:
                # print("go right") 
                self.insert_helper(key, data, node.right, node)
        else:  # update key
            node_left = node.left
            node_right = node.right
            if key < parent.key:
                parent.left = TreeNode(key, data, node_left, node_right)
            elif key > parent.key:
                parent.right = TreeNode(key, data, node_left, node_right)

    # returns tuple with min key and associated data in the BST
    # returns None if the tree is empty
    def find_min(self) -> Optional[Tuple[Any, Any]]:
        if self.is_empty():
            return None
        else:
            return self.find_min_helper(self.root)

    def find_min_helper(self, node: Optional[TreeNode]) -> Tuple[Any, Any]:
        if node.left is None:
            return (node.key, node.data)
        else:
            return self.find_min_helper(node.left)

    # returns tuple with max key and associated data in the BST
    # returns None if the tree is empty
    def find_max(self) -> Optional[Tuple[Any, Any]]:
        if self.is_empty():
            return None
        else:
            return self.find_max_helper(self.root)

    def find_max_helper(self, node: Optional[TreeNode]) -> Tuple[Any, Any]:
        if node.right is None:
            return node.key, node.data
        else:
            return self.find_max_helper(node.right)

    # returns the height of the tree
    # if tree is empty, return None
    def tree_height(self) -> Optional[int]:
        if self.is_empty():
            return None
        else:
            return self.tree_height_helper(self.root)

    def tree_height_helper(self, node: Optional[TreeNode]) -> Optional[int]:
        if node is None:
            return -1
        else:
            choices = [self.tree_height_helper(node.left), self.tree_height_helper(node.right)]
            return 1 + max(i for i in choices if i is not None)

    # returns Python list of BST keys representing inorder traversal of BST
    def inorder_list(self) -> List:
        inorder_list: List = []
        if self.is_empty():
            return inorder_list
        else:
            self.inorder_list_helper(self.root, inorder_list)
            return inorder_list

    def inorder_list_helper(self, node: Optional[TreeNode], inorder_list: List):
        if node.left is not None:
            self.inorder_list_helper(node.left, inorder_list)
        inorder_list.append(node.key)
        if node.right is not None:
            self.inorder_list_helper(node.right, inorder_list)

    # returns Python list of BST keys representing preorder traversal of BST
    def preorder_list(self) -> List:
        preorder_list: List = []
        if self.is_empty():
            return preorder_list
        else:
            self.preorder_list_helper(self.root, preorder_list)
            return preorder_list

    def preorder_list_helper(self, node: Optional[TreeNode], preorder_list: List):
        preorder_list.append(node.key)
        if node.left is not None:
            self.preorder_list_helper(node.left, preorder_list)
        if node.right is not None:
            self.preorder_list_helper(node.right, preorder_list)

    # returns Python list of BST keys representing level-order traversal of BST
    # You MUST use your queue_array data structure from lab 3 to implement this method
    def level_order_list(self) -> List:
        level_list: List = []
        q = Queue(25000)  # Don't change this!
        if self.is_empty():
            return level_list
        else:
            q.enqueue(self.root)
            while not q.is_empty():
                item: TreeNode = q.dequeue()
                level_list.append(item.key)
                if item.left is not None:
                    q.enqueue(item.left)
                if item.right is not None:
                    q.enqueue(item.right)
            return level_list
