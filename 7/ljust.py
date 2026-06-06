# Prog06. ljust() add space characters at the end of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using ljust() function.

def ljust(string: str, count: int, value: str = " ") -> str:
    if count <= len(string):
        return string
    
    return string + (count - len(string)) * value
