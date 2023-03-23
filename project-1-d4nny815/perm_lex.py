from typing import List


# string -> List of strings
# Returns list of permutations for input string
# e.g. 'ab' -> ['ab', 'ba']; 'a' -> ['a']; '' -> []
def perm_gen_lex(str_in: str) -> List:
    """Returns list of permutations for input string"""
    if len(str_in) == 1:
        return [str_in]  # base case
    else:
        list = []
        for ind, val in enumerate(str_in):  # loop through removed char and simplier strings
            for smaller in perm_gen_lex(str_in[:ind] + str_in[ind + 1:]):  # loop through simplier strings
                # str_in[:ind]+str_in[ind+1:] -> simplier string by removing first char
                list.extend([val + smaller])  # add smaller permutations to list
        return list
