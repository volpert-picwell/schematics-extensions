import random
import re
import string

from schematics.exceptions import ValidationError
from schematics.types import StringType


class NumericStringType(StringType):
    """String that contains only digits.

    Parameters:
        length (int): Exact number of digits the string can contains. Optional.

    Example usage:

        class MyModel(Model):
            my_field = NumericStringType(length=5)
    """

    MESSAGES = {
        'length': u'Value is not a numeric string of length %d'
    }

    REGEX_PATTERN = r'^\d{%d}$'

    def __init__(self, **kwargs):
        length = kwargs.pop('length')
        super(NumericStringType, self).__init__(**kwargs)
        self.length = length
        self.regex = re.compile(self.REGEX_PATTERN % self.length)

    def _mock(self, context=None):
        return ''.join(
            random.choice(string.digits) for _ in range(self.length))

    def validate_regex(self, value):
        if self.regex is not None and self.regex.match(value) is None:
            raise ValidationError(self.messages['length'] % self.length)
