
import random
number = random.randint(1, 50)
live = 4
print(number)

def not_integer(x):
    try:
        int(x)
        return True
    except ValueError:
        return print("Sayı girmedin! Oyun bitti.")

def in_range(x):

    x = int(x)
    if x < 0 or 50 < x:
        return print("Girdiğin sayı 1 ile 50 arasında değil!")
    else:
        return True

def game(x):
    global live
    x = int(x)
    while live != 0:
        x = int(x)
        if x == number:
            print("Tebrikler, doğru tahmin ettin!")
            break
        elif x < number:
            print("Girdiğin sayı, tahmin ettiğim sayıdan küçük.\nKalan tahmin hakkı {}".format(live))
            live = live - 1
            x = input("Tekrar tahmin eder misin?\n")
            if not_integer(x) != True or in_range(x) != True:
                break
            else:
                continue
        else:
            print("Girdiğin sayı, tahmin ettiğim sayıdan büyük.\nKalan tahmin hakkı {}".format(live))
            live = live - 1
            x = input("Tekrar tahmin eder misin?\n")
            if not_integer(x) != True or in_range(x) != True:
                break
            else:
                continue
if __name__  ==  "__main__":

    guess = input("Merhaba, Tahmin oyununa hoş geldin!\n1'den 50'ye kadar bir sayı tuttum!\n5 hakkınız bulunuyor. Tahmin eder misin?\n")

    if not_integer(guess) == True and in_range(guess) == True:
        game(guess)
