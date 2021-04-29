def str_to_bool(string):
    if type(string) != str:
        raise Exception("Type of 'string' must be str")
    
    return string.lower() in ["yes", "ye", "y", "yeah", "yea"]
