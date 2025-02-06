# 16.01.2025


# #Timer
# for minute in range(60):
#     for second in range(60):
#         if second % 2 == 0:
#             continue
#         print(minute, ":", second

#3 x n rectangle
# n = int(input("Enter width: "))
# for i in range (n):
#     for j in range (3):
#         print(n, end="")
#     print()

#Number pyramid
n = int(input("Amount of numbers: "))
for i in range (1, n+1):
    for j in range (i):
        print(i, end=" ")
    print()