def Sozdanie(Vvod):
    res = set()
    shet = {}
    for i in Vvod:
        if i not in shet:
            shet[i] = 1
            res.add(i)
        else:
            shet[i] += 1
            res.discard(i)
            res.add(str(i) * shet[i])
    return res
x1 = [1, 1, 3, 3, 1]
x2 = [5, 5, 5, 5, 5, 5, 5]
x3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]
y1 = Sozdanie(x1)
y2 = Sozdanie(x2)
y3 = Sozdanie(x3)
print(y1)
print(y2)
print(y3)