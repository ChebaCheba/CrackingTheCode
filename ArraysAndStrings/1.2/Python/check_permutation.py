def check_perm(str1, str2):
    temp = set()
    str1 = str1.replace(" ", "")
    str2 = str2.replace(" ","")
    for i in range(len(str1)):
        if str1[i] not in temp:
            temp.add(str1[i])
        else:
            temp.remove(str1[i])
        if str2[i] not in temp:
            temp.add(str2[i])
        else:
            temp.remove(str2[i])
    if not temp:
        return True
    return False

if __name__=="__main__":
    str1 = input("Introduzca el primer string\n")
    str2 = input("Introduzca el segundo string\n")
    is_perm = check_perm(str1,str2)
    if is_perm:
        print("Es una permutacion")
    else:
        print("No es una permutacion")