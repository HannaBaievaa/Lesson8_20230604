def mane_function(*args) :
    result = {}
    for i in args :
        for k,v in i.items :
            if k not in result :
                result[k] = v
            else :
                result[k] += v
        return result

