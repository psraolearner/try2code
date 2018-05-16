import turtle 

painter = turtle.Turtle()

painter.pencolor("red")

for i in range(50):
    painter.backward(60)
    painter.left(123) # Let's go counterclockwise this time 
    
painter.pencolor("blue")
for i in range(50):
    painter.backward(120)
    painter.left(123)


    
turtle.done()
