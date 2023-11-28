#All programming languages support unit testing, and most languages contain a built-in unit testing framework.
#Python is no exception with its "unittest" module:

#https://docs.python.org/3/library/unittest.html

#Use the below Python code and improve it by writing unit tests to it by using the "unittest" feature.

#Code to write the tests for:

#---------------------------------
import unittest

def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

def power(x, y):
    """Calculate x raised to the power y without using math.pow."""
    result = 1
    for _ in range(int(y)):
        result *= x
    return result

print(add(5,4))       # --> 9
print(multiply(3,4))  # --> 12
print(power(2,8))     # --> 256
print(power(2,-2))
#---------------------------------
class TestStringMethods(unittest.TestCase):
    def test_add(self):
        self.assertTrue(add(5,4)==9)

    def test_multiply(self):
        self.assertTrue(multiply(3,4)==12)

    def test_negmultiply(self):
        self.assertTrue(multiply(3,-4)==-12)

    def test_power(self):
        self.assertTrue(power(2,8)==256)

    def test_negpower(self):
        self.assertTrue(power(2,-2)==1/2/2)

unittest.main()