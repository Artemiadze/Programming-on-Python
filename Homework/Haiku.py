import re
from colorama import Fore, Style


def check_haiku(candidate_for_haiku):
    """ Функция принимает строку, делит её на трёхстишье и проверяет на признаки хайку"""

    # Слоги и проверка на первый признак Хайку (проверка на 3 строки)
    syllables = [0, 0, 0]
    lines = candidate_for_haiku.split('/')
    if len(lines) != 3:
        return "Не хайку. Должно быть 3 строки."

    # Итерация по строкам текста для подсчета слогов (гласных)
    for i in range(3):
        for symbol in lines[i]:
            if symbol.lower() in 'аеёиоуыэюя':
                syllables[i] += 1

    if syllables == [5, 7, 5]:
        return "Хайку!"
    else:
        # Если ранняя ошибка в последней строке то выведется что ошибка в 3 строке
        wrong_number = 3
        # Если ранняя ошибка раньше 3 или 2 строки,
        # то проверка автоматически заменит на более раннюю ошибку и выведет номер строки с ошибкой верно
        if syllables[1] != 7:
            wrong_number = 2
        if syllables[0] != 5:
            wrong_number = 1

        # Неверное число слогов для того, чтобы называться хайку
        return f"Не хайку. В {wrong_number} строке слогов не {5 if wrong_number != 2 else 7}, а {syllables[wrong_number-1]}."


def print_result(tercet, result):
    """ Функция печатает трёхстишье (tercet) и результат проверки на хайку"""

    tercet = re.sub(r' / ', r'\n', tercet)  # Заменеям все вхождения " / " на enter
    print(Fore.CYAN + tercet)                           # Окрашивает трёхстишье в бирюзовый
    if result == "Хайку!":
        print(Fore.GREEN + result+"\n")                 # Окрашивает результат в зелёный (Хайку!)
    else:
        print(Fore.LIGHTRED_EX + result + "\n")         # Окрашивает результат в красный (не хайку!)


def write_check_haiku(file_for_checking):
    """ Функция запрашивает файл с стихами, проверяет трёхстишья на хайку
     и записывает результат в файл text_haiku.txt"""

    # Конечный список всех строк с их результатом проверок на хайку
    results = []

    # Итерация по трёхстишьям для проверки их на хайку
    for tercet in file_for_checking:
        results.append(tercet.strip())               # Добавляем в конечный список трёстишье без пробела (.strip)
        results.append(check_haiku(tercet.strip()))  # Добавляем в конечный список  результат проверки трёхстишья
        print_result(tercet.strip(), check_haiku(tercet.strip()))
        results.append("")                           # Добавляем в конечный список красивый отступ для эстетики резу

    # Запись результата проверки стиха на хайку
    with open('test_haiku.txt', 'w', encoding='utf-8') as file_with_result:
        for result in results:
            file_with_result.write(result + '\n')


# Открытие файла с текстом хайку
with open('haiku.txt', 'r', encoding='utf-8') as file:
    haiku_text = file.readlines()
    write_check_haiku(haiku_text)
