def sum():
    try:
        x = input("Введите число: ")
        num = float(x)
        res = 2 + num
        print(f"Результат сложения: {res}")
    except ValueError:
        print("Ошибка: Неподходящий тип данных. Ожидалось число.")

sum()
sum()