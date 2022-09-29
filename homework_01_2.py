# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

variables = [0,1]
for x in variables:
    for y in variables:
        for z in variables:
            result1 = (not (x or y or z))
            result2 = ((not x) and (not y) and (not z))
            my_result = result1 is result2
            print(x, y, z, result1, result2, my_result)