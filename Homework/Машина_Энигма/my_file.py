import re
import enigma as e
from colorama import init

init(autoreset=True)
from colorama import Fore, Back


def color_console():
    """ Функция окрашивает текст и консоль при запуске файла"""
    print(Fore.BLACK + Back.WHITE + "Здравствуйте! Перед Вами шифровальная машина Энигма, которая может "
                                    "зашифровать ваше сообщение")
    print(Fore.BLACK + Back.WHITE + "Перед началом работы машины вам необходимо ввести через пробел три параметра,"
                                    " которые определят работу шифровальной машины.")
    print(Fore.BLACK + Back.RED + "1. Сначала вы вводите стартовое смещение ротеров в виде трёх для трёх ротеров")
    print(Fore.BLACK + Back.RED + "Например, АБГ, где А означает что первый ротер смещать не надо, Б - сместить "
                                  "второй ротер на 1 позицию, Г - сместить третий ротор на 3 позиции")
    print(Fore.BLACK + Back.YELLOW + "2. Затем вы вводите параметры соединительной панели")
    print(Fore.BLACK + Back.YELLOW + "Они из себя представляют пары букв, которые меняются друг на друга")
    print(Fore.BLACK + Back.YELLOW + "Пример: БВ означает, что Б должно заменяться на В и наоборот")
    print(Fore.BLACK + Back.YELLOW + "Если таких пар несколько, то вводите все пары слитно, например, "
                                     "пары БВ и АГ = БВАГ или АГБВ")
    print(Fore.BLACK + Back.GREEN + "3. Вы должны ввести само сообщение, которое хотите закодировать")


# Открытие файлов с настройками трёх роторов и рефлектора
with open("Rotor_1.txt", "r", encoding='utf-8') as file_1:
    file_rotor_1 = file_1.read()

with open("Rotor_2.txt", "r", encoding='utf-8') as file_1:
    file_rotor_2 = file_1.read()

with open("Rotor_3.txt", "r", encoding='utf-8') as file_1:
    file_rotor_3 = file_1.read()

with open("Reflector.txt", "r", encoding='utf-8') as file_ref:
    reflector_file = re.split(r'[ ,-]+', file_ref.read())

# запуск основного кода
if __name__ == "__main__":
    color_console()

    # Ввод всех данных
    try:
        position_rotors, connecting_panel, word = input().upper().split()
        connecting_panel = list(connecting_panel)

        # Начало работы с шифрованием на машине Энигма
        code = e.Enigma('АБВГ', connecting_panel, file_rotor_1, file_rotor_2, file_rotor_3, reflector_file)
        encrypted_word = ''  # зашифрованное сообщение

        # Прогон каждой буквы сообщения через Энигму (имитация ввода с клавиатуры Энигмы буквы для шифровки)
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

        print(Fore.CYAN + "Ваше зашифрованное слово: " + Fore.WHITE, encrypted_word)
    except ValueError:
        print("Надо ввести три параметра, а вы ввели отнудь не три")
        print("Или вы ввели символы не из русского алфавита!")
