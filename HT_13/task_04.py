"""
Create 'list'-like object, but index starts from 1 and index of 0 raises error. Тобто це повинен бути клас, який буде
поводити себе так, як list (маючи основні методи), але індексація повинна починатись із 1
"""


class MyList:
    def __init__(self, *args):
        self.my_list = list(args)

    def __getitem__(self, key):
        if isinstance(key, slice):
            start, stop, step = key.start, key.stop, key.step
            if start == 0:
                raise Exception
            start = start - 1 if start else None
            stop = stop - 1 if stop else None
            return self.my_list[start:stop:step]
        else:
            if key == 0:
                raise Exception
            return self.my_list[key - 1]

    def __setitem__(self, key, value):
        if key == 0:
            raise Exception
        self.my_list[key - 1] = value

    def __delitem__(self, key):
        if key == 0:
            raise Exception
        del self.my_list[key - 1]

    def append(self, value):
        self.my_list.append(value)
