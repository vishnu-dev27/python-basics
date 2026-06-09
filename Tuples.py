#1. Basic tuples

cars = ('Audi','Mercedes','BMW')
cars

cars = ('Audi','Mercedes','Mercedes','BMW')
cars


#2. tuples with one items
cars = ('Toyota',)
cars

#3. Length of a tuple

cars = ('Audi','Mercedes','BMW')
len(cars)


#4. The tuple () comstructor

cars = tuple(('Audi','Mercedes','BMW'))
cars

#5. Accessing tuple items:

#positive indexing
cars = ('Audi','Mercedes','BMW')
cars[1]

#negative indexing
cars = ('Audi','Mercedes','BMW')
cars[-1]

#through slicing
cars = ('Audi','Mercedes','BMW')
cars[1:3]
cars[1:]
cars[:]
