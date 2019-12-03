def one_away(str1, str2):
    if abs(len(str1)-len(str2))>1:
        return False
    count1 = count2 = 0
    diff = 0
    while count1 < len(str1) and count2 < len(str2):
        if diff > 1:
            return False
        if str1[count1] == str2[count2]:
            count1 += 1
            count2 += 1
        else:
            if str1[count1+1] == str2[count2+1]:
                count1 += 1
                count2 += 1
                diff += 1
            elif str1[count1+1] == str2[count2]:
                count1 += 1
                diff += 1
            elif str1[count1] == str2[count2+1]:
                count2 += 1
                diff += 1
            else:
                return False
    return True

if __name__=="__main__":
    str1 = input("Introduce first string\n")
    str2 = input("Introduce second string\n")
    is_one = one_away(str1, str2)
    if is_one:
        print("True")
    else:
        print("False")