## Python's Instance, Class, and Static Methods
* **Instance methods** need a class instance and can access the instance through self.
* **Class methods** don’t need a class instance. They can’t access the instance `self` but they have access to the class itself via `cls`.
* **Static methods** don’t have access to cls or self. They work like regular functions but *belong to the class’s namespace*.
* Static and class methods communicate and (to a certain degree) *enforce developer intent* about class design. This can have *maintenance benefits*.

### Resources
https://realpython.com/instance-class-and-static-methods-demystified/#instance-class-and-static-methods-an-overview
