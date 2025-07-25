# form_builder.py
from abc import ABCMeta, abstractmethod

# Product
class Director(object, metaclass=ABCMeta):
    def __init__(self):
        self._builder = None

    @abstractmethod
    def construct(self):
        pass

    def get_constructed_object(self):
        return self._builder.constructed_object


# Builder Interface
class Builder(object, metaclass=ABCMeta):
    def __init__(self, constructed_object):
        self.constructed_object = constructed_object


# Concrete Builder
class Product(object):
    def __init__(self):
        pass

    def __repr__(self):
        pass


class ConcreteBuilder(Builder):
    pass


class ConcreteDirector(Director):
    pass