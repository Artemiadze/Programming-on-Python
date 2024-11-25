class Enigma:
    def __init__(self, message, panel, rotor_1, rotor_2, rotor_3):
        self.message = message  # сообщение, которое нужно закодировать
        self.alphabet = "АБВГ"  # язык, который используется при кодировке
        self.panel = panel      # list элементов соединительной панели
        self.rotor_1 = rotor_1  # начальная комбинация первого ротора
        self.rotor_2 = rotor_2  # начальная комбинация второго ротора
        self.rotor_3 = rotor_3  # начальная комбинация третьего ротора

    def panel_changes(self):
        """ Метод производит замену символов согласно правилу, прописанном в соединительной панели"""
        for element in self.message:
            for j in range(0, len(self.panel), 2):
                if element == self.panel[j]:
                    self.message = self.message.replace(element, self.panel[j+1])
                elif element == self.panel[j+1]:
                    self.message = self.message.replace(element, self.panel[j])
        print(self.message)

    def first_rotor_change(self):
        """Метод совершает изменение сообщения по первому ротору"""

    def update_rotor(self):
        """Метод совершает сдвиг букв в роторе после нажатия клавиши"""
        


