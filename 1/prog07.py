#Prog07. zfill() add zero characters at the beginning of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using zfill() function.
#zfill() also ignores + or - at beginning and is placed after it

def zfill(text: str, width: int):
    return f"{text[0]}{width * "0"}{text[1:]}" if text[0] in ("+", "-") else f"{width * "0"}{text}"
