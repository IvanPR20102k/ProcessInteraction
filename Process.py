from multiprocessing import Process, Queue
from datetime import datetime


def add_to_queue(q, inp: str):
    try:
        if inp.isalpha():
            print("Введены буквы")
        q.put(inp.split())
    except Exception as e:
        print(e)


def to_power(q):
    while True:
        item: list = q.get()
        result: int = int(item[0]) ** int(item[1])
        summ: int = 0
        i: int = 0
        while i <= result:
            summ += i
            i += 1
        with open("./calculations.txt", 'a') as file:
            file.write(f"{datetime.now()} {item[0]}^{item[1]} = {result} ; Сумма от 0 до {result} = {summ}\n")


if __name__ == "__main__":
    q = Queue()
    p = Process(target=to_power, args=(q,))
    p.start()
    while True:
        number_str: str = input("Введите число и степень через пробел:")
        add_to_queue(q, number_str)
