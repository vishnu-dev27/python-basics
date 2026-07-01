#1. __init__method

class Student:
    def _init_(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Vishnu", 18)

print(s1.name)
print(s1.age)

#2. __str__ method

class Student:
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return f"Student: {self.name}"
s1 = Student("vishnu")
print(s1)

#3. __repr__ method

class Student:
    def __init__(self, name):
        self.name = name
        def __repr__(self):
            return f"Student('{self.name}')"

s1 = Student("Vishnu")

print(repr(s1))


#4. __len__ method

class Team:
    def __init__(self, players):
        self.players = players
        def __len__(self):
            return len(self.players)

team = Team(["Luffy", "Zoro", "Sanji"])

print(len(team))


#5. __add__ method

class Coins:
    def __init__(self, amount):
        self.amount = amount
    def __add__(self, other):
        return Coins(self.amount + other.amount)

c1 = Coins(200)
c2 = Coins(300)

total = c1 + c2

print(total.amount)


#6. __eq__ method

class Player:
    def __init__(self, level):
        self.level = level
        def __eq__(self, other):
            return self.level == other.level

p1 = Player(100)
p2 = Player(100)

print(p1 == p2)


#7. __lt__ method

class Score:
    def __init__(self, marks):
        self.marks = marks
    def __lt__(self, other):
        return self.marks < other.marks

a = Score(75)
b = Score(90)

print(a < b)


#8. __getitem__ method

class Inventory:
    def __init__(self, items):
        self.items = items
    def __getitem__(self, index):
        return self.items[index]

bag = Inventory(["Sword", "Potion", "Shield"])

print(bag[0])
print(bag[2])


#9. __contains__ method

class Crew:
    def __init__(self):
        self.members = ["Luffy", "Zoro", "Nami"]
    def __contains__(self, item):
        return item in self.members

crew = Crew()

print("Luffy" in crew)
print("Sanji" in crew)


#10. __call__ method

class Greeting:
    def __call__(self):
        print("Welcome aboard!")

greet = Greeting()

greet()
