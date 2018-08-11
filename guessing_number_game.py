#guess the number game

import random

num = random.randint(1,9)
count = 0
while True:
    user = raw_input("guess the number")
    if (user == "exit"):
        print "Thank you for playing"
        break
    user = int(user)
    if (user != num and user > num):
        print "Wrong, Too high"
        count +=1
    elif (user != num and user < num):
        print "Wrong, Too low"
        count+=1
    else:
        print "Yes, you are right, the number is %d" %num
        num = random.randint(1,9)
        print "number of guesses are %d" %count
        count = 0