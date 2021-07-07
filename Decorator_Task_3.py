from datetime import datetime


def loger(directory='log.txt'):
    def _loger(function):

        def new_fun(*args, **kwargs):

            with open(directory, 'a', encoding='utf-8') as file:
                file.write(f"""Дата\Время: {datetime.now()}
Вызвана функция - '{function.__name__}'
С аргументами: args: {args}; kwargs: {kwargs}.\n""")

            result = function(*args, **kwargs)

            with open(directory, 'a', encoding='utf-8') as file:
                file.write(f"""Возвращаемый результат функции - '{result}'
{'*' * 42}\n""")

            return result
        return new_fun
    return _loger
