class Animal:
    def __init__(self,name):
        self.name = name
        self.is_alive = True
    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} is sleeping")
    def play(self):
        print(f"{self.name} is playing")
class Dog(Animal):
    pass
class Cat(Animal):
    pass
Dog = Dog("Scooby")
Cat = Cat("Canute")
print(Dog.name)
print(Dog.is_alive)
Dog.eat()
Dog.sleep()
print(Cat.name)
print(Cat.is_alive)
Cat.eat()
Cat.sleep()
