def compare(x,y):
    try:
        if x == y:
            return True
    except:
        return None

if __name__  ==  "__main__":

    my_list = []
    my_list2 = []
    text_back = ""
    vowels = ["a","e","ı","i","o","ö","u","ü"]
    text = input("Tişikkirlir Sipirmin: ")

    for i in text:
        my_list.append(i)

    for i in range(len(my_list)):
        count = 0
        for y in range(len(vowels)):
            if compare(my_list[i],vowels[y]) == True:
                my_list2.append("i")
            else:
                count += 1
                if count == 8:
                    my_list2.append(my_list[i])

    for i in my_list2:
        text_back += i
    print(text_back)


