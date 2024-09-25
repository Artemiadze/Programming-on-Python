# Власов Артём 23КНТ2

min = 1
max = 1000
len = (max + min)//2
print("Вы загадали это число :", len, "?")
print("Введите 'ДА' или 'НЕТ'")
answer = input()
answer = answer.capitalize()                                 #функция для стандартизации регистра : ДА,дА -> Да; нет -> Нет

#Проверка на ошибку в команде, которую вводит пользователь
while answer != 'Да' and answer != "Нет":
    print("Пожалуйста, введите команду корректно")
    answer = input()
    answer = answer.capitalize()

if answer == 'Да':
    print()                                                  #пустая строка для эстетики
    print("УРА! Я угадал ваше число! И оно равно", len)
else:
    while answer != "Да":
        print()                                              #пустая строка для эстетики
        print("Ваше число больше чем", len, "?")
        print("Введите 'МЕНЬШЕ' или 'БОЛЬШЕ'")
        answer_about_size = input()
        answer_about_size = answer_about_size.capitalize()

        #Проверка на ошибку в команде
        while answer_about_size != 'Больше' and answer_about_size != 'Меньше':
            print("Пожалуйста, введите команду корректно")
            answer_about_size = input()
            answer_about_size = answer_about_size.capitalize()

        if answer_about_size == 'Больше':
            min = len
        elif answer_about_size == 'Меньше':
            max = len
        len = (max + min) // 2

        print()                                               #пустая строка для эстетики
        print("Вы загадали это число :", len, "?")
        print("Введите 'ДА' или 'НЕТ'")
        answer = input()
        answer = answer.capitalize()

        #Проверка на ошибку в команде
        while answer != 'Да' and answer != "Нет":
            print("Пожалуйста, введите команду корректно")
            answer = input()
            answer = answer.capitalize()

    print()                                                    #пустая строка для эстетики
    print("УРА! Я угадал ваше число! И оно равно", len)