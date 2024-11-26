from accessify import protected


class Enigma:
    def __init__(self, message, panel, rotor_1, rotor_2, rotor_3):
        self.message = message  # сообщение, которое нужно закодировать
        self.alphabet = "АБВГ"  # язык, который используется при кодировке
        self.panel = panel  # list элементов соединительной панели
        self.rotor_1 = rotor_1  # начальная комбинация первого ротора
        self.rotor_2 = rotor_2  # начальная комбинация второго ротора
        self.rotor_3 = rotor_3  # начальная комбинация третьего ротора

    @protected
    def index_of_symbol(self, symbol):
        char_dict = {
            'А': 0, 'Б': 1, 'В': 2, 'Г': 3
        }
        return char_dict.get(symbol, 0)

    def panel_changes(self):
        """ Метод производит замену символов согласно правилу, прописанном в соединительной панели"""
        for element in self.message:
            for j in range(0, len(self.panel), 2):
                if element == self.panel[j]:
                    self.message = self.message.replace(element, self.panel[j + 1])
                elif element == self.panel[j + 1]:
                    self.message = self.message.replace(element, self.panel[j])
        print(self.message)

    def first_rotor_change(self):
        """Метод совершает изменение сообщения по первому ротору"""
        for element in self.message:
            for i in range(len(self.rotor_1)):
                if self.index_of_symbol(element) == i:
                    self.message = self.message.replace(element, self.rotor_1[i])
                    self.update_rotor_1()
                    break
        print(self.message)

    def update_rotor_1(self):
        """Метод совершает сдвиг букв в роторе 1 после нажатия клавиши"""
        self.rotor_1 = self.rotor_1[1:] + self.rotor_1[:1]
        print("Обновлённый ротер: ", self.rotor_1)

    def update_rotor_2(self):
        """Метод совершает сдвиг букв в роторе 2 после нажатия клавиши"""
        self.rotor_2 = self.rotor_2[1:] + self.rotor_2[:1]

    def update_rotor_3(self):
        """Метод совершает сдвиг букв в роторе 3 после нажатия клавиши"""
        self.rotor_3 = self.rotor_3[1:] + self.rotor_3[:1]

    def update_rotor(self, rotor_name):
        """Метод совершает сдвиг букв в указанном роторе."""
        rotor = getattr(self, rotor_name)  # Получить значение атрибута по имени
        updated_rotor = rotor[1:] + rotor[:1]  # Сдвиг ротора
        setattr(self, rotor_name, updated_rotor)  # Обновить атрибут на новый
