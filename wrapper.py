from functools import wraps

def yo_mamma_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        orig_val = func(*args, **kwargs)
        return f'Yo mamma says "{orig_val}"'
    return wrapper

def sophisticated_decorator(potatoes):
    @wraps(potatoes)
    def wrapper(*args, **kwargs):
        orig_val = potatoes(*args, **kwargs)
        return f'It is with a great honor that I hear you say "{orig_val}"'
    return wrapper


# @yo_mamma_decorator
@sophisticated_decorator
def just_saying(txt):
    return txt


if __name__ == "__main__":
    print(just_saying('I love star wars!!!'))