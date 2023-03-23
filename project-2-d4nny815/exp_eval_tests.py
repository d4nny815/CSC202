# Start of unittest - add to completely test functions in exp_eval!

import unittest
from exp_eval import *

class test_expressions(unittest.TestCase):

    def test_postfix_eval_01a(self) -> None:
        self.assertAlmostEqual(postfix_eval("3 5 +"), 8)

    def test_postfix_eval_01b(self) -> None:
        self.assertAlmostEqual(postfix_eval("8 1 >>"), 4)
        self.assertAlmostEqual(postfix_eval("8 1 <<"), 16)

    def test_postfix_eval_01c(self) -> None:
        self.assertAlmostEqual(postfix_eval("8 2 **"), 64)

    def test_postfix_eval_01d(self) -> None:
        self.assertAlmostEqual(postfix_eval("18.5 -2 *"), -37)
        self.assertAlmostEqual(postfix_eval("-18.52 -0.78 +"), -19.3)
        
    def test_postfix_eval_02(self) -> None:
        try:
            postfix_eval("blah")
            self.fail()     # pragma: no cover
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Invalid token")

    def test_postfix_eval_03a(self) -> None:
        try:
            postfix_eval("4 +")
            self.fail()     # pragma: no cover
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")

    def test_postfix_eval_03b(self) -> None:
        try:
            postfix_eval("")
            self.fail()     # pragma: no cover
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")

    def test_postfix_eval_04(self) -> None:
        try:
            postfix_eval("1 2 3 +")
            self.fail()     # pragma: no cover
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Too many operands")
            
    def test_postfix_eval_05(self) -> None:
        try:
            postfix_eval("8 0 / 4 +")
            self.fail()     # pragma: no cover
        except ValueError as e:
            self.assertEqual(str(e), "Can't divide by 0")
            
    def test_postfix_eval_06(self) -> None:
        try:
            postfix_eval("8.0 1 >>")
            self.fail()     # pragma: no cover
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Illegal bit shift operand")

    def test_infix_to_postfix_01a(self) -> None:
        self.assertEqual(infix_to_postfix("6 - 3"), "6 3 -")
        self.assertEqual(infix_to_postfix("6"), "6")
        self.assertEqual(infix_to_postfix("32 >> 2 >> 1"), "32 2 >> 1 >>")

    def test_infix_to_postfix_01b(self) -> None:
        self.assertEqual(infix_to_postfix("32 >> 2 << 1"), "32 2 >> 1 <<")

    def test_infix_to_postfix_01c(self) -> None:
        self.assertEqual(infix_to_postfix("3 ** 2 ** 2"), "3 2 2 ** **")

    def test_infix_to_postfix_02(self) -> None:
        self.assertEqual(infix_to_postfix("( 5 - 3 ) * 4"), "5 3 - 4 *")
        self.assertEqual(infix_to_postfix("3 + 4 * 2 / ( 1 - 5 ) ** 2 ** 3"), "3 4 2 * 1 5 - 2 3 ** ** / +")

    def test_infix_to_postfix_03(self) -> None:
        self.assertEqual(infix_to_postfix("70 - -3 * 10"), "70 -3 10 * -")

    def test_infix_to_postfix_04(self) -> None:
        self.assertEqual(infix_to_postfix("70.52 - 3.5 * 10.05"), "70.52 3.5 10.05 * -")

    def test_infix_to_postfix_05(self) -> None:
        self.assertEqual(infix_to_postfix("-70.52 - 3.5 * 10.05"), "-70.52 3.5 10.05 * -")

    def test_prefix_to_postfix(self) -> None:
        self.assertEqual(prefix_to_postfix("* - 3 / 2 1 - / 4 5 6"), "3 2 1 / - 4 5 / 6 - *")

    def test_init(self) -> None:
        stack = Stack(5)
        self.assertEqual(stack.items, [None]*5)
        self.assertEqual(stack.capacity, 5)

        stack = Stack(5, [1, 2])
        self.assertEqual(stack.items[0:2], [1, 2])
        self.assertEqual(stack.capacity, 5)

        with self.assertRaises(IndexError):
            Stack(5, [1, 2, 3, 4, 5, 6])

    def test_eq(self) -> None:
        stack1 = Stack(5)
        stack2 = Stack(5)
        stack3 = Stack(10)
        stack4 = Stack(5,[1, 2])
        self.assertEqual(stack1, stack2)
        self.assertNotEqual(stack1, stack3)
        self.assertNotEqual(stack1, stack4)
        self.assertFalse(stack1.__eq__(None))

    def test_repr(self) -> None:
        stack = Stack(5, [1, 2])
        self.assertEqual(stack.__repr__(), "Stack(5, [1, 2])")
    
    def test_isempty(self) -> None:
        stack1 = Stack(5)
        stack2 = Stack(5, [1, 2, 3])
        self.assertTrue(stack1.is_empty())
        self.assertFalse(stack2.is_empty())
        return
    
    def test_isfull(self) -> None:
        stack1 = Stack(5, [1, 2, 3, 4, 5])
        stack2 = Stack(5)
        self.assertTrue(stack1.is_full())
        self.assertFalse(stack2.is_full())
        return
    
    def test_push(self) -> None:
        stack1 = Stack(5, [1, 2, 3, 4])
        stack1.push(5)
        self.assertEqual(stack1.peek(), 5)
        with self.assertRaises(IndexError):
            stack1.push(1)
        return
    
    def test_pop(self) -> None:
        stack1 = Stack(5, [1, 2])
        self.assertEqual(stack1.pop(), 2)
        self.assertEqual(stack1.pop(), 1)
        with self.assertRaises(IndexError):
            stack1.pop()
        return
    
    def test_peek(self) -> None:
        stack1 = Stack(5, [1, 2])
        stack2 = Stack(5)
        self.assertEqual(stack1.peek(), 2)
        with self.assertRaises(IndexError):
            stack2.peek()
        return
    
    def test_size(self) -> None:
        stack1 = Stack(5, [1, 2])
        self.assertEqual(stack1.size(), 2)
        return
if __name__ == "__main__":
    unittest.main()
