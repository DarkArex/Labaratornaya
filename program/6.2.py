def delete(tup, delete):
    if delete not in tup:
        return tup
    else:
        delete = tup.index(delete)
        return tup[:delete] + tup[delete+1:]
x1 = ((1, 2, 3), 1)
x2 = ((1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2), 3)
x3 = ((2, 4, 6, 6, 4, 2), 9)
y1 = delete(x1[0], x1[1])
y2 = delete(x2[0], x2[1])
y3 = delete(x3[0], x3[1])
print(y1)
print(y2)
print(y3)