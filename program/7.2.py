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