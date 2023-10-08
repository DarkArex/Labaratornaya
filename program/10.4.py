import time
def Time(x):
    def cover(*args, **kwargs):
        start = time.time()
        res = x(*args, **kwargs)
        end = time.time()
        work = (end - start) * 1000
        print(f"Функция {x.__name__} выполнилась за {work:.2f} мс")
        return res
    return cover
@Time
def slow():
    time.sleep(2)
    print("Медленная функция")
@Time
def fast():
    time.sleep(0.3)
    print("Быстрая функция")
slow()
fast()