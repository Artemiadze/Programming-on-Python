def print_strings(question):
    """ Функция принимает строки для печати (вопросы, варианты и т.д.) """
    print(question, end='')


def work_with_answers(list_of_answers_from_user, index_of_iteration, stop_index):
    """ Функция получает список для хранения введённых пользователем ответов, индекс варианта ответа и индекс последнего
    варианта ответа, который выводит компьютер перед тем, как запросить у пользователя ответ. Затем проверяет коректность
    вводимого номера варианта и запоминает ответ, который ввёл пользователь """

    number_of_possible_answer = frozenset(
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])  # множество для сравнения корректности вводимого номера варианта

    # если индекс выводимого вопроса равен номеру последнего вопроса, то запрашиваем ответ
    if index_of_iteration == stop_index:
        while True:
            answer = input("Выберите верный вариант ответа:\n")
            if answer.isdigit() and int(answer) in number_of_possible_answer:        # Проверка на корректность ввода
                list_of_answers_from_user.append(int(answer))                        # Добавляет введённый ответ
                break
            else:
                print("Некорректный ввод!")


def check_share_of_variants_of_answers(file_with_choice):
    """ Функция получает файл с вариантами ответов, проходится по файлу,
     сохраняет в лист количество вариантов ответов на каждый вопрос и возвращает этот лист"""
    list_of_number_of_answers_to_the_question = []
    k = 1
    first_line = file_with_choice.readline().rstrip('\n')           # первая строка файла с вариантами ответов
    for line in file_with_choice:                                   # считаем кол-во вариантов для каждого вопроса
        if int(line[0]) != 1 or line == first_line:
            # если вариант не первый или это самая первый вариант первого вопроса
            k += 1
        else:
            # если встретили 1, значит мы попали на варианты другого вопроса
            list_of_number_of_answers_to_the_question.append(k)
            k = 1
    list_of_number_of_answers_to_the_question.append(k)    # добавляем кол-во ответов на последний вопрос

    return list_of_number_of_answers_to_the_question


def checking_answers(file_with_points, list_of_answers_from_user, file_with_correct_answers):
    """ Функция получает файл с баллами на каждое задание, список ответов от пользователя, файлс правильными ответами
    сверяет ответы пользователя и правильные ответы на тест, сравнивает ответы пользователя с ответами из базы данных,
    после этого возвращает количество баллов, затем кол-во правильных ответов и кол-во неправильных ответов, и ещё
    максимальная сумма баллов, которую можно было получить впринципе"""

    right_answers = 0      # кол-во правильных ответов
    wrong_answers = 0      # кол-во неправильных ответов
    total_sum_points = 0   # максимальная сумма баллов в файле file_with_points
    numbers_of_points = 0  # Число очков
    index_of_list_in_function = 0  # индекс итерации листа с ответами пользователя

    # теперь этот файл доступен для построчного чтения, где номер строки это индекс (т.е.index_of_list_in_function)
    point = file_with_points.readlines()

    # Сверяем ответы и считаем баллы
    for line in file_with_correct_answers:
        total_sum_points += int(point[index_of_list_in_function])
        # проверка на правильность ответов пользователя
        if int(line) == list_of_answers_from_user[index_of_list_in_function]:
            numbers_of_points += int(point[index_of_list_in_function])
            right_answers += 1
        else:
            wrong_answers += 1
        index_of_list_in_function += 1
    return numbers_of_points, right_answers, wrong_answers, total_sum_points
