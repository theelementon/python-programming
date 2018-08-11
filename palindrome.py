
#code to check palindrome

a = raw_input("enter your name")
if a[0:].lower() == a[::-1].lower():
    print "It is a palindrome"
else:
    print "not a palindrome"