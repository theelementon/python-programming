#password generator

import random
password = []
weak = ["ersdfgbfer", "jvbrfindiv", "dfvgkyatca", "kysvcakdsd", "aytsvckeft"]
weakopt = random.randint(0,4)
option = raw_input("How strong do you want the password to be?")
if (option == "weak"):
    print weak[weakopt]
elif (option == "medium"):
    for i in range(1,5):
        password.append(str(unichr(random.randint(97,122))))
        password.append(str(unichr(random.randint(48,57))))
    print "".join(password)
elif (option == "strong"):
    for i in range(1,10):
        password.append(str(unichr(random.randint(33,126))))
    print "".join(password)