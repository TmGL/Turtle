import turtle
from util.shapes import *
from util.filling import *

def make_shape(name, colour = "black", fill = True):
    if type(name) != str:
        raise Exception("Type of 'name' must be a string")
    if type(colour) != str:
        raise Exception("Type of 'colour' must be a string")
    if type(fill) != bool:
        raise Exception("Type of 'fill' must be a boolean")
    
    turtle.fillcolor(colour)
    turtle.clear()

    name = name.lower()
    if name == "triangle":
        return triangle(fill)
    elif name == "square":
        return square(fill)
    elif name == "pentagon":
        return pentagon(fill)
    elif name == "hexagon":
        return hexagon(fill)
    elif name == "star":
        return star(fill)
    else:
        raise Exception("Invalid shape was provided")
