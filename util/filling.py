from turtle import *

def is_filling(fill):
    if type(fill) != bool:
        raise Exception("Type of 'fill' must be a boolean")
        
    if filling():
        if not fill:
            return end_fill()
    else:
        if not fill:
            return begin_fill()
        
