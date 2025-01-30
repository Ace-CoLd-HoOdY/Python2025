#30.01.2025
#If letter in word - print it

import sys
import time

def slow_print(text, delay=0.06):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


slovnik = [
    "Макс",
    "Машина",
    "Кіт",
    "Захар",
    "Анаконда",
    "Чорний",
    "Великий",
    "Фрукт",
    "Їжа",
    "Гра",
    "Вода",
]

letter = input("Enter any letter:  ")

for i in slovnik:
    if letter in i.lower():
        slow_print(i) 