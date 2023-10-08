import random
def play():
    x = random.randint(1, 6)
    print(f"Кубик: {x}")
    if x in (5, 6):
        print("Вы победили")
    elif x in (3, 4):
        print("Продолжаем играть...")
        play()
    else:
        print("Вы проиграли")
if __name__ == "__main__":
    play()
