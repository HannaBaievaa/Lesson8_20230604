def mane_function(test_results) :
    if test_results == [] :
        return [0,0,0]

        import math
        total = 0
        for i in range(len(test_results)) :
            total += test_results[i]
        medium = total / len(test_results)

