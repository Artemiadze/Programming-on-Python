import Interaction_With_Questions as Inter

# Подключаем файлы с вопросами, вариантами ответов и правильными ответами
file_with_question = open('Question.txt', 'r', encoding="utf-8")
file_with_choice = open('Answer_Options.txt', 'r', encoding="utf-8")
file_with_correct_answers = open('Correct_Answers.txt', 'r', encoding="utf-8")


list_of_answers_from_user = []
# Печать всех вариантов
for string in file_with_question:
    Inter.print_strings(string)
    for i in range(4):
        line = file_with_choice.readline()
        Inter.print_strings(line)
        Inter.work_with_answers(line, list_of_answers_from_user, i)

# print(list_of_answers_from_user)
# Закрытие всех файлов при завершении работы с файлами
file_with_question.close()
file_with_choice.close()
file_with_correct_answers.close()