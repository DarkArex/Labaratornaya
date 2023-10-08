def PoiskID(enter, id):
    x = None
    y = None
    for i, entry in enumerate(enter):
        if entry == id:
            if x is None:
                x = i
            else:
                y = i
    if x is None:
        return ()
    elif y is None:
        return enter[x:]
    else:
        return enter[x:y+1]
print(PoiskID((1, 2, 3), 8))
print(PoiskID((1, 8, 3, 4, 8, 8, 9, 2), 8))
print(PoiskID((1, 2, 8, 5, 1, 2, 9), 8))
