import pytest

from schematics_extensions.models import Model
from schematics.exceptions import (
    BaseError, ValidationError, ConversionError,
    ModelValidationError, ModelConversionError,
)
from schematics.types import StringType, DateTimeType, BooleanType

"""
THIS IS HERE TEMPORARILY UNTIL THE VALIDATION ORDERING FIX IS
RELEASED TO SCHEMATICS
"""


def test_multi_key_validation_fields_order():
    class Signup(Model):
        name = StringType()
        call_me = BooleanType(default=False)

        def validate_name(self, data, value):
            if data['name'] == u'Brad':
                value = u'Joe'
                data['name'] = value
                return value
            return value

        def validate_call_me(self, data, value):
            if data['name'] == u'Joe':
                raise ValidationError(u"Don't try to decept me! You're Joe!")
            return value

    Signup({'name': u'Tom'}).validate()

    with pytest.raises(ValidationError):
        Signup({'name': u'Brad'}).validate()
