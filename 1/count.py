#Prog08. count() return how many time the function parameter appear in the string. Create a program that do the same functionality without using count() function.

#try to create more efficient algorithm
def count(text: str, substring: str) -> int:
    count = 0
    len_substring = len(substring) 
    i = 0
    while i <= len(text) - len_substring:
        if text[i : i + len_substring] == substring:
            count += 1
            i += len_substring
    return count


print(count("aaaa", "aa"))

