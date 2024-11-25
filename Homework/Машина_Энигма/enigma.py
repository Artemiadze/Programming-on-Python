class Enigma:
    def __init__(self, message, panel):
        self.message = message  # сообщение, которое нужно закодировать
        self.alphabet = "АБВГ"  # язык, который используется при кодировке
        self.panel = panel      # list элементов соединительной панели

    def panel_changes(self):
        for i in range(0, len(self.message)):
            for j in range(0, len(self.panel), 2):
                if self.message[i] == self.panel[j]:
                    self.message = self.message.replace(self.message[i], self.panel[j+1])
                elif self.message[i] == self.panel[j+1]:
                    self.message = self.message.replace(self.message[i], self.panel[j])
        print(self.message)
        


