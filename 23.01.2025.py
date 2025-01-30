#23.01.2025


#Найменьший дільник
n = int(input("Enter any number: "))
for i in range(2, n + 1):
    if n % i == 0:
        print("Your smallest devisor is: ", i)
        break


#Сума 10 числ який зупиняеться як тільки побаче від'ємне число
sum = 0
for i in range (10):
    number = int(input("Enter any number: "))
    if number > 0:
        sum += number
        print(sum)
    else:
        print(sum)
        break