#Prog09. index() return the first location of the function parameter in the string. Create a program that do the same functionality without using index() function.
#same logic as prog08 but slightly tweaked
#return index instead of incrementing
def index(text: str, substring: str) -> int:
    if not substring:
        return 0
    
    len_substring = len(substring)
    for i in range(len(text)):
        if text[i : i + len_substring] == substring:
            return i
    raise ValueError
        
