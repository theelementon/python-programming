#fibonacci number finder using functions

fibo = [0,1]
num = input("Enter a number to make fibonacci series")
a = 0
b = 1
def function(a,b):
        lfib = fibo[b] + fibo[a]
        fibo.append(lfib)
        return

for i in range(2, num):
        function(a,b)
        a+=1
        b+=1

print fibo