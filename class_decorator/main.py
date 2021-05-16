from typing import Callable
from time import time
import functools

def debug(func):
	"""Print the function signature and return value"""
	@functools.wraps(func)
	def wrapper_debug(*args, **kwargs):
		args_repr = [repr(a) for a in args]                     
		kwargs_repr = [f"{k}={v}" for k, v in kwargs.items()] 
		signature = ", ".join(args_repr + kwargs_repr)   

		print(f"Calling {func.__name__} ({signature})")

		value = func(*args, **kwargs)
		print(f"{func.__name__!r} returned {value!r}")          
		
		return value

	return wrapper_debug

class MyDecorator:
	def __init__(self, function: Callable) -> None:
		self.function = function

	def __call__(self, *args, **kwargs) -> None:
		start_time = time()
		result = self.function(*args, **kwargs)
		end_time = time()
		print(f"Execution took {format(end_time - start_time)} seconds")
		return result


@MyDecorator
def call_name(name: str):
	return f"Hi {name}"


# message = call_name("Foo")
# print(message)

"""
Passing argument to the class decorator
"""
class MyDecoratorWithArgument(object):
	def __init__(self, func) -> None:
		self.func = func

	@debug
	def __call__(self, *args, **kwargs) -> None:
		return self.func(*args, **kwargs)


@MyDecoratorWithArgument
def call_name_2(name: str):
	return f"Hello {name}"


message = call_name_2("Foo")
print(message)


"""
Function as a wrapper
"""
def do_twice(fn: Callable):
	def wrapper_do_twice(*args, **kwargs):
		print(args, kwargs)
		fn(*args, **kwargs)
		fn(*args, **kwargs)

	return wrapper_do_twice

@do_twice
def main_function(first_numb: int, last_numb: int, optional: int) -> int:
	sum = first_numb + last_numb
	if optional:
		sum = sum + optional

	print("Sum is:", sum)
	return sum


# main_function(3, 4, optional=2)