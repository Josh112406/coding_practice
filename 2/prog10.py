# Prog10: Create a program that ask user to input 2 numbers. Print all the numbers between the two numbers.
num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))
if num_1 < num_2:
    for i in range(num_1, num_2 - 1):
        print(i + 1)
elif num_1 > num_2:
    for i in range(num_1 - 1, num_2, -1):
        print(i)
elif num_1 == num_2:
    print("The numbers are the same")
else:
    print("There is nothing in between")