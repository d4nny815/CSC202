from typing import List, Any, Optional


class HashTable:

    def __init__(self, table_size: int):  # can add additional attributes
        self.table_size = table_size  # initial table size
        self.hash_table: List = [None] * table_size  # hash table
        self.num_items = 0  # empty hash table

    def insert(self, key: str, value: Any) -> None:
        """ Inserts an entry into the hash table (using Horner hash function to determine index, 
        and quadratic probing to resolve collisions).
        The key is a string (a word) to be entered, and value is any object (e.g. Python List).
        If the key is not already in the table, the key is inserted along with the associated value
        If the key is is in the table, the new value replaces the existing value.
        When used with the concordance, value is a Python List of line numbers.
        If load factor is greater than 0.5 after an insertion, hash table size should be increased (doubled + 1)."""
        hash_value = self.horner_hash(key)
        # print(hash_value, key)
        item_pair = (key, value)
        already_key = False

        i = 1
        # quad probe to get right index
        while self.hash_table[hash_value] is not None:
            if self.hash_table[hash_value][0] == key:
                already_key = True
                break
            hash_value = (hash_value + i ** 2) % self.table_size
            i += 1

        if already_key:
            # replace current item
            self.hash_table[hash_value] = item_pair
            pass
        else:
            # insert into hash table        
            self.hash_table[hash_value] = item_pair
            self.num_items += 1

        if self.get_load_factor() >= .5:
            # expand table
            old_table = self.hash_table
            self.table_size = self.table_size * 2 + 1
            self.hash_table = [None] * self.table_size
            self.num_items = 0
            for item in old_table:
                if item is not None:
                    self.insert(item[0], item[1])

    def horner_hash(self, key: str) -> int:
        """ Compute and return an integer from 0 to the (size of the hash table) - 1
        Compute the hash value by using Horner’s rule, as described in project specification."""
        h = 0
        n = min(8, len(key))
        for i in range(n):
            h = (31 * h) + ord(key[i])
        return h % self.table_size

    def in_table(self, key: str) -> bool:
        """ Returns True if key is in an entry of the hash table, False otherwise. Must be O(1)."""
        hash_value = self.horner_hash(key)

        i = 1
        while self.hash_table[hash_value] is not None:
            if self.hash_table[hash_value][0] == key:
                return True
            hash_value = (hash_value + i ** 2) % self.table_size
            i += 1

        return False

    def get_index(self, key: str) -> Optional[int]:
        """ Returns the index of the hash table entry containing the provided key. 
        If there is not an entry with the provided key, returns None. Must be O(1)."""
        hash_value = self.horner_hash(key)

        i = 1
        while self.hash_table[hash_value] is not None:
            if self.hash_table[hash_value][0] == key:
                return hash_value

            hash_value = (hash_value + i ** 2) % self.table_size
            i += 1
        return None

    def get_all_keys(self) -> List:
        """ Returns a Python list of all keys in the hash table."""
        my_list = []
        for item in self.hash_table:
            if item is not None:
                my_list.append(item[0])
        return my_list

    def get_value(self, key: str) -> Any:
        """ Returns the value (for concordance, list of line numbers) associated with the key.
        If key is not in hash table, returns None. Must be O(1)."""
        hash_value = self.horner_hash(key)

        i = 1
        while self.hash_table[hash_value] is not None:
            if self.hash_table[hash_value][0] == key:
                return self.hash_table[hash_value][1]
            hash_value = (hash_value + i ** 2) % self.table_size
            i += 1
        return None

    def get_num_items(self) -> int:
        """ Returns the number of entries (words) in the table. Must be O(1)."""
        return self.num_items

    def get_table_size(self) -> int:
        """ Returns the size of the hash table."""
        return self.table_size

    def get_load_factor(self) -> float:
        """ Returns the load factor of the hash table (entries / table_size)."""
        return self.num_items / self.table_size
