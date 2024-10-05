my_list = [(20, 'зажигалка'), (100, 'компас'), (100, 'бутерброды'), (100, 'мешок'), (400, 'бинокль'), (1000, 'термос'), (1000, 'палатка')]
ves = int(input('Введите вес рюкзака'))
my_list = my_list[::-1] # развернули в обратную сторону
k = 0
for i in range(len(my_list)):
    if my_list[i][0] <= ves:
        print(my_list[i][1])
        ves -= my_list[i][0]
        k += my_list[i][0]
    #print(list_1[i][0])
print("Итоговый вес:",k)
