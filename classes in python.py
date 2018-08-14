

'''class Snake:

    def __init__(self, name):
        self.name = name

    def change_name(self, new_name):
        self.name = new_name

python = Snake("python")
anaconda = Snake("anaconda")
print(python.name)
print(anaconda.name)

class calculator:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def addition(self):
        print self.x + self.y
    def subtract(self):
        print x - y
    def multiply(self):
        print x * y
    def division(self):
        print x / y

c = calculator(9,8)
c.addition() '''

class power:
    def spliting(self,sent):
        sentence = sent.split(" ")
        return sentence
    def printing(self,sentence):
        print " ".join(sentence[::-1])

s = power()

s.printing(s.spliting("This is a sentence"))

