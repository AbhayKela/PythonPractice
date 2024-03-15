import functools
def add_number(a,b):
    return a + b

numbers = [33,77,9.9,100,88] # provide as list
result = functools.reduce(add_number,numbers)
print(result)