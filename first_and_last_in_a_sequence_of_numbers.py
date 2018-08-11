#finding first and last number in a random list
import random
rand = []
def randomnum():
    for i in range(1,9):
        c = random.randint(1,9)
        rand.append(c)
def listed(x):
    print rand
    print "{},{}".format(rand[0],rand[-1])
listed(randomnum())