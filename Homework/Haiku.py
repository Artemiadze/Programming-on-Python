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
        # Неверное число слогов для того, чтобы называться хайку
        return f"Не хайку. В {syllables.index(max(syllables)) + 1} строке слогов не {5 if max(syllables) > 5 else 7}, а {max(syllables)}."


# Открытие файла с текстом хайку
with open('haiku.txt', 'r', encoding='utf-8') as file:
    haiku_text = file.readlines()


# Конечный список всех строк с их результатом проверок на хайку
results = []


# Итерация по трёхстишьям для проверки их на хайку
for tercet in haiku_text:
    results.append(tercet.strip())                     # Добавляем в конечный список трёстишье без пробела (.strip)
    results.append(check_haiku(tercet.strip()))        # Добавляем в конечный список  результат проверки трёхстишья
    results.append("")                                 # Добавляем в конечный список красивый отступ для эстетики резу


# Запись результата проверки стиха на хайку
with open('test_haiku.txt', 'w', encoding='utf-8') as file:
    for result in results:
        file.write(result + '\n')
