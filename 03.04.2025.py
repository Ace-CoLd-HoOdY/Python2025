#03.04.2025
from time import sleep

#Delete each number from the end
# numbers = [1, 2, 3, 4, 5]

# while numbers:
#     print(*numbers)
#     numbers.pop()

# print("Can`t go further")

#User enters 7 numbers and they are being deleted step by step
numbers = []

for i in range (1, 8):
    number = int(input(f"Enter your {i} number: "))
    numbers.append(number)

while numbers:
    sleep(1)
    print(*numbers)
    numbers.pop()