from accessify import protected


class Enigma:
    def __init__(self, panel, rotor_1, rotor_2, rotor_3, reflector):
        self.panel = panel  # list элементов соединительной панели

        self.rotor_1 = rotor_1  # начальная комбинация первого ротора для левого смещения
        self.rotor_2 = rotor_2  # начальная комбинация второго ротора для левого смещения
        self.rotor_3 = rotor_3  # начальная комбинация третьего ротора для левого смещения

        self.rotor_1_start = rotor_1  # начальная комбинация первого ротора для правого смещения
        self.rotor_2_start = rotor_2  # начальная комбинация второго ротора для правого смещения
        self.rotor_3_start = rotor_3  # начальная комбинация третьего ротора для правого смещения

        self.reflector = reflector  # комбинация рефлектора

        self.rotor_shift_left_1 = 0  # сколько сдвигов влево совершил первый ротер
        self.rotor_shift_left_2 = 0  # сколько сдвигов влево совершил второй ротер

        self.rotor_shift_right_1 = 0  # сколько сдвигов вправо совершил первый ротер
        self.rotor_shift_right_2 = 0  # сколько сдвигов вправо совершил первый ротер

    @protected
    def index_of_symbol(self, symbol):
        """По букве возвращаем её индекс в алфавите"""
        char_dict = {
            'А': 0, 'Б': 1, 'В': 2, 'Г': 3
        }
        return char_dict.get(symbol, 0)

    @protected
    def symbol_of_index(self, number):
        """По индексу возвращаем соответсвующую букву из алфавита"""
        char_dict = {
            0: 'А', 1: 'Б', 2: 'В', 3: 'Г'
        }
        return char_dict.get(number, 0)

    def start_position_for_rotors(self,position_string):
        """ В зависимости от того, что ввёл пользователь, меняем начальную позицию ротером"""
        position_1 = self.index_of_symbol(position_string[0])
        position_2 = self.index_of_symbol(position_string[1])
        position_3 = self.index_of_symbol(position_string[2])
        self.update_rotor('rotor_1', position_1)
        self.update_rotor('rotor_2', position_2)
        self.update_rotor('rotor_3', position_3)
        self.update_rotor('rotor_1_start', position_1)
        self.update_rotor('rotor_2_start', position_2)
        self.update_rotor('rotor_3_start', position_3)

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
        """Метод совершает изменение символа по первому ротору со смещением вправо"""
        for i in range(len(self.rotor_1)):
            if self.index_of_symbol(symbol) == i:
                # Замена конкретного символа в конкретном месте в кодирующемся сообщении
                symbol = self.rotor_1[i]

                # после каждой буквы ротор 1 поворачивается на 1 позицию и замены сдвигаются.
                self.rotor_shift_left_1 += 1
                self.update_rotor('rotor_1', position_to_shift)
                break

        if self.rotor_shift_left_1 == len(self.rotor_1):
            self.update_rotor('rotor_2', position_to_shift)
            self.rotor_shift_left_2 += 1

        print("Новый символ после 1 ротора = ", symbol)
        return symbol

    def first_right_rotor_change(self, symbol, position_to_shift):
        """Метод совершает изменение символа по первому ротору со смещением вправо"""
        for i in range(len(self.rotor_1_start)):
            if self.rotor_1_start[i] == symbol:
                # Замена конкретного символа в конкретном месте в кодирующемся сообщении
                symbol = self.symbol_of_index(i)

                # после каждой буквы ротор 1 поворачивается на 1 позицию и замены сдвигаются.
                self.rotor_shift_right_1 += 1
                self.update_rotor('rotor_1_start', position_to_shift)
                break
        if self.rotor_shift_right_1 == len(self.rotor_1_start):
            self.update_rotor('rotor_2_start', position_to_shift)
            self.rotor_shift_right_2 += 1

        print("Новый символ после 1 ротора = ", symbol)
        return symbol

    def second_rotor_change(self, symbol, position_to_shift):
        """Метод совершает изменение символа по второму ротору со смещением влево"""
        for i in range(len(self.rotor_2)):
            if self.index_of_symbol(symbol) == i:
                # Замена конкретного символа в конкретном месте в кодирующемся сообщении
                # print(f"Меняем  {symbol} на {self.rotor_2[i]}")
                print("Нынешний second ротор", self.rotor_2)
                symbol = self.rotor_2[i]
                break

        if self.rotor_shift_left_2 == len(self.rotor_2):
            self.update_rotor('rotor_3', position_to_shift)
        print("Новый символ после 2 ротора = ", symbol)
        return symbol

    def second_right_rotor_change(self, symbol, position_to_shift):
        """Метод совершает изменение символа по второму ротору со смещением вправо"""
        for i in range(len(self.rotor_2_start)):
            if self.rotor_2_start[i] == symbol:
                # Замена конкретного символа в конкретном месте в кодирующемся сообщении
                symbol = self.symbol_of_index(i)
                break

        if self.rotor_shift_right_2 == len(self.rotor_2_start):
            self.update_rotor('rotor_3_start', position_to_shift)

        print("Новый символ после 2 ротора = ", symbol)
        return symbol

    def third_rotor_change(self, symbol):
        """Метод совершает изменение символа по третьему ротору влево"""
        for i in range(len(self.rotor_3)):
            if self.index_of_symbol(symbol) == i:
                # Замена конкретного символа в конкретном месте в кодирующемся сообщении
                symbol = self.rotor_3[i]
                break

        print("Новый символ после 3 ротора = ", symbol)
        return symbol

    def third_rotor_right_change(self, symbol):
        """Метод совершает изменение символа по третьему ротору вправо"""
        for i in range(len(self.rotor_3_start)):
            if self.rotor_3_start[i] == symbol:
                # Замена конкретного символа в конкретном месте в кодирующемся сообщении
                symbol = self.symbol_of_index(i)
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
