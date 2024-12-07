from enigma import *
import pytest


@pytest.fixture
def enigma_machine():
    """ Функция создаёт и возвращает созданный здесь класс Энигма с заданными в этой же
    функции атрибутами для этого класса"""

    # настройки энигмы такие простые, чтобы было легче самому находить решения,
    # а потом через тесты сравнивать, совпало ли с машиной
    alphabet = "АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    panel = "АБВГДЕ"
    rotor_1 = "БВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯА"
    rotor_2 = "ВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБ"
    rotor_3 = "ГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВ"
    reflector = "АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    return Enigma(alphabet, panel, rotor_1, rotor_2, rotor_3, reflector)


def test_update_rotor(enigma_machine):
    """ Проверка функции сдвига ротора на N (здесь N = 1)позиций"""
    original_rotor = enigma_machine.rotor_1
    enigma_machine.update_rotor("rotor_1", 1)
    new_rotor = enigma_machine.rotor_1
    assert original_rotor != new_rotor, "Сдвиг ротора некорректен!"


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
             "ГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВ")),  # Тест пройдёт
    ("БВГ", ("ВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБ",
             "ГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВ",
             "ДЕЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГ")),  # Тест не должен пройти - должен выдать ошибку(и он её выдаст)
    ("БББ", ("ВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБ",
             "ГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВ",
             "ДЕЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГ")),  # Тест пройдёт
    ("ВВД", ("ГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВ",
             "ДЕЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГ",
             "ЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЖ"))  # Тест пройдёт
])
def test_start_positions(enigma_machine, start_positions, expected_rotors):
    """Проверка установки начальных позиций роторов,
    действительно ли работает в энигме сдвиг роторов"""

    enigma_machine.start_position_for_rotors(start_positions)
    assert enigma_machine.rotor_1 == expected_rotors[0], "Ротор 1 не совершил необходимый сдвиг при запуске машины"
    assert enigma_machine.rotor_2 == expected_rotors[1], "Ротор 2 не совершил необходимый сдвиг при запуске машины"
    assert enigma_machine.rotor_3 == expected_rotors[2], "Ротор 3 не совершил необходимый сдвиг при запуске машины"


@pytest.mark.parametrize("message,encrypted", [
    ("АБВ", "ЖЖЛ"),  # правильный ответ
    ("ГДЕ", "ЖИК"),  # неправильый ответ - должен выдать ошибку(наглядная демонстрация ошибки ручного расчёта тестов )
    ("ГАВ", "ККЛ"),   # правильный ответ
    ("АРТЕМ", "ЖШЩНХ"),   # правильный ответ
    ("ВЛАСОВ", "ИСИЩЧР"),   # правильный ответ
])
def test_message_encryption(enigma_machine, message, encrypted):
    """Проверка корректности шифрования сообщений."""

    result = ""
    for char in message:
        # полный цикл кодирования всего сообщения по каждой букве
        enigma_machine.start_position_for_rotors("ААА")
        char = enigma_machine.panel_changes(char)
        char = enigma_machine.first_rotor_change(char)
        char = enigma_machine.second_rotor_change(char)
        char = enigma_machine.third_rotor_change(char)
        char = enigma_machine.reflectors_change(char)
        result += char
    assert result == encrypted, "Машина закодировала сообщение не так как надо тестироващику"


@pytest.mark.parametrize("message", [
    123,  # Некорректные символы
    "",  # Пустая строка
    None,  # None вместо строки
])
def test_incorrect_input(enigma_machine, message):
    """Проверка обработки разных вариаций некорректного ввода."""

    # Проверяем различные Exception в Pytest
    with pytest.raises(Exception):
        result = ""
        for char in message:
            # полный цикл кодирования всего сообщения по каждой букве
            enigma_machine.start_position_for_rotors("ААА")
            char = enigma_machine.panel_changes(char)
            char = enigma_machine.first_rotor_change(char)
            char = enigma_machine.second_rotor_change(char)
            char = enigma_machine.third_rotor_change(char)
            char = enigma_machine.reflectors_change(char)
            result += char


def test_different_rotors(enigma_machine):
    """Проверка, что разные начальные положения роторов дают разные закодированные сообщения"""

    message = "ГАВ"     # Наше сообщение
    rotors_position_1 = 'ААА'   # Первая настройка роторов
    rotors_position_2 = 'ААБ'   # Вторая настройка роторов
    encrypted_1 = ""    # Результат шифрования при rotors_position_1
    encrypted_2 = ""    # Результат шифрования при rotors_position_2

    # Прогон каждой буквы сообщения через Энигму (имитация ввода с клавиатуры Энигмы буквы для шифровки)
    for char_1 in message:
        enigma_machine.start_position_for_rotors(rotors_position_1)
        char_1 = enigma_machine.panel_changes(char_1)
        char_1 = enigma_machine.first_rotor_change(char_1)
        char_1 = enigma_machine.second_rotor_change(char_1)
        char_1 = enigma_machine.third_rotor_change(char_1)
        char_1 = enigma_machine.reflectors_change(char_1)
        char_1 = enigma_machine.third_rotor_right_change(char_1)
        char_1 = enigma_machine.second_right_rotor_change(char_1)
        char_1 = enigma_machine.first_right_rotor_change(char_1)
        char_1 = enigma_machine.panel_changes(char_1)
        encrypted_1 += char_1

    # Прогон того же сообщения, но с другими начальными настройками ротеров
    for char_2 in message:
        enigma_machine.start_position_for_rotors(rotors_position_2)
        char_2 = enigma_machine.panel_changes(char_2)
        char_2 = enigma_machine.first_rotor_change(char_2)
        char_2 = enigma_machine.second_rotor_change(char_2)
        char_2 = enigma_machine.third_rotor_change(char_2)
        char_2 = enigma_machine.reflectors_change(char_2)
        char_2 = enigma_machine.third_rotor_right_change(char_2)
        char_2 = enigma_machine.second_right_rotor_change(char_2)
        char_2 = enigma_machine.first_right_rotor_change(char_2)
        char_2 = enigma_machine.panel_changes(char_2)
        encrypted_2 += char_2

    assert encrypted_1 != encrypted_2, "Сообщение не поменялось "
