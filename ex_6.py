#!/usr/bin/env python3
import json
import sys
from librip.ctxmngrs import Timer as timer
from librip.decorators import print_result
from librip.gens import field, gen_random
from librip.iterators import Unique as unique

path = 'data_light.json'

# Здесь необходимо в переменную path получить
# путь до файла, который был передан при запуске

with open(path) as f:
    data = json.load(f)

@print_result
def f1(arg):
    return list(sorted(unique(field(data, 'job-name'), ignore_case=True), key=lambda x: x.lower()))

@print_result
def f2(arg):
    print(arg)
    return list(filter(lambda x: x.lower().startswith('программист'), arg))

@print_result
def f3(arg):
    return list(map(lambda x: x + ' с опытом Python', arg))


@print_result
def f4(arg):
    return list('{}, зарплата {} руб.'.format(i,j) for i,j in zip(arg, gen_random(100000, 200000, len(arg))))

with timer():
    f4(f3(f2(f1(data))))
