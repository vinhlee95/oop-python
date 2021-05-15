from typing import Callable
from time import time


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
	def __init__(self, arg) -> None:
		self._arg = arg

	def __call__(self, *param_arg) -> None:
		print(param_arg)


@MyDecoratorWithArgument("foo")
def call_name_2(name: str):
	return "FOo bar"


# message = call_name_2()
# print(message)


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


main_function(3, 4, optional=2)