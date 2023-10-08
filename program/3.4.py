x = str(input("Insert string: "))
print("Длина предложения: ", len(x))
print("Строка в нижнем регистре: ", x.lower())
glasnie = 0
for i in x:
    l = i.lower()
    if l == "a" or l == "e" or\
       l == "i" or l == "o" or\
       l == "u":
        glasnie += 1
print("Количество гласных (a, e, i, o, u) в предложении: ", glasnie)
rep = x.lower().replace('ugly', 'beauty')
print("'Ugly' теперь 'beauty'  : ", rep)
print("Строка начинается с 'The': ", x.startswith('The'))
print("Строка оканчивается на 'end': ", x.endswith('end'))