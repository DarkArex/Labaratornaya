oldoc1 = [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4]
oldoc2 = [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4]
oldoc3 = [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]
def NewOcencki(Oc):
    NewOcencki = []
    for i in Oc:
        if i == 2:
            continue
        elif i == 3:
            NewOcencki.append(4)
        else:
            NewOcencki.append(i)
    return NewOcencki
newoc1 = NewOcencki(oldoc1)
newoc2 = NewOcencki(oldoc2)
newoc3 = NewOcencki(oldoc3)
print(f"Новые оценки 1: {newoc1}")
print(f"Новые оценки 2: {newoc2}")
print(f"Новые оценки 3: {newoc3}")