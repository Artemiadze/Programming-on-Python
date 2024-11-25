import re
import enigma as e
with open("Connecting_Panel.txt", "r", encoding='utf-8') as file:
    # четные индексы - буквы которые заменяются, нечетные - которые надо заменить
    file_with_panel = re.split(r'[ ,-]', file.read())

print(file_with_panel)

code = e.Enigma('ГАВ',file_with_panel)
code.panel_changes()