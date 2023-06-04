def mane_function() :
    result = {}
    for color in colors :
        if color not in result :
            result[color] = 1
        else :
            result[color] += 1
        pairs = 0
        for color in result :
            pairs += result[color] // 2
            return pairs

def test_function(*args) :
    for i in args :
        for k,v in i.items :
            if k not in result :
                result[k] = v
            else :
                result[k] += v
        return result

#конфлікт виникає при злитті гілок шляхом об'єднання(метод merge)
#тому що ми маємо зміни в одному й тому самому файлі в двох різних гілках
#Git призупиняє процес допоки конфлікт не буде вирішено вручну
