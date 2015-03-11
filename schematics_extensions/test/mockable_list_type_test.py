import pytest

from schematics.types import StringType
from schematics.types.compound import ModelType
from schematics.models import Model

from ..mockable_list_type import MockableListType


class ExampleSubmodel(Model):
    attribute = StringType(required=True, min_length=10, max_length=10)


class ExampleModel(Model):
    submodels = MockableListType(ModelType(ExampleSubmodel), required=True)


def test_mockable_list_type_is_attribute_generates_a_list_of_mocked_models():
    model = ExampleModel.get_mock_object()
    submodel = model.submodels[0]
    assert type(submodel) == ExampleSubmodel
    assert len(submodel.attribute) == 10
