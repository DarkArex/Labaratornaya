x = input("Введите последовательность чисел, разделенных пробелом: ")
y = [int(num) for num in x.split()]
z = tuple(y)
print("Список:", y)
print("Кортеж:", z)
