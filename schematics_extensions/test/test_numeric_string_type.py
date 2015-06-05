import unittest

from schematics.exceptions import ValidationError
from ..models import Model

from ..numeric_string_type import NumericStringType


class ModelForTesting(Model):
    numeric_string = NumericStringType(length=11)


class NumericStringTypeTest(unittest.TestCase):
    def assertValidWith(self, value):
        test_model = ModelForTesting({'numeric_string': value})
        test_model.validate()

    def assertInvalidWith(self, value):
        test_model = ModelForTesting({'numeric_string': value})
        self.assertRaises(ValidationError, test_model.validate)

    def test_validity(self):
        self.assertValidWith('12345678901')
        self.assertValidWith(12345678901)

    def test_invalidity(self):
        self.assertInvalidWith('123456789012')
        self.assertInvalidWith('1234567890')

    def test_not_required_by_default(self):
        class ModelForTesting(Model):
            numeric_string = NumericStringType(length=11)

        ModelForTesting().validate()

    def test_can_be_required(self):
        class ModelForTesting(Model):
            numeric_string = NumericStringType(length=11, required=True)

        self.assertRaises(ValidationError, ModelForTesting().validate)

    def test_generates_valid_mocks(self):
        class ModelForTesting(Model):
            numeric_string = NumericStringType(length=11, required=True)

        ModelForTesting.get_mock_object().validate()

    def test_decent_error_message(self):
        class ModelForTesting(Model):
            numeric_string = NumericStringType(length=11, required=True)

        test_model = ModelForTesting({'numeric_string': 'abcde'})

        self.assertRaisesRegexp(ValidationError, r'11', test_model.validate)

    def test_length_is_not_required(self):
        class ModelForTesting(Model):
            numeric_string = NumericStringType(required=True)

        test_model = ModelForTesting({'numeric_string': '1234'})

    def test_max_length_is_honored(self):
        class ModelForTesting(Model):
            numeric_string = NumericStringType(required=True, max_length=5)

        valid_model = ModelForTesting({'numeric_string': '12345'})
        valid_model.validate()
        invalid_model = ModelForTesting({'numeric_string': '123456'})
        self.assertRaises(ValidationError, invalid_model.validate)

    def test_mock_honors_max_length(self):
        class ModelForTesting(Model):
            numeric_string = NumericStringType(required=True, max_length=5)

        for _ in range(100):
            model = ModelForTesting.get_mock_object()
            model.validate()
            mock_length = len(model.numeric_string)
            self.assertTrue(mock_length <= 5)

    def test_mock_doesnt_require_max_length(self):
        class ModelForTesting(Model):
            numeric_string = NumericStringType(required=True)

        ModelForTesting.get_mock_object().validate()

    def test_non_string_doesnt_break_validation(self):
        class ModelForTesting(Model):
            numeric_string = NumericStringType(required=True, length=5)

        model = ModelForTesting({'numeric_string': 12345}).validate()
