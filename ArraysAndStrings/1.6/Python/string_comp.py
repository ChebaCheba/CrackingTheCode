def string_comp(strng):
    letter_count = 0
    temp = string[0]
    comprehension = ''
    for letter in string:
        if letter == temp:
            letter_count += 1
        else:
            comprehension += temp+str(letter_count)
            temp = letter
            letter_count = 1
    comprehension += temp+str(letter_count)     
    if len(string)>len(comprehension):
        return comprehension
    return string

if __name__=="__main__":
    string = input("Introduce string\n")
    string_c = string_comp(string)
    print(string_c)