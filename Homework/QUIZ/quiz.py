import Interaction_With_Questions as Inter

# Подключаем файлы с вопросами, вариантами ответов и правильными ответами
file_with_question = open('Question.txt', 'r', encoding="utf-8")
file_with_choice = open('Answer_Options.txt', 'r', encoding="utf-8")
file_with_correct_answers = open('Correct_Answers.txt', 'r')
file_with_points = open('Points.txt', 'r')


list_of_answers_from_user = []      # лист для записи тех ответов, который вводит пользователь

# Лист где сохраняются количество вариантов ответов на каждый вопрос
list_of_number_of_answers_to_the_question = Inter.check_share_of_variants_of_answers(file_with_choice)
file_with_choice.close() # Закрытие файла для того,чтобы можно было с ним ещё раз поработать
index_list = 0

# Печать всех вариантов
file_with_choice = open('Answer_Options.txt', 'r', encoding="utf-8")
for string in file_with_question:
    Inter.print_strings(string)     # печатаем вопрос
    for i in range(list_of_number_of_answers_to_the_question[index_list]):
        Variants_for_the_answer = file_with_choice.readline()                           # считываем строку
        Inter.print_strings(Variants_for_the_answer)                                    # Печатаем ответы
        # Проверка коректности введённых ответов
        Inter.work_with_answers(list_of_answers_from_user, i, int(list_of_number_of_answers_to_the_question[index_list]) - 1)

    index_list += 1

# выводим кол-во правильных, неправильных заданий, число баллов, которое получил пользователь за прохождение тестирования
numbers_of_points,right_answers,wrong_answers,total_sum_points = Inter.checking_answers(file_with_points, list_of_answers_from_user, file_with_correct_answers)

Inter.print_strings(f"Вы дали {right_answers} правильных ответов\n")
Inter.print_strings(f"Количество неправильных ответов равно {wrong_answers}\n")
Inter.print_strings(f"Число баллов за тест равно: {numbers_of_points} из {total_sum_points} возможных\n")

# Закрытие всех файлов при завершении работы с файлами
file_with_question.close()
file_with_choice.close()
file_with_correct_answers.close()
file_with_points.close()