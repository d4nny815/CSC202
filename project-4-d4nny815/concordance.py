from typing import Any, List, Optional
from hash_quad import *


class Concordance:

    def __init__(self) -> None:
        """ Starting size of hash table should be 191: self.concordance_table = HashTable(191) """
        self.stop_table: Optional[HashTable] = None  # hash table for stop words
        self.concordance_table: HashTable = HashTable(191)  # hash table for concordance

    def load_stop_table(self, filename: str) -> None:
        """ Read stop words from input file (filename) and insert each word as a key into the stop words hash table.
        Starting size of hash table should be 191: self.stop_table = HashTable(191)
        If file does not exist, raise FileNotFoundError"""

        # assuming its in format "word\n"
        self.stop_table = HashTable(191)
        word_list = []
        with open(filename, 'r', newline='') as file:
            for line_num, line in enumerate(file):
                word = ''
                for char in line:
                    if char.isalpha():
                        word += char
                word_list.append((word, line_num + 1))

        for key, value in word_list:
            self.stop_table.insert(key, value)

    def load_concordance_table(self, filename: str) -> None:
        """ Read words from input text file (filename) and insert them into the concordance hash table, 
        after processing for punctuation, numbers and filtering out words that are in the stop words hash table.
        Do not include duplicate line numbers (word appearing on same line more than once, just one entry for that line)

        Process of adding new line numbers for a word (key) in the concordance:
            If word is in table, get current value (list of line numbers), append new line number, insert (key, value)
            If word is not in table, insert (key, value), where value is a Python List with the line number
        If file does not exist, raise FileNotFoundError """

        # assuming its in format "word\n"
        self.concordance_table = HashTable(191)
        words_and_line_numbers = set()
        with open(filename, 'r') as file:
            for line_number, line in enumerate(file):
                word = ''
                for char in line:
                    if char.isalpha():
                        word += char
                    elif char in ' -':
                        word += ' '
                    else:
                        char = ''
                        continue
                for i in word.split():
                    words_and_line_numbers.add((i.lower(), line_number + 1))

        for word, line_number in words_and_line_numbers:
            if self.stop_table is None:
                continue
            elif self.stop_table.in_table(word):
                continue
            elif self.concordance_table.in_table(word):
                # word already in concord table update its line number, no repeating line numbers
                line_number_list: List = self.concordance_table.get_value(word)
                line_number_list.append(line_number)
                self.concordance_table.insert(word, line_number_list)
            else:
                self.concordance_table.insert(word, [line_number])

        # list = self.concordance_table.get_all_keys()
        # for item in sorted(list):
        #     print(f"key: {item}, val: {self.concordance_table.get_value(item)}")

    def write_concordance(self, filename: str) -> None:
        """ Write the concordance entries to the output file(filename)
        See sample output files for format. """
        list = self.concordance_table.get_all_keys()
        list.sort()
        with open(filename, 'w', newline='') as file:
            for key in list:
                file.write(f"{key}:")
                line_numbers: List = self.concordance_table.get_value(key)
                for line in sorted(line_numbers):
                    file.write(f" {line}")
                file.write("\n")
