from turtle import begin_fill, end_fill, forward, right

def triangle(fill = True):
    if fill:
        begin_fill()
    for x in range(3):
        forward(100)
        right(120)
    end_fill()

def square(fill = True):
    if fill:
        begin_fill()
    for x in range(4):
        forward(100)
        right(90)
    end_fill()

def pentagon(fill = True):
    if fill:
        begin_fill()
    for x in range(5):
        forward(100)
        right(72)
    end_fill()

def hexagon(fill = True):
    if fill:
        begin_fill()
    for x in range(6):
        forward(100)
        right(60)
    end_fill()
    
def star(fill = True):
    if fill:
        begin_fill()
    for i in range(5):
        forward(100)
        right(144)
    end_fill()
    

