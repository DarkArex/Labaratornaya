class Erorr(Exception):
    def __init__(self, text):
        super().__init__(text)
def Proverka(x):
    if x < 0:
        raise Erorr("Значение не может быть отрицательным.")
    elif x == 0:
        raise Erorr("Значение не может быть равным нулю.")
    else:
        print("Значение допустимо.")

try:
    Proverka(-5)
except Erorr as e:
    print(f"Поймано исключение: {e}")
else:
    print("Программа успешно завершена.")

def Obrabotka(y):
    if not y:
        raise Erorr("Невозможно обработать пустые данные.")
    print("Данные обработаны.")

try:
    y = []  #
    Obrabotka(y)
except Erorr as e:
    print(f"Поймано исключение: {e}")
else:
    print("Программа успешно завершена.")