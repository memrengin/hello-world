def compare(x,y):
    if x == y:
        return True
    else:
        return False

if __name__  ==  "__main__":

    my_list = []
    my_list2 = []
    result_list = []
    text1 = input("1. listede yer alacak sayıları giriniz: ")
    text2 = input("2. listede yer alacak sayıları giriniz: ")

    for i in text1:
        if " " in i:
            pass
        else:
            my_list.append(i)

    for i in text2:
        if " " in i:
            pass
        else:
            my_list2.append(i)

    for i in my_list:
        counter = 0
        for y in my_list2:
            if compare(i, y) == False:
                counter += 1
                if counter == len(my_list2):
                    result_list.append(i)

    print(set(result_list))



