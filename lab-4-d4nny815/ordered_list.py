from __future__ import annotations
from typing import Optional, Any, List

class Node:
    """Node for use with doubly-linked list"""
    def __init__(self, item: Any):
        self.item = item  # item held by Node
        self.next: Node = self  # reference to next Node, init to this Node
        self.prev: Node = self  # reference to previous Node, init to this Node
    
        

class OrderedList:
    """A doubly-linked ordered list of integers, 
    from lowest (head of list, sentinel.next) to highest (tail of list, sentinel.prev)"""
    def __init__(self) -> None:
        """Use only a sentinel Node. No other instance variables"""
        self.sentinel: Node = Node(None)    # Empty linked list, just sentinel Node
        self.sentinel.next = self.sentinel  # Initialize next to sentinel
        self.sentinel.prev = self.sentinel  # Initialize prev to sentinel

    def __eq__(self, other: object) -> bool:
        lists_equal = True
        if not isinstance(other, OrderedList):
            lists_equal = False
        else:
            s_cur = self.sentinel.next
            o_cur = other.sentinel.next
            while s_cur != self.sentinel and o_cur != other.sentinel:
                if s_cur.item != o_cur.item:
                    lists_equal = False
                s_cur = s_cur.next
                o_cur = o_cur.next
            if s_cur != self.sentinel or o_cur != other.sentinel:
                lists_equal = False
        return lists_equal

    def is_empty(self) -> bool:
        """Returns back True if OrderedList is empty"""
        return self.sentinel.next is self.sentinel and self.sentinel.prev is self.sentinel # only sentinel node

    def add(self, item: Any) -> None:
        """Adds an item to OrderedList, in the proper location based on ordering of items
        from lowest (at head of list) to highest (at tail of list)
        If item is already in list, do not add again (no duplicate items)"""
        pointer = self.sentinel.next  # pointer to which node its on
        while pointer is not self.sentinel and item > pointer.item:
            pointer = pointer.next
        if item != pointer.item:
            temp = Node(item)
            temp.next = pointer
            temp.prev = pointer.prev
            pointer.prev.next = temp
            pointer.prev = temp
            

    def remove(self, item: Any) -> bool:
        """Removes an item from OrderedList. If item is removed (was in the list) returns True
        If item was not removed (was not in the list) returns False"""
        pointer = self.sentinel.next
        while pointer is not self.sentinel and item > pointer.item:
            pointer = pointer.next
        if pointer.item == item:
            pointer.prev.next = pointer.next
            pointer.next.prev = pointer.prev
            return True
        else:
            return False

    def index(self, item: Any) -> Optional[int]:
        """Returns index of an item in OrderedList (assuming head of list is index 0).
        If item is not in list, return None"""
        pointer = self.sentinel.next
        ind = 0
        while pointer is not self.sentinel and item > pointer.item:
            pointer = pointer.next
            ind += 1
        if pointer is not self.sentinel and pointer.item == item:
            return ind
        else:
            return None

    def pop(self, index: int) -> Any:
        """Removes and returns item at index (assuming head of list is index 0).
        If index is negative or >= size of list, raises IndexError"""
        if index < 0 or index >= self.size():
            raise IndexError
        else:
            pointer = self.sentinel.next
            ind = 0
            while pointer is not self.sentinel and index > ind:
                pointer = pointer.next
                ind += 1
            item = pointer.item
            pointer.prev.next = pointer.next
            pointer.next.prev = pointer.prev
            return item

    def search(self, item: Any) -> bool:
        """Searches OrderedList for item, returns True if item is in list, False otherwise - USE RECURSION"""
        return self.search_helper(self.sentinel.next, item)
        
    def search_helper(self, node: Node, item: Any) -> bool:
        if node.item == item:
            return True
        elif node is not self.sentinel:
            return self.search_helper(node.next, item)
        else:
            return False
            

    def python_list(self) -> List:
        """Return a Python list representation of OrderedList, from head to tail
        For example, list with integers 1, 2, and 3 would return [1, 2, 3]"""
        py_list = []
        current = self.sentinel.next
        while current is not self.sentinel:
            py_list.append(current.item)
            current = current.next
        return py_list

    def python_list_reversed(self) -> List:
        """Return a Python list representation of OrderedList, from tail to head, USING RECURSION
        For example, list with integers 1, 2, and 3 would return [3, 2, 1]"""
        py_list: List = []
        self.python_list_reversed_helper(self.sentinel.prev, py_list)
        return py_list
    
    def python_list_reversed_helper(self, node: Node, py_list: List) -> None:
        if node is not self.sentinel:
            py_list.append(node.item)
            self.python_list_reversed_helper(node.prev, py_list)

    def size(self) -> int:
        """Returns number of items in the OrderedList - USE RECURSION"""
        return self.size_helper(self.sentinel.next)
    
    def size_helper(self, node: Node) -> int:
        if node is self.sentinel:
            return 0
        else:
            return 1 + self.size_helper(node.next)
