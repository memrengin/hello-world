
my_list = []
text = input("Tersten yazılmasını istediğiniz yazıyı giriniz: ")
# print(type(text))

for i in text:
    my_list.append(i)
my_list.reverse()
# print(my_list)

text_reversed = ""
for i in my_list:
    text_reversed += i
print(text_reversed)



