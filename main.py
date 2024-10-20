import question
import random

def replacing(my_password, replace_symbols_on_numbers):
    """ Если пользователю надо, то функция заменяет определённые буквы на цифры """
    if replace_symbols_on_numbers == 'Н':
        return my_password

    #  Словарь букв, которые надо заменить на цифры
    symbols_replacing = {
        'i': '1', 'f': '4', 'o': '0', 'e': '2', 'k': '9',
        'D': '7', 'S': '8', 'B': '5', 'T': '6', 'N': '3'
    }
    # Замена всех нужных букв на цифры с помощью итератора
    for element in my_password:
        if element in symbols_replacing:
            my_password = my_password.replace(element, symbols_replacing[element])
    return my_password


def generate_password(length, replace_symbols_on_numbers):
    """Функция генерирует пароль"""

    # Лямбда функции для составления списка доступных символов для генерации пароля
    alphabet = lambda \
            Registr: 'ABCDEFGHIGKLMOPQRSTYWXVZabcdefghigklmopqrstywxvz' if Register == 'Д' else 'abcdefghigklmopqrstywxvz'
    numbers = lambda \
            The_precence_of_numbers: '0123456789' if The_precence_of_numbers == 'Д' else ''
    special_characters = lambda \
            The_precence_of_special_characters: '-!#$&*?' if The_precence_of_special_characters == 'Д' else ''

    # Составление списка доступнызх символов для генерации пароля
    symbols_for_generation = ''
    symbols_for_generation = symbols_for_generation + alphabet(Register)
    symbols_for_generation = symbols_for_generation + numbers(The_precence_of_numbers)
    symbols_for_generation = symbols_for_generation + special_characters(The_precence_of_special_characters)

    # Составление пароля с помощью доступных символов и функции random
    my_password = ''.join(random.choice(symbols_for_generation) for _ in range(length))
    my_password = replacing(my_password, replace_symbols_on_numbers)

    return my_password


# Взаимодействие с пользователем


amount_of_password = question.User_numbers("Сколько паролей надо?\n")
len_of_password = question.User_numbers("Сколько символов длина пароля?\n")
Register = question.User_answers("Включить разный регистр символов (д/н)?\n")
The_precence_of_numbers = question.User_answers("Включить цифры (д/н)?\n")
The_precence_of_special_characters = question.User_answers("Включить специмволы (д/н)?\n")
replace_symbols_on_numbers = question.User_answers("Заменить некоторые буквы на цифры (д/н)?\n")


# Результат генерации пароля и печать
print("Ваши пароли:")
for i in range(amount_of_password):
    password = generate_password(len_of_password, replace_symbols_on_numbers)
    print(password)
