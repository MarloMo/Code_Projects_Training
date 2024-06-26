class Person:
    # commonly referred to as the constructor method for the class.
    def __init__(self, name, age):
        self.name = name  # Initialize the name attribute
        self.age = age  # Initialize the age attribute

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."


# Creating an instance of the Person class
person1 = Person("Alice", 30)

# Accessing the attributes and methods of the instance
print(person1.name)  # Output: Alice
print(person1.age)  # Output: 30
print(
    person1.greet())  # Output: Hello, my name is Alice and I am 30 years old.
