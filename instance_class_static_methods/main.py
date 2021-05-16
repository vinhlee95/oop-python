from typing import List


class MyClass:
	foo = "bar"

	def method(self):
		"""
		Instance method could be invoked only from a class instance
		It could modify the instance's propery, but not the class itself
		"""
		return f"instance method called. foo is {self.foo}"

	@classmethod
	def classmethod(cls):
		"""
		Class method points to the class, not the object instance when this method is called
		It thus could be invoke from the class itself without creating a new instance
		Class method can modify the class
		"""
		old_foo = cls.foo
		cls.foo = "foo"
		return f"class method called. foo changed from {old_foo} to {cls.foo}"

	@staticmethod
	def staticmethod():
		"""
		Staticmethod does not modify class or instance state
		and it is independent from everything else
		-> Because of ˆ, this method is also easy to test
		"""
		return 'static method called'

def print_my_class():
	print(MyClass().method()) # need to create a new object instance to call instance method
	# No need to create new instance to invoke classmethod() and static method()
	print(MyClass.classmethod())
	print(f"New class instance. foo is now {MyClass().foo}")
	print(MyClass.staticmethod())

# print_my_class()

"""
Factory functions
Used to create interfaces for variations of a data class
"""
class Pizza:
	mozzarella = "mozzarella"
	tomatoes = "tomatoes"

	def __init__(self, ingredients: List[str]) -> None:
		self.ingredients = ingredients

	def __repr__(self) -> str:
		return f"Pizza {self.ingredients}"

	@classmethod
	def margherita(cls):
		return cls([cls.mozzarella, cls.tomatoes])

def print_pizza():
	print(f"I want to have {Pizza.margherita()}")

# print_pizza()
