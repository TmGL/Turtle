def valid_shape(arg): 
    options = {
        "square": "square", 
        "tri": "triangle",
        "triangle": "triangle",
        "penta": "pentagon",
        "pentagon": "pentagon",
        "hex": "hexagon",
        "hexagon": "hexagon",
    }

    return options.get(arg);
