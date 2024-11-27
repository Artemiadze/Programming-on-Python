import re
import enigma as e

with open("Rotor_1.txt", "r", encoding='utf-8') as file_1:
    file_rotor_1 = file_1.read()

with open("Rotor_2.txt", "r", encoding='utf-8') as file_1:
    file_rotor_2 = file_1.read()

with open("Rotor_3.txt", "r", encoding='utf-8') as file_1:
    file_rotor_3 = file_1.read()
with open("Reflector.txt", "r", encoding='utf-8') as file_ref:
    reflector_file = re.split(r'[ ,-]+', file_ref.read())

position_rotors = input()
connecting_panel = input()
connecting_panel = list(connecting_panel)
word = input()


# Не забыть удалить!!!
print(connecting_panel)
print(file_rotor_1)
print(file_rotor_2)
print(file_rotor_3 + "\n")
print("Сдвиг влево ", file_rotor_1[1:] + file_rotor_1[:1])
print("Сдвиг вправо ", file_rotor_1[-1:] + file_rotor_1[:-1])
print(reflector_file)
print("\n")

code = e.Enigma('АБВГ', connecting_panel, file_rotor_1, file_rotor_2, file_rotor_3, reflector_file)
encrypted_word = ''
for symbol in word:
    code.start_position_for_rotors(position_rotors.upper())
    symbol = code.panel_changes(symbol)
    symbol = code.first_rotor_change(symbol, 1)
    symbol = code.second_rotor_change(symbol, 1)
    symbol = code.third_rotor_change(symbol)
    symbol = code.reflectors_change(symbol)
    symbol = code.third_rotor_right_change(symbol)
    symbol = code.second_right_rotor_change(symbol, 1)
    symbol = code.first_right_rotor_change(symbol, 1)
    symbol = code.panel_changes(symbol)
    encrypted_word += symbol
    print("\n")

print("Зашифрованное слово: ", encrypted_word)