def add(x,y):
    print "Adding %d + %d" %(x,y)
    return x+y

def subtract(x,y):
    print "Subtracting %d - %d" % (x,y)
    return x-y

def multiply(x,y):
    print "Multiplying %d * %d" %(x,y)
    return x * y

def divide(x,y):
    print "Dividing %d / %d" %(x,y)
    return x / y


print "Let's do some math with just functions!"

age     = add(15,10)
height  = subtract(75,8)
weight  = multiply(60,2)
iq      = divide(120,2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" %(age,height,weight,iq)


#A puzzle for the extra credit, type it in anyway.
print "Here's a puzzle."

what = add(age, subtract(height,multiply(weight,divide(iq,2))))

print "That becomes: ",what, "can you do it by hand?"
