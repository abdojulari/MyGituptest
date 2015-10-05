def add(a,b):
    print "ADDING %d + %d" % (a,b)
    return a + b

def subtract(a,b):
    print "SUBSTRACTING %d - %d" % (a,b)
    return a - b

def multiply(a,b):
    print "MULTIPLYING %d * %d" %(a,b)
    return a * b

def divide(a,b):
    print "DIVIDING %d / %d" %(a,b)
    return a/b

print "Let's try out with these functions"

age = add(30, 6)
height = subtract(70, 2)
weight = multiply(70, 3)
iq = divide(124,2)

print "Age: %d, Height: %d, Weight:%d, IQ: %d" %(age, height, weight, iq)

print "let's try out this funny puzzle"
what= add(age, subtract(height, multiply(weight, divide(iq,2))))
print "I think this", what, "serves the basis of practice"

