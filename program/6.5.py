def Podchet(x):
    sum = 0
    for i in x:
        if isinstance(i, list):
            sum += Podchet(i)
        elif isinstance(i, int):
            sum += i
    return sum
prim1 = [1, 2, 3, 4, 5]
prim2 = [1, [2, 3], [4, [5, 6]]]
prim3 = []
print(Podchet(prim1))
print(Podchet(prim2))
print(Podchet(prim3))