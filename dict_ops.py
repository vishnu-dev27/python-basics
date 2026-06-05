#1. Changing Values in dictionaries using key words

car = {'brand':'audi','model':'Q8'}
car['Model'] = 'RS5'
car


#2. Changing Values in dictionaries using update() method

car = {'brand':'audi','model':'Q8'}
car.update({'model':'RS5'})
car

#3. Adding Values in dictionaries using key words

car = {'brand':'audi','model':'Q8'}
car['Color'] = Green
car

#4. Adding Values in dictionaries using update() method

car = {'brand':'audi','model':'Q8'}
car ({'color':'black'})
car

#5. removing an item in dictionaries using pop() method

car = {'brand':'audi','model':'Q8'}
car.pop('brand')
car

#6. removing an item in dictionaries using popitem() method

car = {'brand':'audi','model':'Q8'}
car.popitem( )
car

#7. removing an item in dictionaries using del and clear() method

car = {'brand':'audi','model':'Q8'}
del car['brand']
car

car = {'brand':'audi','model':'Q8'}
car.clear( )
car
