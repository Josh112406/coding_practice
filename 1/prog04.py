#Prog04. islower() check if all characters of the string is on lower case. Create a program that do the same functionality without using islower() function.
#use lowercase list
def islower(text: str):
    lowercase_list = [x for x in 'abcdefghijklmnopqrstuvwxyz']
    
    for char in text:
        if char.isalpha() and not char in lowercase_list:
            return False
    return True
    
print(islower("32fhFkjsd928ydf"))