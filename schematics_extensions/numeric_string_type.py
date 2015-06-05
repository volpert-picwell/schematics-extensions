from random import choice, randint
import string

from schematics.exceptions import ValidationError
from .types import StringType


class NumericStringType(StringType):
    """String that contains only digits.

    Parameters:
        length (int): Exact number of digits the string can contains. Optional.

    Example usage:

        class MyModel(Model):
            my_field = NumericStringType(length=5)
    """

    MESSAGES = {
        'length': u'Value is not a numeric string of length %d',
        'digits': u'Value contains characters other than numeric digits',
    }

    def __init__(self, **kwargs):
        self.length = kwargs.pop('length', None)
        super(NumericStringType, self).__init__(**kwargs)

    def _mock(self, context=None):
        length = self.length if self.length else randint(1, self.max_length
                                                         if self.max_length
                                                         else 20)
        return ''.join(choice(string.digits) for _ in range(length))

    def validate_numeric(self, value):
        try:
            int(value)
        except:
            raise ValidationError(self.messages['digits'])

    def validate_length(self, value):
        if self.length and len(value) != self.length:
            raise ValidationError(self.messages['length'] % self.length)
