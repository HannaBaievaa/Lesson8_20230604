def mane_function() :
    result = {}
    for color in colors :
        if color not in result :
            result[color] = 1
        else :
            result[color] += 1
        pairs = 0
