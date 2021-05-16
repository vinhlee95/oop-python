import functools
import time

def timer(func):
	"""
	Print the runtime of the decoration function

	We wrap the function argument within @functools.wraps so that it could copy over the function name,
	docstrings, argument list
	
	https://docs.python.org/3/library/functools.html#functools.wraps
	https://stackoverflow.com/questions/308999/what-does-functools-wraps-do
	"""
	@functools.wraps(func)
	def wrapper_timer(*args, **kwargs):
		start_time = time.perf_counter()
		result = func(*args, **kwargs)
		end_time = time.perf_counter()
		print(f"Finished executing {func.__name__}. Execution time is {end_time - start_time}")
		return result

	return wrapper_timer
	
@timer
def do_stuff(num_times):
	"""
	Calculate sum
	"""
	for _ in range(num_times):
		sum([i**2 for i in range(10000)])

# Print name and docstring of the main function
print(do_stuff.__name__) # without @functools.wrap, this would print "wrapper_timer"
print(do_stuff.__doc__) # without @functools.wrap, this would print "None" even though do_stuff does has docstring

do_stuff(2)
