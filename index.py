from functions.make_shape import *
from util.str_to_bool import *
from util.valid_shape import *

name = raw_input("What shape do you want to make? ")
if not name:
    raise Exception("You did not provide a valid shape! Please restart.")

colour = raw_input("What colour do you want your shape to be? ")
fill = str_to_bool(raw_input("Do you want your shape filled in? "))

make_shape(name, colour, fill)
