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