import time

def timing_decorator(function):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = function(*args, **kwargs)
        end_time = time.time()
        print(f"Время выполнения функции Фибоначи: {end_time - start_time} секунд")
        return result
    return wrapper

@timing_decorator
def fibonacci():
    fib1 = fib2 = 1
    for i in range(2, 200):
        fib1, fib2 = fib2, fib1 + fib2
    print(fib2, end=' ')

if __name__ == '__main__':
    fibonacci()