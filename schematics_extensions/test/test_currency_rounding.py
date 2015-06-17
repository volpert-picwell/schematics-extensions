import pytest

from ..types import CurrencyType
from ..models import Model


class ExampleModel(Model):
    attribute = CurrencyType(required=True)


def test_float_is_rounded_up_correctly():
    model = ExampleModel({'attribute': 34.5679})
    assert model.attribute == 34.57


def test_float_is_rounded_down_correctly():
    model = ExampleModel({'attribute': 34.44496})
    assert model.attribute == 34.44
