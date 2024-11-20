from accessify import protected


class Programmer:
    def __init__(self, name, post):
        self.name = name                                              # Имя
        self.post = post.title()                                      # Должность
        self.work_hours = 0                                           # Кол-во отработанных часов
        self.salary_per_hour = self.info_post_salary(post)            # Должность
        self.allowance = 0                                            # Надбавка (Senior)
        self.salary_accumulated = 0                                   # Накопившеяся зарплата
        self.history = [f"{self.name} принят в компанию на должность {self.post}'а"]  # История изменения

    @protected
    def info_post_salary(self, post):
        """ Метод вовзращает размер оклада для каждой из должностей"""
        salary_dict = {
            'Junior': 10,
            'Middle': 15,
            'Senior': 20
        }
        return salary_dict.get(post, 0)  # Возвращает зарплату

    @property
    def post(self):
        """Валидация  данных для должности программиста
        Если должность будет неверной, то будет выводить ошибку (прям красную строку с ошибкой Value error)"""
        return self._post

    @post.setter
    def post(self, value):
        if value != 'Junior' and value != 'Middle' and value != 'Senior':
            raise ValueError("Введенa неправильная должность")
        self._post = value

    def work(self, time):
        """ Метод считает отработку в количестве часов, считает сколько у него почасовая оплата (надбавка + ЗП)
        и накопившуюся заплату, которая должна выплалить в методе salary"""
        self.work_hours += time
        hourly_rate = self.salary_per_hour + self.allowance             # Почасовая оплата
        self.salary_accumulated += hourly_rate * time
        self.history.append(f"{self.name} отработал в компании {time} ч. с оплатой {hourly_rate} тгр/ч")

    def bonus(self, amount):
        """ Метод для выдача программисту бонуса (попадает в накопленную зарплату"""

        self.salary_accumulated += amount
        self.history.append(f"{self.name} получил премию в размере {amount} тгр")

    def rise(self):
        """ Метод повышает человека до след. должности в иерархии программистов"""
        if self.post.capitalize() == 'Senior':
            self.allowance += 1
            self.history.append(
                f"{self.name} получил повышение (новая ставка: {self.salary_per_hour + self.allowance} тгр/ч)")
        else:
            if self.post.capitalize() == 'Junior':
                self.post = 'Middle'
            elif self.post.capitalize() == 'Middle':
                self.post = 'Senior'
            self.salary_per_hour = self.info_post_salary(self.post)
        self.history.append(f"{self.name} получил повышение до {self.post} (новая ставка: "
                            f"{self.salary_per_hour + self.allowance} тгр/ч)")

    def info(self):
        """ Метод вoзвращает строку для бухгалтерии в формате: <имя> <количество
        отработанных часов> ч. <накопленная зарплата> тгр."""

        return f"{self.name} {self.work_hours} ч. {self.salary_accumulated} тгр"

    def salary(self):
        """ Bыдача зарплаты. Возвращает сколько надо выдать зарплаты и обнуляет
        накопленную зарплату"""
        self.history.append(f"{self.name} получил зарплату {self.salary_accumulated} тгр")
        self.salary_accumulated = 0

    def stat(self):
        """ Bыводит статистику и все шаги с момента приема на работу в формате
        <Имя> <Должность> <событие с описанием>"""

        return '\n'.join(self.history)


# Практика использования
p1 = Programmer("Артём", "MIDDLE")
p1.work(10)
#print(p1.info_post_salary("Middle")) #проверка на доступ к защищенному методу
p1.bonus(50)
p1.rise()
p1.work(5)
p1.salary()
print("INFO:")
print(p1.info())
print("STATISTIC")
print(p1.stat())

print("\n")
programmer = Programmer("Васильев Иван", 'Junior')
programmer.work(750)
print(programmer.info())
programmer.rise()
programmer.work(500)
print(programmer.info())
programmer.rise()
programmer.work(250)
print(programmer.info())
programmer.rise()
programmer.work(250)
print(programmer.info())

