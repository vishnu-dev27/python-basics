#1. Basic dictionaries

car = {'Brand':'Audi','Model':'q7'}
car

car = {'Brand':'Audi','Model':'q7'}
car['Model'] = 'q8'
car

#2. length of dictionary

car = {'Brand':'Audi','Model':'q7'}
len(car)

#3. the dict() constructor

car = dict(Brand = "Audi", Model = "q8")
car

#4. Accessing dictionary items in python using key names

car = {'Brand':'Audi','Model':'q7'}
car['Brand']
car

#5. Accessing dictionary items in python using get() method

car = {'Brand':'Audi','Model':'q7'}
car.get('Model')
car

#6. Accessing dictionary items in python using keys() method

car = {'Brand':'Audi','Model':'q7'}
car_keys = car.keys()
car_keys
car['fuel type'] = 'Diesel'
car_keys


#7. Accessing dictionary items in python using values() method

car = {'Brand':'Audi','Model':'q7'}
car_values = car.values()
car_values
car['fuel type'] = 'Diesel'
car_values

#8. Accessing dictionary items in python using items() method

car = {'Brand':'Audi','Model':'q7'}
car_items = car.items()
car_items
car['fuel type'] = 'Diesel'
car_items
