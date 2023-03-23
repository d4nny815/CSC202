from stack_array import Stack

# You should not change this Exception class!
class PostfixFormatException(Exception):
    pass

# helper functions
def is_number(num: str) -> bool:  
    try:
        complex(num)
        return True
    except:
        return False
    
def is_float(num: str) -> bool:
    x = num.replace('.', '', 1)
    if x == num:
        return False
    return True


def postfix_eval(input_str: str) -> int:
    """Evaluates a postfix expression"""
    """Input argument:  a string containing a postfix expression where tokens 
    are space separated.  Tokens are either operators + - * / ** << >> or numbers (integers or floats)
    Returns the result of the expression evaluation. 
    Raises an PostfixFormatException if the input is not well-formed"""
    stack = Stack(30)
    pointer = ''
    if input_str.isalpha():  # expression contains and invalid operator or operand
        raise(PostfixFormatException('Invalid token'))
    if len(input_str) < 5:  # expression does not contain sufficient operands 
        raise(PostfixFormatException('Insufficient operands'))  
    
    for ind, val in enumerate(input_str):
        pointer += val 
        if val == ' ' or ind == (len(input_str) - 1):
            pointer = pointer.rstrip()  # remove white space from expression
            if is_number(pointer):  # value is encountered
                stack.push(pointer)
            else:  # operator is encountered
                    operand1 = stack.pop()
                    operand2 = stack.pop()
                    if pointer == '/' and operand1 == '0':
                        raise(ValueError("Can't divide by 0"))
                    elif pointer in ['<<', '>>'] and (is_float(operand1) or is_float(operand2)):
                        raise(PostfixFormatException("Illegal bit shift operand")) 
                    stack.push(eval(f'{operand2} {pointer} {operand1}'))
            pointer = '' 
    if stack.size() > 1:  # leftover operands
        raise(PostfixFormatException("Too many operands"))
    return stack.pop()


def infix_to_postfix(input_str: str) -> str:
    """Converts an infix expression to an equivalent postfix expression"""
    """Input argument:  a string containing an infix expression where tokens are 
    space separated.  Tokens are either operators + - * / ** << >> or numbers (integers or floats)
    Returns a String containing a postfix expression """
    stack = Stack(30)
    rpn = ''
    pointer = ''
    operators = {'<<': 3, '>>': 3, '**': 2, '*': 1, '/': 1, '+': 0, '-': 0, '(': -1, ')': -1}  # operators with their precedance value
    
    for ind, val in enumerate(input_str):
        pointer += val
        if val == ' ' or ind == (len(input_str) - 1):
            pointer = pointer.rstrip() 
            if is_number(pointer):  # encounter digit
                rpn += f'{pointer} '
            elif pointer == '(' or pointer == ')': # encounter parenthesis
                if pointer == '(':
                    stack.push(pointer)
                elif pointer == ')':
                    while stack.peek() != '(':
                        rpn += f'{stack.pop()} ' 
                    stack.pop()
            else: # encounter an operator
                if not stack.is_empty():
                    o1 = operators[f'{pointer}']
                    o2 = operators[f'{stack.peek()}']  
                    if ((o1 <= o2 and pointer != '**') or 
                        (o1 < o2 and pointer == '**')):
                        rpn += f'{stack.pop()} '     
                stack.push(pointer)
            pointer = ''  # reset pointer
            
    while stack.num_items != 0:  # empty stack into rpn string
        rpn += f'{stack.pop()} '
    return rpn.rstrip()

print(infix_to_postfix("( 6 / 3 ) - 2 * 4 + 1"))

def prefix_to_postfix(input_str: str) -> str:
    """Converts a prefix expression to an equivalent postfix expression"""
    """Input argument: a string containing a prefix expression where tokens are 
    space separated.  Tokens are either operators + - * / ** << >> or numbers (integers or floats)
    Returns a String containing a postfix expression(tokens are space separated)"""
    new_str = input_str[::-1]
    stack = Stack(30)
    pointer = ''
    
    for ind, val in enumerate(new_str):
        pointer += val
        if val == ' ' or ind == (len(input_str) - 1):
            pointer = pointer.rstrip()
            if is_number(pointer):
                stack.push(pointer)
            else:
                op1 = stack.pop()
                op2 = stack.pop()
                stack.push(f'{op1} {op2} {pointer}')
            pointer = ''      
    return stack.pop()



