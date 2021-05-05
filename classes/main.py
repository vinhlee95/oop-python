class Human:
	# Class attribute
	is_intelligent = True

	def __init__(self, name: str, age: int) -> None:
		self.name = name
		self.age = age

	# Instance method
	def __repr__(self) -> str:
		return f"{self.name} is {self.age} years old."

	def speak(self, sound: str) -> str:
		return f"{self.name} says {sound}"


# Instantiate an object
my_human = Human(name="Foo", age=12)
foo_human = Human(name="Foo", age=23)
# Object is mutable by default
foo_human.is_intelligent = False

print(my_human.speak("Hello"))

# Inheritance
class SuperHuman(Human):
	def speak(self, sound = "I am super human!"):
		return super().speak(sound=sound)


superman = SuperHuman(name="Clark Kent", age=35)
print(superman.speak())