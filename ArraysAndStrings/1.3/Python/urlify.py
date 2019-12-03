def urlify(string, length):
    count = 0
    url = ""
    while count < length:
        if string[count].isspace():
            url += "%20"
        else:
            url += string[count]
        count+=1
    return url

if __name__=="__main__":
    string = input("Introduce input toURLify\n")
    length = int(input("Introduce length\n"))
    url = urlify(string, length)
    print("URL: ", url)