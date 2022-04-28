# from functools import wraps

# def yo_mamma_decorator(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         orig_val = func(*args, **kwargs)
#         return f'Yo mamma says "{orig_val}"'
#     return wrapper

# def sophisticated_decorator(potatoes):
#     @wraps(potatoes)
#     def wrapper(*args, **kwargs):
#         orig_val = potatoes(*args, **kwargs)
#         return f'It is with a great honor that I hear you say "{orig_val}"'
#     return wrapper



# # @yo_mamma_decorator
# @sophisticated_decorator
# def just_saying(txt):
#     return txt

from sqlite3 import TimestampFromTicks
import time

def create_time(func):
  def wrap(*args, **kwargs):
    start = time.time()
    result = func(*args, **kwargs)
    end = time.time()

    print(func.__name__, end-start)
    return result
  return wrap

@create_time
def countdown(number):
  while number> 0:
    number -= 1

countdown(5)
countdown(1000)
