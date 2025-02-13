#13.02.2025


#Multiplication table except for 5
# for i in range(1, 11):
#     if i == 5:
#         continue
#     for j in range(1, 11):
#         print(i, "*", j, "=", i*j)

#Pyramid from * but it skips even stars
# for i in range(1, 11):
#     if i % 2 == 0:
#       continue
#     print('*' * i)

#Guess num 7
# num = 7
# while True:
#   a = int(input('Введіть число: '))
#   if a != num:
#     continue
#   else:
#     print("Ви вгадали!")
#     break

#Smallest odd divider
n = int(input("Enter any number: "))
for i in range(2, n + 1):
    if n % i == 0:
        if i % 2 != 0:
            print("Your smallest odd divider is: ", i)
            break
        else:
            print("No odd divider; only even one exists: ", i)
            break