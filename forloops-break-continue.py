#1. Break statement using For-loop

numbers = list(range(1,100))

for number in numbers:
    if number>50:
		break
print(number, end = ' ')


#2. Continue statement using For-loop

for i in range(9)
    if i==4:
        continue
print(i)

#3. Nested For-loop

list1 = [1,2,3]
list2 = [4,5,6]
for i in list1:
    for j in list2:
        print()
