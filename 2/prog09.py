# Prog09: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero or ending five.

for i in range(101):
    if i % 10 != 5 and i % 10 != 0:
        print(i)