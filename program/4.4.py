def sqr(*args):
    if len(args) == 0:
        return 0
    x = sum(args)
    mid = x / len(args)
    return mid

if __name__ == "__main__":
    x = [1, 2, 3, 4, 5]
    mid = sqr(*x)
    print(f"Среднее арифметическое: {mid}")