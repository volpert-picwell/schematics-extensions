import unittest

from ..models import *
from ..types import *
from ..types.compound import *


class SimpleModel(Model):
    string_field = StringType()


class ModelForTesting(Model):
    int_field = IntType()
    string_field = StringType()
    float_field = FloatType()
    boolean_field = BooleanType()
    long_field_is_long = LongType()
    dict_field = DictType(StringType)
    list_field = ListType(StringType)
    model_field = ModelType(SimpleModel)


class ReprTest(unittest.TestCase):
    def setUp(self):
        self.repr_model = ModelForTesting.get_mock_object()

    def test_repr_works(self):
        self.assertEqual(self.repr_model, eval(repr(self.repr_model)))
