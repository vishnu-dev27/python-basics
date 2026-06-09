#1. Adding Items in tuples

cars = ('Audi','BMW','Toyota')
temp = list(cars)
temp

cars = tuple(temp)
cars

#2. Updating Items in tuples

cars = ('Audi','BMW','Toyota')
temp = list(cars)
temp[1] = 'Lexus'
temp

cars = tuple(temp)
cars

#3. Removing an Item using tuples

cars = ('Audi','BMW','Toyota')
temp = list(cars)
temp.remove('Toyota')
temp

cars = tuple(temp)
cars

#5. Unpacking a tuple in python

cars = ('Audi','BMW','Toyota')
car1, car2, car3 = cars
car1
'Audi'
car2
'BMW'
car3
'Toyota'


#6. Unpacking an tuple in python using Astersik

cars = ('Audi','BMW','Toyota')
car1, car2, *car3 = cars
car1

car2

car3

cars = ('Audi','BMW','Toyota')
car1, *car2, car3 = cars
car1

car2

car3
