# Создаем пустой файл
with open('nonetext.txt.txt', 'w') as empty:
    pass
with open('textthistext.txt.txt', 'w') as full:
    full.write("Таки текста есть")
def Chek(doc):
    try:
        with open(doc, 'r') as file:
            text = file.read()
        if not text:
            raise Exception("Таки файл пустой")
        return text
    except Exception as e:
        print(f"Ошибка: {e}")
print("Содержимое пустого файла:")
nonetext = Chek('nonetext.txt.txt')
print("\nСодержимое файла с информацией:")
textthistext = Chek('textthistext.txt.txt')
if textthistext:
    print(textthistext)