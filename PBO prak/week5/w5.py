# Define a parent class
class Animal:
  def __init__(self, name, species):
    self.name = name
    self.species = species

  def make_sound(self):
    pass

# Define a child class that inherits from the parent class
class Dog(Animal):
  def __init__(self, name, breed):
    super().__init__(name, species="Dog")
    self.breed = breed

  def make_sound(self):
    return "Woof!"

# Create an instance of the child class
my_dog = Dog("Fido", "Golden Retriever")

# Access attributes and methods of the parent and child classes
print(my_dog.name)      # Output: "Fido"
print(my_dog.species)   # Output: "Dog"
print(my_dog.breed)     # Output: "Golden Retriever"
print(my_dog.make_sound())  # Output: "Woof!"
