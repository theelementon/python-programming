

class Snake:

    def __init__(self, name):
        self.name = name

    def change_name(self, new_name):
        self.name = new_name

python = Snake("python")
anaconda = Snake("anaconda")
print(python.name)
print(anaconda.name)

class loops:
    print "Inside the class"
    def firstloop(self , number):
        print "Inside loop " + number
    def secondloop(self , number):
        print "Inside loop " + number

l = loops()
l.firstloop("1","one")
l.secondloop("2","two")