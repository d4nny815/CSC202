from __future__ import annotations
from typing import Optional, Any, Tuple

# NodeList is
# None or
# Node(value, rest), where rest is the rest of the NodeList
class Node:
    def __init__(self, value: Any, rest: Optional[Node]):
        self.value = value
        self.rest = rest

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Node):
            return (self.value == other.value
            and self.rest == other.rest
            )
        else:
            return False

    def __repr__(self) -> str:
        return ("Node({!r}, {!r})".format(self.value, self.rest))

# a StrList is one of
# - None, or
# - Node(string, StrList)

# StrList -> string
# Returns first (as determined by Python compare) string in StrList
# If StrList is empty (None), return None
# Must be implemented recursively
def first_string(strlist: Optional[Node]) -> Optional[str]:
    if strlist is None: # empty list
        return None
    if strlist.rest is None: # base case
        return strlist.value
    else: 
        least = first_string(strlist.rest) # get the last value in list, recursively
        if least > strlist.value:
            least = strlist.value
        return least





# StrList -> (StrList, StrList, StrList)
# Returns a tuple with 3 new StrLists,
# the first one with strings from the input list that start with a vowel,
# the second with strings from the input list that start with a consonant,
# the third with strings that don't start with an alpha character
# Must be implemented recursively
def split_list(strlist: Optional[Node]) -> Tuple[Optional[Node], Optional[Node], Optional[Node]]:
    
    if strlist is None:
        return None, None, None # base case for start of Node
    else:
        vowels = "aeiouAEIOU"
        consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
        
        item = split_list(strlist.rest)
        first_letter = strlist.value[0] # get the first character
        if first_letter in vowels:
            return (Node(strlist.value, item[0]), item[1], item[2]) # add node to tuple pointing to previous tuple, not changing other elements
        elif first_letter in consonants:
            return (item[0], Node(strlist.value, item[1]), item[2])
        else:
            return (item[0], item[1], Node(strlist.value, item[2]))
    

# strlist = Node("xyz", Node("Abc", Node("49ers", None)))
# print(split_list(strlist))
