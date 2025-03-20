#20.03.2025


#Fruits
# fruits = ["apple", "lemon", "pear", "banana", "orange"]
# print (fruits)
# print (*fruits)

# print (fruits[2])
# print (fruits[-1])

# fruits.append("mango")
# print (fruits)

# fruits.insert(1, "kiwi")
# print (fruits)


#Add a number to a list if its even
# numbers = [1, 2, 3, 5, 6, 7, 8, 9, 10]
# newnumber = int(input("Enter any number: "))
# if newnumber % 2 == 0:
#     print ("Old list: ", *numbers)
#     numbers.append(newnumber)
#     print ("New list: ", *numbers)
# else:
#     print("Sorry, it`s not even")


#Which fruit to delete?
fruits = ["apple", "lemon", "pear", "banana", "orange"]
print (fruits)
delete = int(input("Which fruit do you want do delete? (from zero): "))
fruits.pop(delete)
print (fruits)