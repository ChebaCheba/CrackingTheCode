def check_unique(string):
    unique = dict()
    for letter in string:
        if letter not in unique:
            unique[letter]=True
        else:
            return False
    return True

def _quick_sort(string):
    list_string = list(string)
    _pivot(list_string)
    return list_string

def _pivot(list_string, j = 0, p = None):
    i = j-1
    if not p:
        p = len(list_string) -1
    print(j,p)
    if not j>=p:
        for k in range(j, p):
            if list_string[k] <= list_string[p]:
                i += 1
                list_string[i],list_string[k] = list_string[k], list_string[i]
        list_string[i+1], list_string[p]=list_string[p], list_string[i+1]
        _pivot(list_string, j = j, p = i)
        _pivot(list_string, j = i+2, p = p)

def check_unique_sort(string):
    sorted_string = _quick_sort(string)
    print(sorted_string)
    for i in range(len(sorted_string)-2):
        if sorted_string[i]==sorted_string[i+1]:
            return False
    return True

if __name__=="__main__":
    string = input("Introduce a string\n")
    #is_unique = check_unique(string)
    is_unique = check_unique_sort(string)
    if is_unique:
        print("The string has only unique characters")
    else:
        print("The string has repeated characters")