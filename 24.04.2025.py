#24.04.2025


#Perimeter of a rectangle and draws
widths = int(input("Enter the widths: "))
height = int(input("Enter the height: "))

for i in range (height):
    print("*" *widths)

print("The perimeter is: ", 2*(widths + height))


#Perimeter with function def
# def perimeter(w, h):
#     return 2*(w+h)
# print(perimeter(5,6))