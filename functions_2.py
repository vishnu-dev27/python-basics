#1. Functions with Variable length arguements (*args)

def add(*numbers):
    print(sum(numbers))
add(1,3,4,5,6,7)


#2. Functions with keywords Variable length arguements (**kwargs)

def details(**data)
    print(data)
data(name="Leon",age=27)


#3. Lambda Functions

square = lambda x: x*x
print(square(67))


#4. Nested Functions

def outer():
    def inner():
        print("Hello, Leon S. Kennedy")
    inner()
outer()


#5. Recursive Functions

def countdown(n):
    if n == 0:
        print("The space shuttle is now ready for launch.")
        return
    print(n)
    countdown(n -1)
countdown(10)
