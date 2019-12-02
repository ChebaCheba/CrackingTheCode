def check_unique(string):
    unique = dict()
    for letter in string:
        if letter not in unique:
            unique[letter]=True
        else:
            return False
    return True

if __name__=="__main__":
    string = input("Introduce a string\n")
    is_unique = check_unique(string)
    if is_unique:
        print("The string has only unique characters")
    else:
        print("The string has repeated characters")