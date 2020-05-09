

class Logger:
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls, *args, **kwargs)
        return cls.instance


a = Logger()
print(a)

b = Logger()
print(b)

c = Logger()
print(c)

#  Note that address of a, b and c is same.