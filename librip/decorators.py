# Здесь необходимо реализовать декоратор, print_result который принимает на вход функцию,
# вызывает её, печатает в консоль имя функции, печатает результат и возвращает значение
# Если функция вернула список (list), то значения должны выводиться в столбик
# Если функция вернула словарь (dict), то ключи и значения должны выводить в столбик через знак равно

def print_result(func):
    def wrapper(*args, **kwargs):
        print(func.__name__)
        res = func(*args, **kwargs)
        if type(res) == dict:
            for i in res: print('{} = {}'.format(i, res[i]))
        elif type(res) == list:
            for i in res: print(i)
        else:
            print(res)
        return res
    return wrapper
