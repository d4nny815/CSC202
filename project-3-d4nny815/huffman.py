from __future__ import annotations
from typing import List, Optional
class HuffmanNode:
    def __init__(self, char_ascii: int, freq: int, left: Optional[HuffmanNode] = None, right: Optional[HuffmanNode] = None):
        self.char_ascii = char_ascii    # stored as an integer - the ASCII character code value
        self.freq = freq                # the frequency associated with the node
        self.left = left                # Huffman tree (node) to the left!
        self.right = right              # Huffman tree (node) to the right

    def __repr__(self) -> str:
        return f'HuffmanNode({self.char_ascii}, {self.freq}, {self.left}, {self.right}) '
    
    def __lt__(self, other: HuffmanNode) -> bool:
        return comes_before(self, other)


def comes_before(a: HuffmanNode, b: HuffmanNode) -> bool:
    """Returns True if tree rooted at node a comes before tree rooted at node b, False otherwise"""
    if a.freq == b.freq:
        return a.char_ascii < b.char_ascii  # go by char value if equal freq
    else:
        return a.freq < b.freq  


def combine(a: HuffmanNode, b: HuffmanNode) -> HuffmanNode:
    """Creates a new Huffman node with children a and b, with the "lesser node" on the left
    The new node's frequency value will be the sum of the a and b frequencies
    The new node's char value will be the lower of the a and b char ASCII values"""       
    # print(a)
    # print(b)
    if a < b:
        left = a
        right = b
    else:
        left = b
        right = a
    return HuffmanNode(min(b.char_ascii, a.char_ascii), a.freq + b.freq, left, right)


def cnt_freq(filename: str) -> List:
    """Opens a text file with a given file name (passed as a string) and counts the
    frequency of occurrences of all the characters within that file
    Returns a Python List with 256 entries - counts are initialized to zero.
    The ASCII value of the characters are used to index into this list for the frequency counts"""
    list = [0] * 256  
    string = ''
    with open(filename, 'r') as file:
        for char in file:
            string += char  # add every character to a string
    for char in string:  
        list[ord(char)] += 1 
    return list

def create_huff_tree(char_freq: List) -> Optional[HuffmanNode]:
    """Input is the list of frequencies (provided by cnt_freq()).
    Create a Huffman tree for characters with non-zero frequency
    Returns the root node of the Huffman tree. Returns None if all counts are zero."""
    if max(char_freq) == 0:  # all counts are zero
        return None
    else:    
        list: List = []
        for char_value, freq in enumerate(char_freq): 
            if freq > 0:  
                list.append(HuffmanNode(char_value, freq))  # add huffNode for char that appear more than once
        while len(list) > 1:
            a = list.pop(list.index(min(list)))  # pop the 2 min huffman node 
            b = list.pop(list.index(min(list))) 
            list.append(combine(a, b)) #append new HuffanNode with the 2 least freq 
        return list.pop()
        


def create_code(node: Optional[HuffmanNode]) -> List:
    """Returns an array (Python list) of Huffman codes. For each character, use the integer ASCII representation
    as the index into the array, with the resulting Huffman code for that character stored at that location.
    Characters that are unused should have an empty string at that location"""
    if node is None:
        return []
    else:
        list = [''] * 256  # list to store code to get to each char
        create_code_helper(node, '', list)
    return list

def create_code_helper(node: HuffmanNode, code: str, list: List) -> None:
    if node.left is None and node.right is None: 
        list[node.char_ascii] = code  # reach end of node and store code to get to char
    if node.left is not None:
        left_code = code + '0'
        create_code_helper(node.left, left_code, list)
    if node.right is not None:
        right_code = code + '1'
        create_code_helper(node.right, right_code, list)
    return



def create_header(freqs: List) -> str:
    """Input is the list of frequencies (provided by cnt_freq()).
    Creates and returns a header for the output file
    Example: For the frequency list asscoaied with "aaabbbbcc, would return “97 3 98 4 99 2” """
    string = ''
    for char_value, char_freq in enumerate(freqs):
        if char_freq > 0:
            string += f'{char_value} {char_freq} '
    return string.rstrip()  # remove empty space from right


def huffman_encode(in_file: str, out_file: str) -> None:
    """Takes inout file name and output file name as parameters
    Uses the Huffman coding process on the text from the input file and writes encoded text to output file
    Take not of special cases - empty file and file with only one unique character"""
    freqs = cnt_freq(in_file)
    code = create_code(create_huff_tree(freqs))
    print(code)
    
    with open(in_file, 'r') as input_file:
        lines = input_file.readlines() 
        
    with open(out_file, 'w', newline='') as output_file:
        output_file.write(create_header(freqs) + '\n')
        for line in lines:
            for char in line:
                output_file.write(code[ord(char)])
   
   
def parse_header(headerstring: str) -> List:
    freq_list = [0] * 256
    space = True
    string = ''
    for ind, char in enumerate(headerstring):
        string += char
        if char == ' ' or ind == len(headerstring) - 1:
            if space:
                space = not space
            else:
                string = string.rstrip()
                index, freq = string.split(' ')
                # print(index, "ind", freq, "freq")
                freq_list[int(index)] = int(freq)
                string = ''
                space = not space
    return freq_list            
                
def huffman_decode(encoded_file: str, decode_file: str) -> None:
    try:
        with open(encoded_file, 'r') as file:
            header = file.readline()
            code = file.readline()
        huff_tree = create_huff_tree(parse_header(header.rstrip()))
        pointer = huff_tree
        with open(decode_file, 'w', newline='') as file:
            for char in code:
                if char == '1':
                    if pointer is not None:
                        pointer = pointer.right
                elif char == '0':
                    if pointer is not None:
                        pointer = pointer.left
                if pointer is not None:        
                    if pointer.right is None and pointer.left is None:
                        file.write(chr(pointer.char_ascii))
                        pointer = huff_tree    
    except:
        raise FileNotFoundError

        
