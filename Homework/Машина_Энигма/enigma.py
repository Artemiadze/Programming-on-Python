from accessify import protected


class Enigma:
    def __init__(self, panel, rotor_1, rotor_2, rotor_3, reflector):
        self.panel = panel  # list элементов соединительной панели
        self.rotor_1 = rotor_1  # начальная комбинация первого ротора
        self.rotor_2 = rotor_2  # начальная комбинация второго ротора
        self.rotor_3 = rotor_3  # начальная комбинация третьего ротора
        self.rotor_1_start = rotor_1
        self.rotor_2_start = rotor_2
        self.rotor_3_start = rotor_3
        self.reflector = reflector  # комбинация рефлектора
        self.rotor_shift_1 = 0  # сколько сдвигов совершил первый ротер
        self.rotor_shift_2 = 0  # сколько сдвигов совершил второй ротер

    @protected
    def index_of_symbol(self, symbol):
        char_dict = {
            'А': 0, 'Б': 1, 'В': 2, 'Г': 3
        }
        return char_dict.get(symbol, 0)

    @protected
    def symbol_of_index(self, number):
        char_dict = {
            0: 'А', 1: 'Б', 2: 'В', 3: 'Г'
        }
        return char_dict.get(number, 0)

    def panel_changes(self, symbol):
        """ Метод производит замену символов согласно правилу, прописанном в соединительной панели"""
        for j in range(0, len(self.panel), 2):
            if symbol == self.panel[j]:
                symbol = self.panel[j + 1]
            elif symbol == self.panel[j + 1]:
                symbol = self.panel[j]
        print("Новый символ после panel = ", symbol)
        return symbol

    def first_rotor_change(self, symbol, position_to_shift):
        """Метод совершает изменение сообщения по первому ротору"""
        for i in range(len(self.rotor_1)):
            if self.index_of_symbol(symbol) == i:
                # Замена конкретного символа в конкретном месте в кодирующемся сообщении
                # print(f"Меняем  {symbol} на {self.rotor_1[i]}")
                # print("Нынешний первый ротор", self.rotor_1)
                symbol = self.rotor_1[i]
                self.update_rotor('rotor_1', position_to_shift)
                self.rotor_shift_1 += 1
                # self.update_rotor_1() - на случай, если пред. вариант будет сбоить
                break
        if self.rotor_shift_1 == len(self.rotor_1):
            self.update_rotor('rotor_2', position_to_shift)

        print("Новый символ после 1 ротора = ", symbol)
        return symbol

    def first_right_rotor_change(self, symbol, position_to_shift):
        """Метод совершает изменение сообщения по первому ротору"""
        for i in range(len(self.rotor_1_start)):
            if self.rotor_1_start[i] == symbol:
                # Замена конкретного символа в конкретном месте в кодирующемся сообщении
                symbol = self.symbol_of_index(i)
                self.update_rotor('rotor_1_start', position_to_shift)
                self.rotor_shift_1 += 1
                # self.update_rotor_1() - на случай, если пред. вариант будет сбоить
                break
        if self.rotor_shift_1 == len(self.rotor_1_start):
            self.update_rotor('rotor_2', position_to_shift)
        print("Новый символ после 1 ротора = ", symbol)
        return symbol

    def second_rotor_change(self, symbol, position_to_shift):
        """Метод совершает изменение сообщения по первому ротору"""
        for i in range(len(self.rotor_2)):
            if self.index_of_symbol(symbol) == i:
                # Замена конкретного символа в конкретном месте в кодирующемся сообщении
                # print(f"Меняем  {symbol} на {self.rotor_2[i]}")
                symbol = self.rotor_2[i]
                break
        if self.rotor_shift_2 == len(self.rotor_2):
            self.update_rotor('rotor_3', position_to_shift)
        print("Новый символ после 2 ротора = ", symbol)
        return symbol

    def third_rotor_change(self, symbol):
        """Метод совершает изменение сообщения по первому ротору"""
        for i in range(len(self.rotor_3)):
            if self.index_of_symbol(symbol) == i:
                # Замена конкретного символа в конкретном месте в кодирующемся сообщении
                # print(f"Меняем  {symbol} на {self.rotor_3[i]}")
                symbol = self.rotor_3[i]
                break
        print("Новый символ после 3 ротора = ", symbol)
        return symbol

    def reflectors_change(self, symbol):
        """ """
        for j in range(0, len(self.reflector), 2):
            if symbol == self.reflector[j]:
                symbol = self.reflector[j + 1]
                break
            elif symbol == self.reflector[j + 1]:
                symbol = self.reflector[j]
                break
        print("Новый символ после рефлектора = ", symbol)
        return symbol

    def update_rotor(self, rotor_name, position_to_shift):
        """Метод совершает сдвиг букв в указанном роторе. если -1,то влево, если 1 то вправо"""
        rotor = getattr(self, rotor_name)  # Получить значение атрибута по имени
        updated_rotor = rotor[position_to_shift:] + rotor[:position_to_shift]  # Сдвиг ротора
        setattr(self, rotor_name, updated_rotor)  # Обновить атрибут на новый
        # print("Обновлённый ротер: ", updated_rotor)
