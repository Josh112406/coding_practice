#Prog08. count() return how many time the function parameter appear in the string. Create a program that do the same functionality without using count() function.

#works but slow
# def count(text: str, substring: str):
#     found = []
#     index = 0
#     for _ in range(len(text)):
#         string = text.find(substring, index) 
#         if string != -1:
#             found += [string]
#             index += 1
            

#     return len(set(found))

#try to create more efficient algorithm
def count(text: str, substring: str):
    count = 0
    


print(count("sub sub sub sub", "sub"))