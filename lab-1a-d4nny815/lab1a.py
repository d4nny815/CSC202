# CPE 202 Lab 1a
from typing import Optional
from typing import List


# Maybe_List (Optional[List]) is either
# Python List
# or
# None

# Maybe_integer (Optional[int]) is either
# integer
# or
# None

# Maybe_List -> Maybe_integer
def max_list_iter(int_list: Optional[List]) -> Optional[int]:
    """finds the max of a list of numbers and returns the value (not the index)
    If int_list is empty, returns None. If list is None, raises ValueError"""
    if int_list is not None:
        if len(int_list) == 0:
            return None
        else:
            return max(int_list)
    else:
        raise ValueError


# Maybe_List -> Maybe_List
def reverse_list(int_list: Optional[List]) -> Optional[List]:
    """reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""
    if int_list is not None:
        return int_list[::-1]
    else:
        raise ValueError


# Maybe_List -> None
def reverse_list_mutate(int_list: Optional[List]) -> None:
    """reverses a list of numbers, modifying the input list, returns None
   If list is None, raises ValueError"""
    if int_list is not None:
        tmp_list = int_list[::-1]
        for i in range(len(tmp_list)):
            int_list[i] = tmp_list[i]
    else:
        raise ValueError
    return None
