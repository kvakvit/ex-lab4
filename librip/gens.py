import random


# Генератор вычленения полей из массива словарей
# Пример:
# goods = [
#    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
#    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
# ]
# field(goods, 'title') должен выдавать 'Ковер', 'Диван для отдыха'
# field(goods, 'title', 'price') должен выдавать {'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха', 'price': 5300}
from librip.ctxmngrs import Timer as timer

def field(items, *args):

    assert len(args) > 0
    # Необходимо реализовать генератор
    if len(args) == 1:
        for dict in items:
            d = dict.get(args[0])
            if d: yield d
    else:
        for dict in items:
            yield {a: dict.get(a) for a in args if dict.get(a)}


# Генератор списка случайных чисел
# Пример:
# gen_random(1, 3, 5) должен выдать примерно 2, 2, 3, 2, 1
# Hint: реализация занимает 2 строки
def gen_random(begin, end, num_count):
    for y in range(num_count):
        yield random.randint(begin,end)
