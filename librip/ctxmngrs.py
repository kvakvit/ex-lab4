import time

class Timer(object):
    def __init__(self):
        self.start = time.time()

    def __enter__(self):
        pass

    def __exit__(self, exp_type, exp_value, exp_tr):
        print('%20f' % round(time.time() - self.start, 20))
