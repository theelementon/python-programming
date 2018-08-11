#reversing a sentence using function

def splitt(d):
    global c
    c = (d.split(" "))
    return c

splitt("This is a test sentence")
print c[::-1]