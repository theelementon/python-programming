#prime number

prime = input("Enter a number")
flag = 0
div = []
for i in range(2,prime-1,1):
    if(prime%i == 0):
        div.append(i)
        flag=1
if (flag == 1):
    print "Not a prime"
    print "its divisors are {}".format(div)
else:
    print "prime"