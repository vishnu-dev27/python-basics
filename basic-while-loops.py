#1. Basic while Loop

n=0
while n<=10:
    print(n)
    n+=1

#2. Sum of n-natural numbers using while-loop

n = int(input("enter the value of n: "))
sum = 0
while n>0:
    sum+= n
    n-=1
print(f"sum is {sum}.")

#3. Infinite while-loop

n = 10
while True:
    print(n)
    n-=1

#4. Breaking the infinite while-loop

while True:
    line = ("enter the line()type 'q'to quit: ")
        if line == 'q':
            break
            print(line)
