#to find divisor of a number

num = input("enter a number")
listname = []
a=1
while a<=num:
    listname.append(a)
    a+=1
print filter((lambda x:num%x),listname)