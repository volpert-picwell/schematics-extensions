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


class NullableTest(unittest.TestCase):
    def setUp(self):
        self.null_model = ModelForTesting.get_null_object()

    def test_fields_are_null(self):
        self.assertEqual(self.null_model.int_field, None)
        self.assertEqual(self.null_model.string_field, None)
        self.assertEqual(self.null_model.float_field, None)
        self.assertEqual(self.null_model.boolean_field, None)
        self.assertEqual(self.null_model.long_field_is_long, None)
        self.assertEqual(self.null_model.dict_field, {})
        self.assertEqual(self.null_model.list_field, [])
        self.assertEqual(self.null_model.model_field, None)


class OverridesTest(unittest.TestCase):
    def setUp(self):
        overrides = {
            "int_field": 42,
            "string_field": "foobar",
            "float_field": 3.14,
            "boolean_field": True,
            "long_field_is_long": 42L,
            "dict_field": {"foo": "bar"},
            "list_field": ["moe", "larry", "curly"],
            "model_field": SimpleModel.get_mock_object(
                overrides={"string_field": "foo"}
            )
        }

        self.null_model = ModelForTesting.get_null_object(
            overrides=overrides
        )

    def test_fields_are_overridden(self):
        self.assertEqual(self.null_model.int_field, 42)
        self.assertEqual(self.null_model.string_field, "foobar")
        self.assertEqual(self.null_model.float_field, 3.14)
        self.assertEqual(self.null_model.boolean_field, True)
        self.assertEqual(self.null_model.long_field_is_long, 42L)
        self.assertEqual(self.null_model.dict_field["foo"], "bar")
        self.assertEqual(self.null_model.list_field, ["moe", "larry", "curly"])
        self.assertEqual(self.null_model.model_field.string_field, "foo")
