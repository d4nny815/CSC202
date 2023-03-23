from typing import Any, Tuple, List

class MyHashTable:

    def __init__(self, table_size: int = 11):
        self.table_size = table_size
        self.hash_table: List = [[] for _ in range(table_size)] # List of lists implementation
        self.num_items = 0
        self.num_collisions = 0

    def insert(self, key: int, value: Any) -> None:
        """Takes a key, and an item.  Keys are valid Python non-negative integers.
        If key is negative, raise ValueError exception
        The function will insert the key-item pair into the hash table based on the
        hash value of the key mod the table size (hash_value = key % table_size)"""
        if key < 0:
            raise ValueError
        else:
            hash_value = self.hash(key)
            item_pair = (key, value)
            # print(item_pair)
            already_key = False
            
            for i, pair in enumerate(self.hash_table[hash_value]): # check if key already exist
                if pair[0] == key:  
                    self.hash_table[hash_value][i] = item_pair  # replace existing pair with new pair
                    already_key = True  # flag that a key already existed
                    self.num_items -= 1  # decrease item counted as it'll be added back later
            
            # print("len:", len(self.hash_table[hash_value]))
            if len(self.hash_table[hash_value]) >= 1 and not already_key:
                  
                # more than 1 item is at hash value and item wasnt replaced
                self.num_collisions += 1
                
            if not already_key:  
                self.hash_table[hash_value].append(item_pair)  # add new pair if a new key
                # print(self.hash_table[hash_value])
                
            self.num_items += 1
                
            # add resize for load factor
            if self.load_factor() > 1.5:
                print("resize")
                old_table = self.hash_table
                self.hash_table = [[] for _ in range(self.table_size *  2 + 1)]
                self.table_size = len(self.hash_table)
                self.num_items = 0
                for item in old_table:
                    for pair in item:
                        self.insert(pair[0], pair[1])    
            # print(self.hash_table)
            return

    def hash(self, key: int) -> int:
        return key % self.table_size

    def get_item(self, key: int) -> Any:
        """Takes a key and returns the item from the hash table associated with the key.
        If no key-item pair is associated with the key, the function raises a LookupError exception."""
        hash_value = self.hash(key)
        
        for pair in self.hash_table[hash_value]:
            if pair[0] == key:
                return pair[1]
            
        raise LookupError
        
    def remove(self, key: int) -> Tuple[int, Any]:
        """Takes a key, removes the key-item pair from the hash table and returns the key-item pair.
        If no key-item pair is associated with the key, the function raises a LookupError exception.
        (The key-item pair should be returned as a tuple)"""    
        hash_value = self.hash(key)
        
        for i in range(len(self.hash_table[hash_value])):
            if self.hash_table[hash_value][i][0] == key:
                self.num_items -= 1
                return self.hash_table[hash_value].pop(i)
        raise LookupError

    def load_factor(self) -> float:
        """Returns the current load factor of the hash table"""
        return self.num_items / self.table_size

    def size(self) -> int:
        """Returns the number of key-item pairs currently stored in the hash table"""
        return self.num_items

    def collisions(self) -> int:
        """Returns the number of collisions that have occurred during insertions into the hash table"""
        return self.num_collisions

