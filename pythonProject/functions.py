def add(*args):
    return sum(args)

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def greet(name):
    return f"Привет, {name}!"

def is_positive(x):
    return x > 0

def is_negative(x):
    return x < 0

def filter_list(lst, func):
    return [x for x in lst if func(x)]