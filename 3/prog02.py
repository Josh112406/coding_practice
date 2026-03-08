# Prog02: Create a program that ask user to input 2 numbers. Print "Equal" when the numbers are the same.
#same as prog01, just reversed the condition
#short version, take input first then compare
num_1 = float(input("Enter first number: "))
num_2 = float(input("Enter second number: "))
print("Equal" if num_1 == num_2 else "Not Equal")

#longer version
num_1 = float(input("Enter first number: "))
num_2 = float(input("Enter second number: "))
if num_1 == num_2:
    print("Equal")
else:
    print("Not Equal")