class Director:
    """
    The Director is only responsible for executing the building steps in a
    particular sequence. It is helpful when producing products according to a
    specific order or configuration. Strictly speaking, the Director class is
    optional, since the client can control builders directly.
    """

    def __init__(self) -> None:
        self.name = None

    @property
    def builder(self):
        return self.name

    @builder.setter
    def builder(self, name) -> None:
        """
        The Director works with any builder instance that the client code passes
        to it. This way, the client code may alter the final type of the newly
        assembled product.
        """
        self.name = name


a = Director()

print (a.builder)
a.builder = 1
print (a.builder)
