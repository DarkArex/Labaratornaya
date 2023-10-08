from collections import Counter


def Poisk(str):
    shet = Counter(str)
    best = shet.most_common(3)
    res = {int(num): count for num, count in best}
    return res
x = "87441654652165456456222"
result = Poisk(x)
sort = dict(sorted(result.items()))
print(sort)