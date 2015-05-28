import unittest

from ..types import IntType

from ..immutable_model import ImmutableModel, ImmutabilityError


class ModelForTesting(ImmutableModel):
    attr = IntType()


class ImmutabilityTest(unittest.TestCase):
    def setUp(self):
        self.model = ModelForTesting({'attr': 5})

    def test_setting_attributes(self):
        with self.assertRaises(ImmutabilityError):
            self.model.attr = 6

        self.assertEqual(5, self.model.attr)

    def test_setting_attributes_via_brackets(self):
        with self.assertRaises(ImmutabilityError):
            self.model['attr'] = 6

        self.assertEqual(5, self.model.attr)


class ImmutabilityErrorTest(unittest.TestCase):
    def test_error_messasge(self):
        error = ImmutabilityError(ModelForTesting(), 'the_key', 'the_value')

        self.assertRegexpMatches(error.message, r"'the_value'")
        self.assertRegexpMatches(error.message, r"'the_key'")
        self.assertRegexpMatches(error.message, r"ModelForTesting")
