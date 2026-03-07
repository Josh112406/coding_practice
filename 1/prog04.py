#Prog04. islower() check if all characters of the string is on lower case. Create a program that do the same functionality without using islower() function.
#use lowercase list
def islower(text: str):
    lowercase_list = [x for x in 'abcdefghijklmnopqrstuvwxyz']
    for char in text:
        if char.isalpha() and char in lowercase_list:
            return True
        return False
    
print(islower("Hfklsih"))