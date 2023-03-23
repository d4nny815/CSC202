from typing import Any, List

class MinHeap:

    def __init__(self, capacity: int = 50):
        """Constructor creating an empty heap with default capacity = 50 but allows heaps of other capacities to be created."""
        self.heap: List = [0]*(capacity+1)     # index 0 not used for heap
        self.num_items = 0                     # empty heap


    def enqueue(self, item: Any) -> None:
        """inserts "item" into the heap
        Raises IndexError if there is no room in the heap"""
        if self.is_full():
            raise IndexError
        else:
            self.num_items += 1  
            self.heap[self.num_items ] = item  # add item to end of heap
            self.perc_up(self.num_items)  # move to item up the heap if needed

    def peek(self) -> Any:
        """returns root of heap (highest priority) without changing the heap
        Raises IndexError if the heap is empty"""
        if self.is_empty():
            raise IndexError
        else:
            return self.heap[1]

    def dequeue(self) -> Any:
        """returns item at root (highest priority) - removes it from the heap and restores the heap property
           Raises IndexError if the heap is empty"""
        if self.is_empty():
            raise IndexError
        else:
            item = self.heap[1]  # store item at top of heap
            self.heap[1] = self.heap[self.num_items]  # replace top with item at bottom
            self.num_items -= 1
            self.perc_down(1)  # perc down item moved to top
            return item
        
        

    def contents(self) -> List:
        """returns a list of contents of the heap in the order it is stored internal to the heap.
        (This may be useful for in testing your implementation.)
        If heap is empty, returns empty list []"""
        return self.heap[1:self.num_items + 1]
                

    def build_heap(self, alist: List) -> None:
        """Discards the items in the current heap and builds a heap from
        the items in alist using the bottom up method.
        If the capacity of the current heap is less than the number of
        items in alist, the capacity of the heap will be increased to accommodate the items in alist"""
        # should remain same capacity if not needed more
        if len(alist) > self.capacity():
            # add space needed(difference of alist and current capacity)
            self.heap.append([0]*(len(alist) - self.capacity()))  
        i = len(alist) // 2  # index to middle item
        self.num_items = len(alist)  # update num of items to items in alist
        # heap remains current capacity add alist to current heap filling rest with 0
        self.heap = [0] + alist + [0 for _ in range(self.capacity() - len(alist))]
        while i > 0:
            self.perc_down(i)
            i -= 1
            

    def is_empty(self) -> bool:
        """returns True if the heap is empty, false otherwise"""
        return self.num_items == 0

    def is_full(self) -> bool:
        """returns True if the heap is full, false otherwise"""
        return self.num_items == self.capacity()

    def capacity(self) -> int:
        """This is the maximum number of a entries the heap can hold, which is
        1 less than the number of entries that the array allocated to hold the heap can hold"""
        return len(self.heap) - 1
    
    def size(self) -> int:
        """the actual number of elements in the heap, not the capacity"""
        return self.num_items

    def perc_down(self,i: int) -> None:
        """where the parameter i is an index in the heap and perc_down moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes."""
        done = False
        while not done and 2*i <= self.size(): # at least one child
            c1 = 2*i    # Child 1
            c2 = c1+1   # Child 2
            if c2 <= self.size() and self.heap[c1] > self.heap[c2]: # Two children and c2 is smaller
                if self.heap[i] > self.heap[c2]:
                    self.heap[i], self.heap[c2] = self.heap[c2], self.heap[i]
                    i = c2
                else:
                    done = True
            else:   # One child, or c1 is smaller
                if self.heap[i] > self.heap[c1]:
                    self.heap[i], self.heap[c1] = self.heap[c1], self.heap[i]
                    i = c1
                else:
                    done = True

    def perc_up(self,i: int) -> None:
        """where the parameter i is an index in the heap and perc_up moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes."""
        parent = i // 2
        while parent > 0 and self.heap[i] < self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent
            parent = i // 2

    def heap_sort_ascending(self, alist: List) -> None:
        """perform heap sort on input alist in ascending order
        This method will discard the current contents of the heap, build a new heap using
        the items in alist, and mutate (change contents of) alist to put the items in ascending order"""
        self.build_heap(alist)  
        size = self.size()  # get original size of heap
        while self.size() > 0:  
            min = self.dequeue()  # get min value at top of heap
            alist[(size - (self.size() + 1))] = min  # alter original list at index currently working on
