
""" CSCI204 Stack Lab
Last Modified by: Prof. Fuchsberger, March, 2021
Do not change this file.
"""

from tests import menu, test_stack, test_expression, test_expressions

menu()
infix = input( ">>> " )

while not infix == "":
    if infix == "a" or infix == "A":
        test_stack()

    elif infix == "b" or infix == "B":
        test_expressions()

    else:
        test_expression(infix, "?")

    menu()
    infix = input( ">>> " )

print()