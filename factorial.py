#factorial of a number

num = input("Enter a number")
fact = 1
inc = 2
for i in range(1,num):
    fact = fact*inc
    inc+=1
print fact