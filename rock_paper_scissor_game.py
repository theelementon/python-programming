#rock paper scissor game

import random
print "1 for rock,2 for scissor,3 for paper"
us=0
cs=0
while True:
    user = input("enter anumber  between  1 to 3 : ")
    comp = random.randint(1,3)
    if (user==1 and comp==2 or user==2 and comp==3 or user==3 and comp==1):
        us+=1
        print"user wins"
        print "user=%d, comp=%d"%(us,cs)

    elif (user==2 and comp==1 or user==3 and comp==2 or user==1 and comp==3):
        cs+=1
        print"comp wins"
        print "user=%d, comp=%d"%(us,cs)

    elif (user==1 and comp==1 or user==2 and comp==2 or user==3 and comp==3):
        print" match draw"
        print "user=%d, comp=%d"%(us,cs)
    elif(user>3):
        print "wrong input, enter 1 or 2 or 3"
    elif(user==0):
         print"thank you for playing"
         break