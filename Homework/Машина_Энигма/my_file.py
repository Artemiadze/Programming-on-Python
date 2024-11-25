import re
import enigma as e
with open("Connecting_Panel.txt", "r", encoding='utf-8') as file:
    # четные индексы - буквы которые заменяются, нечетные - которые надо заменить
    file_with_panel = re.split(r'[ ,-]', file.read())

with open("Rotor_1.txt", "r", encoding='utf-8') as file_1:
    file_rotor_1 = file_1.read()

with open("Rotor_2.txt", "r", encoding='utf-8') as file_1:
    file_rotor_2 = file_1.read()

with open("Rotor_3.txt", "r", encoding='utf-8') as file_1:
    file_rotor_3 = file_1.read()

# Не забыть удалить!!!
print(file_with_panel)
print(file_rotor_1)
print(file_rotor_2)
print(file_rotor_3)

code = e.Enigma('ГАВ', file_with_panel, file_rotor_1, file_rotor_2, file_rotor_3)
code.panel_changes()