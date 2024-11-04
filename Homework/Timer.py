import asyncio
from colorama import Fore, Style
import chime


def colors(number_of_timer):
    """Функция возвращает для каждого из 10 таймеров его уникальный цвет,
    используя библиотеку colorama"""

    match number_of_timer:
        case '1':
            return Fore.BLUE
        case '2':
            return Fore.GREEN
        case '3':
            return Fore.YELLOW
        case '4':
            return Fore.CYAN
        case '5':
            return Fore.WHITE
        case '6':
            return Fore.RED
        case '7':
            return Fore.LIGHTBLUE_EX
        case '8':
            return Fore.LIGHTGREEN_EX
        case '9':
            return Fore.LIGHTYELLOW_EX
        case _:
            return Fore.LIGHTRED_EX


def work_with_input_data(message, data_type="intervals"):
    """ Функция проверяет коррекность введённых пользователем
    данных и спасает программу от ошибок. Вводимые данные(data_type) это либо число,
     либо интервал для каждого из таймеров."""

    try:
        input_data = int(input(message))
    except ValueError:
        print("Пожалуйста, введите целое число")
        return work_with_input_data(message)

    # от (data_type) зависит, какая проверка нам нужна
    if data_type != "intervals" and (input_data < 1 or input_data > 10):
        print("Количество таймеров должно быть от 1 до 10")
        return work_with_input_data(message, "Numbers_of_timers")

    elif data_type == "intervals" and input_data < 0:
        print("Время не может быть отрицательным! ")
        return work_with_input_data(message)

    return input_data


async def timer(number_of_timer, interval, flag):
    """ Функция цикла жизни таймера, она считает время работы, выводит все состояния таймера:
    ожидание, отсчет, сработал; выводит сколько времени осталось ему работать и """

    # Если таймер начал работать, то вывести соответсвующую фразу, иначе пропустить шаг
    if flag == 1:
        print(f"Таймер {number_of_timer} запущен. Интервал: {interval}")

    # ждём секунду и обновляем время на табло
    await asyncio.sleep(1)
    interval -= 1

    # Если время таймера истекло
    if interval == 0:
        # Уведомление о завершении работы таймера, с использованием звука из SUPER MARIO
        chime.theme('mario')
        chime.success()

        print(colors(number_of_timer) + f"Таймер {number_of_timer} сработал!\n" + Style.RESET_ALL)
    # Если время таймера ещё не истекло
    else:
        print(f"Таймер {number_of_timer}, осталось времени: {interval} ")
        await timer(number_of_timer, interval, 0)


async def main():
    """Главная функция, создающая и запускающая все таймеры в программе"""

    # Число таймеров
    amount_of_timers = work_with_input_data("Введите количество таймеров (от 1 до 10): ", "Numbers_of_timers")

    # Ввод времени для каждого таймера
    timers = []
    for i in range(amount_of_timers):
        # Проверка на корректность введённых данных
        interval = work_with_input_data(f"Введите интервал для таймера {i + 1} в секундах: ")

        timer_name = f"{i + 1}"
        timers.append(timer(timer_name, interval, 1))
    print("\n")

    # Запускает в конкурентном режиме объекты, допускающие ожидание, находящиеся в группе объектов
    await asyncio.gather(*timers)


# Запуск скриптов внутри этого файла
if __name__ == "__main__":
    asyncio.run(main())
