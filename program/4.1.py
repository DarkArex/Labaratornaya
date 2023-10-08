from datetime import datetime # подклчение библиотеки datetime для исползования функций datetime
from math import sqrt # подклчение библиотеки math для исползования функций sqrt
def main(**kwargs):
    '''
    Вычисляет длину гипотенузы по теореме Пифагора
    '''
    for key in kwargs.items():
        result = sqrt(key[1][0] ** 2 + key[1][1] ** 2)
        print(result)


# Это условие, которое проверяет, запущен ли скрипт напрямую
if __name__ == '__main__':
  # Переменная с датой и временем начала работы функции
    start_time = datetime.now()
  # Вызов функции, в параметры передается список из двух переменных
    main(
        one=[10, 3],
        two=[5, 4],
        three=[15, 13],
        four=[93, 53],
        five=[133, 15])
# Вычисление время выполнения программы
time_costs = datetime.now() - start_time
# Вывод времени выполнения программы
print(f"Время выполнения программы {time_costs}")