#1. input a liat using split( ) method

numbers = input("Enter the numebrs: ").split()
enters the numebsr: 67,66,65,64
numbers

#2. accepting a list using split() and for-loop

n = int(input("enter the number of elements: "))
enter the number of elements: 3
numbers = input("enter the numebrs: ")
enter the numbers: 67,66,65
for i in range(0.n):
	numbers[i] = int(numbers[i])

#3.changing list items in python

list = ["Max","Lewis",1,2,"Norris"]
list[2] = "Piastri"
list

#4. changing multiple items in lists

list = ["Max","Lewis",1,2,"Norris"]
list[2:4] = ["Piastri","Gasly"]
list

#5. removing items from list using remove() method

li = ["Max","Lewis","Ocon","Norris"]
li.remove("Norris")
li

#6. removing items from list using pop() method

li = ["Max","Lewis","Ocon","Norris"]
li.pop(3)
li

#7. removing items from list using del keyword

li = ["Max","Lewis","Ocon","Norris"]
del li(3)
li

#8. removing items from list using clear() method

li = ["Max","Lewis","Ocon","Norris"]
li.clear()
li

#9. Comprehension of lists and it's Syntax

names = ['John','Jack','Jimmy','Mike','Karl']
j_names = []
for name in names:
	if 'J' in name:
		j_names.append(names)

j_names
