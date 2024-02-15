
""" CSCI204 Stack Lab
Last Modified by: Prof. Fuchsberger, March, 2021
Do not change this file.
"""

from stack import MyStack
from infix2postfix import Infix2postfix, IllegalExpressionException, ParensMismatchException

def menu():
    print("\nLab 6 Testprogram. Type one of the following:")
    print( "(A) - Will test your stack functions" )
    print( "(B) - Will test a series of infix to postfix expressions" )
    print( "(any infix expression) - Will convert your infix to postfix notation" )
    print( "Hit Enter to end this program.\n" )

def test_stack():

    """ Test various stack functions """
    num_stack = MyStack()

    if not num_stack.is_empty():
        print("Starting stack should have been empty but isn't.")
    else:
        print("Stack empty test fine.")

    num_stack.push("12")

    if not num_stack.top() == "12":
        print("Top of stack should be 12 but was", num_stack.top())
    else:
        print("Top of stack should be 12 and it was", num_stack.top())

    v = num_stack.pop()
    print("Top of stack popped, the value should be 12 ", v, end = "")
    print( " => ", v == "12" )

    for i in range(10):
        print("Push ", i, " on to the stack.")
        num_stack.push(str(i))     # the stack should grow as it is designed to

    print("Test is_empty and pop...")
    i = 9
    while num_stack.is_empty() == False:
        value = num_stack.pop()
        print("The value of stack top is ", value, end = "")
        print(" the value should be ", i, " => ", value == str(i))
        i = i - 1

    print("\nAll Stack Tests have been completed.\n")

def test_expression( infix, expected = "?" ):
    try:
        my_expression = Infix2postfix()

        postfix = my_expression.translate( infix )
        result = my_expression.evaluate_expression( postfix )
        if expected == "?":
            print_header()
        print("{:27} | {:27} | {:8} | {:8}".format(infix, postfix, result, expected))

    except ( IllegalExpressionException, ParensMismatchException ):
        print( "{:27} | Mismatched Parenthesis, or illegal expression".format(infix) )

def test_expressions():

    print("\nTesting a series of expressions:\n")

    expressions = ['( 3 + 4 )', 
        '3    - ( 2 - 7 )',
        '8 * (   4 - 2 )',
        '  4 - ( 2 / 5 )',
        '( 5 / 3 ) * 9',
        '( 6 * 2 + 1 )',
        '7 + ( 6 - 3 ) / 2',
        '7   * ( 6 - 3 ) / 2',
        '( 3 + 8 ) * 5',
        '6 * ( 2 + 5 ) - 8',
        '( 4 + 2 ) * 7 / 3',
        '( 6 + 2 ) * ( 9 + 1 )',
        '( 123   +   33 ) * 8 + 61']

    results = ['7', '8', '16', '4', '9', '13', '8', '10', '55', '34', '14', '80', '1309']

    print_header()
    for i in range(len(expressions)):
        test_expression(expressions[i], results[i])


    print("\nAll Expression Tests have been successfull.\n")

def print_header():
    print("{:27} | {:27} | {:8} | {:8}".format("Infix", "Postfix", "Result", "Expected"))