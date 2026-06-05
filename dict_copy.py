#1. copying a dictionary in python

car = {'Brand':'Audi','Model':'q7'}
car_copy = car
car_copy

id(car)
id(car_copy)

#2. copying a dictionary in python using copy() method

car = {'Brand':'Audi','Model':'q7'}
car_copy = car.copy()
car_copy

car_copy['model'] = 'q8'
car_copy

#3. copying a dictionary in python using dict() method

car = {'Brand':'Audi','Model':'q7'}
car_copy = car.dict()
car_copy

car_copy['model'] = 'q8'
car_copy
car
