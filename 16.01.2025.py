# 16.01.2025


#Сума всіх парних чисел
n = int(input("Enter any number: "))
sum = 0
while n != 0:
    if n % 2 == 0:
        sum += n % 10
    n //= 10
print(sum)