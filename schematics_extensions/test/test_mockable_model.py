import pytest

from ..types import StringType
from ..models import Model

from ..mockable_model_type import MockableModelType


class ExampleSubmodel(Model):
    attribute = StringType(required=True, min_length=10, max_length=10)


class ExampleModel(Model):
    submodel = MockableModelType(ExampleSubmodel, required=True)


def test_mockable_model_type_attribute_generates_a_mock():
    model = ExampleModel.get_mock_object()
    assert type(model.submodel) == ExampleSubmodel
    assert len(model.submodel.attribute) == 10
