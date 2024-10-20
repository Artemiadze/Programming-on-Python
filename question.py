def User_numbers(question):
    ''' По вашему вопросу возвращает число для работы с генерацией пароля '''
    print(question)
    while True:
        number1 = input()
        if number1.isdigit():
            return int(number1)
        print("Ошибка в типе вводимых данных!")


def User_answers(question):
    ''' Возвращает Да/Нет от пользователя на ваш вопрос '''
    print(question)
    while True:
        answer = input()
        if answer.upper() == 'Д' or answer.upper() == 'Н':
            return answer
        print("Введите буквы 'д' для солгасия или 'н' для отказа")