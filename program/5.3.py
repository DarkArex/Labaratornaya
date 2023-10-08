one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]
def CalcS(a, b, c):
    p = (a + b + c) / 2
    S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    return S
max1 = max(one)
min1 = min(one)
max2 = max(two)
min2 = min(two)
max3 = max(three)
min3 = min(three)
S1 = CalcS(max1, min2, min3)
S2 = CalcS(max2, min1, min3)
print(f"S 1 треугольника: {S1}")
print(f"S 2 треугольника: {S2}")