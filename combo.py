
import pyfiglet
import turtle

# Step 1: Generate ASCII art
art = pyfiglet.figlet_format("HI")

# Step 2: Separate the lines
lines = art.splitlines()

# Step 3: Create Turtle window
screen = turtle.Screen()
screen.setup(900, 600)
screen.bgcolor("black")
screen.title("PyFiglet + Turtle Fusion")

# Step 4: Configure Turtle
t = turtle.Turtle()
t.hideturtle()
t.penup()
t.color("cyan")

# Step 5: Draw PyFiglet output
for i, line in enumerate(lines):
    t.goto(-350, 200 - i * 20)
    t.write(line, font=("Courier", 12, "normal"))

# Step 6: Keep window open
turtle.done()
