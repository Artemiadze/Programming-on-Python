def print_strings(question):
    """Функция принимает строки для печати (вопросы, варианты и т.д.)"""
    print(question, end='')


def work_with_answers(answer_for_printing,list_of_answers_from_user, index_of_iteration):
    """Функция проверяет кооректность вводимого номера варианта"""
    Number_of_possible_answer = frozenset([1, 2, 3, 4]) # множество для сравнения корректности вводимого номера варианта
    if index_of_iteration == 3:
        while True:
            answer = input("Выберите верный вариант ответа:\n")
            if answer.isdigit() and int(answer) in Number_of_possible_answer:
                list_of_answers_from_user.append(int(answer))
                break
            else:
                print("Некорректный ввод!")
