# PyFiglet + Turtle: Python Library Exploration and Fusion

## About This Project

This project explores two Python libraries, PyFiglet and Turtle, individually and then combines them into a single program.

The project was developed in three stages:

- **v0.1 – PyFiglet:** Exploring text generation using ASCII characters.
- **v0.2 – Turtle:** Exploring graphics, shapes, drawings and patterns.
- **v0.3 – Library Fusion:** Integrating PyFiglet and Turtle to display generated ASCII art in a graphical window.

## 1. PyFiglet – First Library (v0.1)

### What is PyFiglet?

PyFiglet is a Python library used to convert normal text into large ASCII-art characters.

### What I learned

- Importing PyFiglet into a Python program.
- Using the `figlet_format()` function.
- Converting normal text into ASCII art.
- Storing the generated output in a variable.
- Printing the generated ASCII art.

### Example

```python
import pyfiglet

result = pyfiglet.figlet_format("JARVIS")

print(result)
```

### Output

The word JARVIS is converted into large ASCII-art characters and displayed in the terminal.

## 2. Turtle – Second Library (v0.2)

### What is Turtle?

Turtle is a built-in Python graphics library used to create drawings, shapes, patterns and simple animations through programming instructions.

### What I learned

- Importing the Turtle library.
- Creating a Turtle object.
- Moving the turtle forward and backward.
- Turning left and right.
- Using loops to create geometric shapes.
- Drawing shapes using simple instructions.

### Example

```python
import turtle

t = turtle.Turtle()

for i in range(4):
    t.forward(100)
    t.right(90)

turtle.done()
```

### Output

A square is drawn inside the Turtle graphics window.

## 3. Library Fusion – PyFiglet + Turtle (v0.3)

### What does the combined project do?

This project integrates PyFiglet and Turtle to generate ASCII art and display it inside a Turtle graphics window.

### How the libraries contribute

**PyFiglet:**
- Generates ASCII art from normal text.
- Returns the generated design as a Python string.

**Turtle:**
- Receives the generated ASCII-art text.
- Displays the text inside a graphical window using its `write()` function.

### How they work together

1. PyFiglet converts the input word into ASCII art.
2. The generated output is stored in a variable.
3. The output is separated into individual lines.
4. Turtle receives those lines.
5. Turtle displays the ASCII art inside its graphics window.

### Combined Code

```python
import pyfiglet
import turtle

# Generate ASCII art using PyFiglet
art = pyfiglet.figlet_format("HI")

# Separate the generated text into lines
lines = art.splitlines()

# Create Turtle graphics window
screen = turtle.Screen()
screen.setup(900, 600)
screen.bgcolor("black")
screen.title("PyFiglet + Turtle Fusion")

# Configure Turtle
t = turtle.Turtle()
t.hideturtle()
t.penup()
t.color("cyan")

# Display ASCII art using Turtle
for i, line in enumerate(lines):
    t.goto(-350, 200 - i * 20)
    t.write(line, font=("Courier", 12, "normal"))

turtle.done()
```

### Expected Output

A black Turtle graphics window displaying the cyan ASCII-art representation of the word HI.

## 4. Requirements

Before running the project, you need:

- Python 3 installed.
- PyFiglet library installed.
- Turtle library (included in Python's standard library).

Install PyFiglet using:

```bash
python3 -m pip install pyfiglet
```

Turtle does not normally require a separate installation.

## 5. How to Run the Project

1. Clone or download this repository.
2. Open the project folder in VS Code.
3. Make sure PyFiglet is installed.
4. Open the terminal.
5. Run the following command:

```bash
python3 main.py
```

## 6. What I Learned From This Project

- How to explore Python libraries independently.
- How to read documentation and understand library functions.
- How to import and use external and built-in libraries.
- How to work with strings and variables.
- How to use loops and functions.
- How to understand and debug Python errors.
- How to combine two libraries into one working program.
- How one library's output can become another library's input.

## 7. Current Limitations and Future Improvements

Currently, the project has the following limitations:

- The input word is fixed in the program.
- Users cannot yet enter words through an interactive interface.
- Font selection and customization are not yet implemented.
- The generated artwork cannot yet be exported directly as an image.
- Turtle displays the ASCII characters as text rather than drawing each character's individual strokes.

Future improvements could include:

- Allowing users to enter their own text.
- Adding different colours and background options.
- Supporting different PyFiglet fonts.
- Adding animations and visual effects.
- Saving the final artwork as an image.

---

**Project Summary:** This project helped me understand two Python libraries individually and explore how they can be integrated to create a combined application. It demonstrates how Python libraries can work together to produce a result that neither library produces alone.