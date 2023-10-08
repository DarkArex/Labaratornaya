# Тема 7. Работа с файлами (ввод, вывод)
Отчет по Теме #7 выполнил(а):
- Корявец Роман Иванович
- ЗПИЭ-20-2

| Задание | Сам_раб |
| ------  | ------ |
| Задание 1 | + |
| Задание 2 | + |
| Задание 3 | + |
| Задание 4 | + |
| Задание 5 | + |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.

## Самостоятельная работа №1
### Найдите в интернете любую статью (объем статьи не менее 200 слов), скопируйте ее содержимое в файл и напишите программу, которая считает количество слов в текстовом файле и определит самое часто встречающееся слово. Результатом выполнения задачи будет: скриншот файла со статьей, листинг кода, и вывод в консоль, в котором будет указана вся необходимая информация.

```python
def ShetSlow(statia):
    with open(statia, 'r', encoding='utf-8') as file:
        text = file.read()
        words = text.split()
        wordscount = len(words)
        return wordscount
def PopularWord(statia):
    with open(statia, 'r', encoding='utf-8') as file:
        text = file.read()
        words = text.split()
        wordscount = {}
        for i in words:
            if i in wordscount:
                wordscount[i] += 1
            else:
                wordscount[i] = 1
        best = max(wordscount, key=wordscount.get)
        return best, wordscount[best]

file = 'text 7.1.txt'
calc = ShetSlow(file)
popular, count = PopularWord(file)
print(f'Количество слов в файле: {calc}')
print(f'Самое часто встречающееся слово: "{popular}" (встречается {count} раз)')
```

### Результат
![Меню](https://github.com/DarkArex/Labaratornaya/blob/Tema-7/picture/1.png)
![Меню](https://github.com/DarkArex/Labaratornaya/blob/Tema-7/picture/1.1.png)


## Выводы

  
## Самостоятельная работа №2
### У вас появилась потребность в ведении книги расходов, посмотрев все существующие варианты вы пришли к выводу что вас ничего не устраивает и нужно все делать самому. Напишите программу для учета расходов. Программа должна позволять вводить информацию о расходах, сохранять ее в файл и выводить существующие данные в консоль. Ввод информации происходит через консоль. Результатом выполнения задачи будет: скриншот файла с учетом расходов, листинг кода, и вывод в консоль, с демонстрацией работоспособности программы.

```python
def main():
    j = []
    while True:
        print("1. Учет расходов")
        print("2. Расходы")
        print("3. Выход")
        vibor = input("Выберите пункт: ")

        if vibor == '1':
            rashod = input("Введите категорию: ")
            sum = input("Cумма: ")
            j.append(f"{rashod}: {sum}")
        elif vibor == '2':
            if not j:
                print("Расходов таки нет.")
            else:
                print("Таки расходы:")
                for i in j:
                    print(i)
        elif vibor == '3':
            with open('rashods.txt', 'w', encoding='utf-8') as file:
                for i in j:
                    file.write(i + '\n')
            print("Файл 'rashods.txt' сохранен")
            break
        else:
            print("Ошибка.")

if __name__ == "__main__":
    main()
```

### Результат
![Меню](https://github.com/DarkArex/Labaratornaya/blob/Tema-7/picture/2.png)
![Меню](https://github.com/DarkArex/Labaratornaya/blob/Tema-7/picture/2.1.png)

## Выводы
В ходе выполнения данной работы, я изучил возможности работы с внешними текстовыми файлами. А также создал программу которая позволяет пользователям учитывать и просматривать свои расходы, а также сохранять данные в файл.
  
## Самостоятельная работа №3
### Имеется файл input.txt с текстом на латинице. Напишите программу, которая выводит следующую статистику по тексту: количество букв латинского алфавита; число слов; число строк.

```python
def Stats(text):
    letters = 0
    words = 0
    lines = 0

    with open(text, 'r') as file:
        for line in file:
            letters += sum(c.isalpha() for c in line)
            words += len(line.split())
            lines += 1
    print(f'Input file contains:')
    print(f'{letters} letters')
    print(f'{words} words')
    print(f'{lines} lines')
if __name__ == "__main__":
    text = "input.txt"
    Stats(text)
```

### Результат
![Меню](https://github.com/DarkArex/Labaratornaya/blob/Tema-7/picture/3.png)
![Меню](https://github.com/DarkArex/Labaratornaya/blob/Tema-7/picture/3.1.png)

## Выводы
В данной работе я изучил как реализовать чтение файла, как провести анализ текста

## Самостоятельная работа №4
### Напишите программу, которая получает на вход предложение, выводит его в терминал, заменяя все запрещенные слова звездочками * (количество звездочек равно количеству букв в слове). Запрещенные слова, разделенные символом пробела, хранятся в текстовом файле input.txt. Все слова в этом файле записаны в нижнем регистре. Программа должна заменить запрещенные слова, где бы они ни встречались, даже в середине другого слова. Замена производится независимо от регистра: если файл input.txt содержит запрещенное слово exam, то слова exam, Exam, ExaM, EXAM и exAm должны быть заменены на ****.

```python
def TextForBan(text):
    with open(text, 'r') as file:
        wordsforban = file.read().split()
    return set(wordsforban)
def banhammer(sentence, wordsforban):
    words = sentence.split()
    cens = []
    for word in words:
        BAN = word.lower()
        if BAN in wordsforban:
            BAN = '*' * len(word)
            cens.append(BAN)
        else:
            cens.append(word)
    return ' '.join(cens)
text = "input7.4.txt"
sentence = "Hello , world! Python IS the programming language of thE future. My EMAIL is.... PYTHON is awesome!!!!"
wordsforban = TextForBan(text)
res = banhammer(sentence, wordsforban)
print("Замененное предложение:")
print(res)
```

### Результат
![Меню](https://github.com/DarkArex/Labaratornaya/blob/Tema-7/picture/4.png)
![Меню](https://github.com/DarkArex/Labaratornaya/blob/Tema-7/picture/4.1.png)

## Выводы
Я изучил, как читать данные из файла, работать с функциями для обработки текста и использовать условные операторы для цензурирования определенных слов в предложении.

## Самостоятельная работа №5
### Самостоятельно придумайте и решите задачу, которая будет взаимодействовать с текстовым файлом.
### Программа должна создать файл с именем random.txt и записать в него случайные числа от 1 до 10 в количестве 25 штук.

```python
def CalcWords(doc):
    wordcount = {}
    with open(doc, 'r') as file:
        text = file.read()
        words = text.split()
        for i in words:
            i = i.strip('.,!?()[]{}"\'').lower()
            if i in wordcount:
                wordcount[i] += 1
            else:
                wordcount[i] = 1
    return wordcount
doc = "text.txt"
res = CalcWords(doc)
for i, count in res.items():
    print(f'{i}: {count}')
```

### Результат
![Меню](https://github.com/DarkArex/Labaratornaya/blob/Tema-7/picture/5.png)
![Меню](https://github.com/DarkArex/Labaratornaya/blob/Tema-7/picture/5.1.png)

## Выводы
В данной работе, я изучил как создавать функции, работать с файлами, разбивать текст на слова, и вести подсчет слов в тексте с использованием словаря.

## Общие выводы по теме
Работа с файлами является важной частью программирования, так как позволяет сохранять, загружать и обмениваться данными между разными частями программы или между разными программами. Понимание функций и методов для работы с файлами позволяет программистам эффективно управлять данными и создавать более функциональные и полезные приложения.
