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