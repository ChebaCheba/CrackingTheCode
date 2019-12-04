def is_rotation(str1, str2):
    concat = str2+str2
    if str1 in concat:
        return True
    return False

if __name__=="__main__":
    str1 = input("Introduce the normal string\n")
    str2 = input("Introduce the rotated string\n")
    is_rot = is_rotation(str1, str2)
    if is_rot:
        print(str2,"is a rotation of",str1)
    else:
        print(str2,"is not a rotation of",str1)