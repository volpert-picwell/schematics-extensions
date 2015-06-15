from schematics.types import (IntType, StringType, FloatType, BooleanType,
                              NumberType, LongType)


class IntType(IntType):

    @classmethod
    def null(self):
        return None


class CurrencyType(NumberType):

    def __init__(self, *args, **kwargs):
        super(CurrencyType, self).__init__(
                number_class=lambda x: round(x, 2),
                number_type='CurrencyType', *args, **kwargs)

    @classmethod
    def null(self):
        return None


class StringType(StringType):

    @classmethod
    def null(self):
        return None


class FloatType(FloatType):

    @classmethod
    def null(self):
        return None


class BooleanType(BooleanType):

    @classmethod
    def null(self):
        return None


class LongType(LongType):

    @classmethod
    def null(self):
        return None
