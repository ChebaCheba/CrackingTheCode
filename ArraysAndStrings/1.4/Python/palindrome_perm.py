def is_palindrome(string):
    temp = set()
    if len(string)<2:
        return False
    stripped = string.replace(' ', '')
    for i in string:
        if not i.isspace():
            if i.lower() not in temp:
                temp.add(i.lower())
            else:
                temp.remove(i.lower())
    if len(temp)<2:
        return True
    return False

if __name__=="__main__":
    string = input("Introduce string\n")
    is_pal = is_palindrome(string)
    if is_pal:
        print(string, "is a palindrome permutation")
    else:
        print(string, "is not a palindrome permutation")