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

# Укажите путь к вашему файлу
file = 'text 7.1.txt'

calc = ShetSlow(file)
popular, count = PopularWord(file)

print(f'Количество слов в файле: {calc}')
print(f'Самое часто встречающееся слово: "{popular}" (встречается {count} раз)')