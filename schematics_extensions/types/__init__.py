from schematics.types import (
    IntType, StringType, FloatType, BooleanType, LongType)


class IntType(IntType):

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
