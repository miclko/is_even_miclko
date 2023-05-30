#is even function


def is_even(x):
    """Function for checking evenness of integers
    Input: x integer
    output:
    true if x  even
    false if x odd
    raise exception if not an integer 
    """    
    if not isinstancex(x,int):
        raise Exception('not an integer')


assert is_even.__doc__ 

has_raised_exception = False
try:
    is_even('3sajnk')
except:
    has_raised_exception = True
    
assert has_raised_exception    