# ~~~~~~~~~~~~~~~~~~~~~~assert~~~~~~~~~~~~~~~~~~~~~
# helps promote modular code Test Driven Development TDD
# def adder(x, y):
#     """Add two numbers together"""

#     return x + y


# assert adder(2, 5) == 7
# assert adder(2, 7) == 10, "expected 2+7 to be 10"
# # won't run b/c ^ failed and raised an assertion error with break
# assert adder(2, 3) == 5

# can run without assert running, in terminal (but not ipy), python -O file.py
# assert is a statement, not a function, not passing arguments, statement to 'assert' (evaluate), and then an error string

# ~~~~~~~~~~~~~~~~~~~~~~~~doc tests~~~~~~~~~~~~~~~~~~~~~~~~~
# run in py, not ipy
# not a 'test' but an example of how it should work
# in py, from app import adder to play and test

# def adder(x, y):
#     """
#     Add two numbers together
#     >>> adder(3,5)
#     8
#     >>> adder(-1,50)
#     49
#     """

#     return x + y + 1

#~~~~~~~~~~~~~~~~~~~~~~~~~unittest~~~~~~~~~~~~~~~~~~~~
#bundle of tests
#starts with test_descriptivename
#python -m unittest NAME_OF_FILE runs all cases


# from unittest import TestCase

# def adder(x, y):
#     """
#     Add two numbers together
#     >>> adder(3,5)
#     8
#     >>> adder(-1,50)
#     49
#     """

#     return x + y + 1


