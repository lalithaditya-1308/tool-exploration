
import pyfiglet
import turtle

# PyFiglet
text = pyfiglet.figlet_format("HELLO")
print(text)

# Turtle
t = turtle.Turtle()

for i in range(4):
    t.forward(100)
    t.right(90)

turtle.done()
