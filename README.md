# Тема 2. Базовые операции языка Python
Отчет по Теме #2 выполнил:
- Корявец Роман Иванович
- ЗПИЭ-20-2

| Задание | Сам_раб |
| ------ | ------ |
| Задание 1 | + |
| Задание 2 | + |
| Задание 3 | + |
| Задание 4 | + |
| Задание 5 | + |
| Задание 6 | + |
| Задание 7 | + |
| Задание 8 | + |
| Задание 9 | + |
| Задание 10 | + |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.

## Самостоятельная работа №1
### Выведите в консоль булевую переменную False, не используя слово False в строке или
изначально присвоенную булеву переменную. Программа должна занимать не более двух
строк редактора кода.

```python
print(not True)
```
### Результат.
![Меню](https://github.com/DarkArex/Labaratornaya/blob/Tema-2/picture/1.png)

## Выводы
Мы научились использовать логический оператор not. Для инвертирования значения True, что приводит к выводу False.

## Самостоятельная работа №2
### Присвоить значения трем переменным и вывести их в консоль, используя только две строки редактора кода.

```python
x, y, z = 8, 3, 1
print(x, y, z)
```

### Результат.
![Меню](https://github.com/DarkArex/Labaratornaya/blob/Tema-2/picture/2.png)

## Выводы
Во второй работе мы изучили способы присвоения значений одновременно нескольким переменным

## Самостоятельная работа №3
### Реализуйте ввод данных в программу, через консоль, в виде только целых чисел (тип данных int). Tо есть при вводе буквенных символов в консоль, программа не должна работать. Программа должна занимать не более двух строк редактора кода.

```python
x = int(input("Введите число: "))
print(x)
```

### Результат.
![Меню](https://github.com/DarkArex/Labaratornaya/blob/Tema-2/picture/3.png)

## Выводы
В данной работе мы изучили способы присвоения значений переменной определенного типа.

## Самостоятельная работа №4
### Создайте только одну строковую переменную. Длина строки должна не превышать 5 символов. На выходе мы должны получить строку длиной не менее 16 символов. Программа должна занимать не более двух строк редактора кода.

```python
x = "AAAB"
print(x*4)
```

### Результат.
![Меню](https://github.com/DarkArex/Labaratornaya/blob/Tema-2/picture/4.png)

## Выводы
Изучив материал, мы научились взаимодействовать со строкой в данной работе

## Самостоятельная работа №5
### Создайте три переменные: день (тип данных - числовой), месяц (тип данных - строка), год (тип данных - числовой) и выведите в консоль текущую дату в формате: "Сегодня день месяц год. Всего хорошего!" используя F строку и оператор end внутри print(), в котором вы должны написать фразу "Всего хорошего!". Программа должна занимать не более двух строк редактора кода.

```python
day, mounth, year = int(7), str("октября"), int(2023)
print(f"Сегодня {day} {mounth} {year}.", end="Всего хорошего!"
```

### Результат.

![Меню](https://github.com/DarkArex/Labaratornaya/blob/Tema-2/picture/5.png)

## Выводы
Мы ознакомились со способом выведения информации в виде F строки

## Самостоятельная работа №6

### В предложении 'Hello World' вставьте 'my' между двумя словами. Выведите полученное предложение в консоль в одну строку. Программа должна занимать не более двух строк редактора кода.

```python
x = "my"
print("Hello {} world".format(x))
```

### Результат.

![Меню](https://github.com/DarkArex/Labaratornaya/blob/Tema-2/picture/6.png)

## Выводы
В шестой работе мы изучили методы внесния элементов в строку

## Самостоятельная работа №7
### Узнайте длину предложения 'Hello World', результат выведите в консоль. Программа должна занимать не более двух строк редактора кода.

```python
x = "Hello world"
print(len(x))
```

### Результат.

![Меню](https://github.com/DarkArex/Labaratornaya/blob/Tema-2/picture/7.png)

## Выводы
В данной работе мы узнали, что с помощью функции `len()` можно узнать длинну строки

## Самостоятельная работа №8
### Переведите предложение 'HELLO WORLD' в нижний регистр. Программа должна занимать не более двух строк редактора кода.

```python
x = "HELLO WORLD"
print((x).lower)
```

![Меню](https://github.com/DarkArex/Labaratornaya/blob/Tema-2/picture/8.png)

## Выводы
В данной работе мы изучили способы изменения регистра строки на нижний

## Самостоятельная работа №9
### Самостоятельно придумайте задачу по проходимой теме и решите ее. Задача должна быть связана со взаимодействием с числовыми значениями. (Возведите число в третью степень. Программа должна занимать не более двух строк редактора кода.)

```python
x, y ,z = 10, 2, 6
print(x/y*z)
```

![Меню](https://github.com/DarkArex/Labaratornaya/blob/Tema-2/picture/9.png)

## Выводы
В данном примере мы присвоили нескольким переменным значеие, а после выполнили аврифметические вычисления над ними

## Самостоятельная работа №10
### Самостоятельно придумайте задачу по проходимой теме и решите ее. Задача должна быть связана со взаимодействием со строковыми значениями. (Напишите предложение 'Hello World' в две строки. Написанная программа должна занимать одну строку в редакторе кода.)

```python
x = "Hello"
y = "world"
print((x+y).upper)
```

![Меню](https://github.com/DarkArex/Labaratornaya/blob/Tema-2/picture/10.png)

## Выводы
В данном примере мы объединили две строки и поменяли региср получившегося результата на верхний
## Общие выводы по теме
В данной теме мы изучили работу с различными переменными, изучили их типы и то как можно взаимодействовать с переменными. Также были изучены спопобы выведения информации в консоль и возможности использования логических операторов.
