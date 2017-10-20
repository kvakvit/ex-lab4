# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):

        self.data = items
        self.index = None
        if type(self.data) == list:
            self.index = 0
        self.unuq = set()
        self.ignore_case = kwargs.get('ignore_case')

    def __next__(self):
        if self.index == None:
            item = str(next(self.data))
        else:
            if self.index == len(self.data):
                raise StopIteration
            item = str(self.data[self.index])
            self.index += 1

        if self.ignore_case:
            item = item.lower()

        if item in self.unuq:
            return self.__next__()
        else:
            self.unuq.add(item)
            return item

    def __iter__(self):
        return self
