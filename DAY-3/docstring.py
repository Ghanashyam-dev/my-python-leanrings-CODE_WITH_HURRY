# docstring are the strings or sentance written inside a function and can be displayed then function is called becoz some functions / modules installed externally the user need to know about how the function works , so docstring help to understand it . 


def add(a, b):
 """
    Returns the sum of two numbers
    Parameters
    a (int): The first number.
    b (int): The second number.
    Returns:
    int: The sum of the two numbers.
    """
 return a + b
print(add.__doc__)


# doc string are used to pass the message which id written inside the function or moudles and user can read it.