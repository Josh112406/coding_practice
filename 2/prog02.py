# Prog02: Create a program that ask user to input 2 numbers. Print "Not Equal" when the numbers are not the same
#short version, take input first then compare
num_1 = float(input("Enter first number: "))
num_2 = float(input("Enter second number: "))
print("Not Equal" if num_1 != num_2 else "Equal")

#longer version
num_1 = float(input("Enter first number: "))
num_2 = float(input("Enter second number: "))
if num_1 != num_2:
    print("Not Equal")
else:
    print("Equal")