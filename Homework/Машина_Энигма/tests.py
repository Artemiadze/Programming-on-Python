from enigma import *
import pytest


@pytest.fixture
def enigma_machine():
    """ Функция создаёт и возвращает созданный здесь класс Энигма с заданными в этой же
    функции атрибутами для этого класса"""

    alphabet = "АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    panel = "АБВГДЕ"
    rotor_1 = "БВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯА"
    rotor_2 = "ВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБ"
    rotor_3 = "ГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВ"
    reflector = "АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    return Enigma(alphabet, panel, rotor_1, rotor_2, rotor_3, reflector)

# не трогать
def test_update_rotor(enigma_machine):
    """ Проверка функции сдвига ротора на N позиций"""
    original_rotor = enigma_machine.rotor_1
    enigma_machine.update_rotor("rotor_1", 1)
    new_rotor = enigma_machine.rotor_1
    assert original_rotor != new_rotor, "Сдвиг ротора некорректен!"

# не трогать
def test_connecting_panel(enigma_machine):
    """ Метод шифрует сообщение только с использованием соединительной панели, затем обратно
    дешифрует только с использованием соединительной панели. Так мы проверям работу соед. панели"""
    message = "АБВ"
    encrypted = "".join([enigma_machine.panel_changes(char) for char in message])
    decrypted = "".join([enigma_machine.panel_changes(char) for char in encrypted])
    assert decrypted == message, "Соединительная панель некорректно работает!"


@pytest.mark.parametrize("start_positions,expected_rotors", [
    ("ААА", ("БВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯА",
             "ВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБ",
             "ГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВ")),
    ("БВГ", ("ВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБ",
             "ГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВ",
             "ДЕЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГ")),
])
def test_start_positions(enigma_machine, start_positions, expected_rotors):
    """Проверка установки начальных позиций роторов."""
    enigma_machine.start_position_for_rotors(start_positions)
    assert enigma_machine.rotor_1 == expected_rotors[0]
    assert enigma_machine.rotor_2 == expected_rotors[1]
    assert enigma_machine.rotor_3 == expected_rotors[2]

# Не трогать
@pytest.mark.parametrize("message,encrypted", [
    ("АБВ", "ЖЖЛ"),  # правильный ответ
    ("ГДЕ", "ЖИК"),  # неправильый ответ
])
def test_message_encryption(enigma_machine, message, encrypted):
    """Проверка корректности шифрования сообщений."""
    result = ""
    for char in message:
        enigma_machine.start_position_for_rotors("ААА")
        char = enigma_machine.panel_changes(char)
        char = enigma_machine.first_rotor_change(char)
        char = enigma_machine.second_rotor_change(char)
        char = enigma_machine.third_rotor_change(char)
        char = enigma_machine.reflectors_change(char)
        result += char
    assert result == encrypted

# Не трогать
@pytest.mark.parametrize("message", [
    123,  # Некорректные символы
    "",  # Пустая строка
    None,  # None вместо строки
])
def test_incorrect_input(enigma_machine, message):
    """Проверка обработки разных вариаций некорректного ввода."""
    with pytest.raises(Exception):
        result = ""
        for char in message:
            enigma_machine.start_position_for_rotors("ААА")
            char = enigma_machine.panel_changes(char)
            char = enigma_machine.first_rotor_change(char)
            char = enigma_machine.second_rotor_change(char)
            char = enigma_machine.third_rotor_change(char)
            char = enigma_machine.reflectors_change(char)
            result += char

# Не трогать
def test_different_rotors():
    """Проверка, что разные начальные положения роторов дают разные закодированные сообщения"""
    alphabet = "АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    panel = "АБВГ"
    rotor_1 = "БВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯА"
    rotor_2 = "ВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБ"
    rotor_3 = "ГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВ"
    reflector = "АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

    # Для одного сообщения запускаем параллельно две машины с разными стартовыми положениями роторов,
    # остальные настройки идентичные
    enigma_1 = Enigma(alphabet, panel, rotor_1, rotor_2, rotor_3, reflector)
    enigma_2 = Enigma(alphabet, panel, rotor_2, rotor_1, rotor_3, reflector)

    message = "ГАВ"
    rotors_position_1 = 'ААА'   # Первая настройка роторов
    rotors_position_2 = 'ААБ'   # Вторая настройка роторов
    encrypted_1 = ""
    encrypted_2 = ""

    # Прогон каждой буквы сообщения через Энигму (имитация ввода с клавиатуры Энигмы буквы для шифровки)
    for char_1 in message:
        enigma_1.start_position_for_rotors(rotors_position_1)
        char_1 = enigma_1.panel_changes(char_1)
        char_1 = enigma_1.first_rotor_change(char_1)
        char_1 = enigma_1.second_rotor_change(char_1)
        char_1 = enigma_1.third_rotor_change(char_1)
        char_1 = enigma_1.reflectors_change(char_1)
        char_1 = enigma_1.third_rotor_right_change(char_1)
        char_1 = enigma_1.second_right_rotor_change(char_1)
        char_1 = enigma_1.first_right_rotor_change(char_1)
        char_1 = enigma_1.panel_changes(char_1)
        encrypted_1 += char_1

    # Прогон того же сообщения, но с другими начальными настройками ротеров
    for char_2 in message:
        enigma_2.start_position_for_rotors(rotors_position_2)
        char_2 = enigma_2.panel_changes(char_2)
        char_2 = enigma_2.first_rotor_change(char_2)
        char_2 = enigma_2.second_rotor_change(char_2)
        char_2 = enigma_2.third_rotor_change(char_2)
        char_2 = enigma_2.reflectors_change(char_2)
        char_2 = enigma_2.third_rotor_right_change(char_2)
        char_2 = enigma_2.second_right_rotor_change(char_2)
        char_2 = enigma_2.first_right_rotor_change(char_2)
        char_2 = enigma_2.panel_changes(char_2)
        encrypted_2 += char_2

    assert encrypted_1 != encrypted_2, "Сообщение не поменялось "


