#1 Acessing characters of a string using for loop

name = "K Sai Vishnuvardhan"
for c in name:
	print(c,end = ' ')

#2 Iterating a string in a reverse order

name = "Kevin"
for c in name [::-1]:
	print(c,end = ' ')

#3 Accessing words of a string

sentence = "I am a good guy"
count = 0
for word in sentence.split():
	count += 1
print(f"there are {count} words in this sentence")
