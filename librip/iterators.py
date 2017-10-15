# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):

        self.data = [item for item in items]
        self.index = 0
        self.unuq = set()
        self.ignore_case = kwargs.get('ignore_case')

    def __next__(self):
        # Нужно реализовать __next__
        if self.index == len(self.data):
            raise StopIteration

        item = str(self.data[self.index])

        if self.ignore_case:
            item = item.lower()

        self.index += 1

        if item in self.unuq:
            return self.__next__()
        else:
            self.unuq.add(item)
            return self.data[self.index-1]

    def __iter__(self):
        return self
