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

          new cod is here for do some conflict

#конфлікт виник при злитті гілок шляхом об'єднання(метод merge)
#тому що я змінила код файлу перейшовшs на другу гілку
#потім зробила злиття та вручну відкорегувала всі зміни, які потрібно залишити у зміненому файлі
