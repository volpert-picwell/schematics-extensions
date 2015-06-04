import pytest

from ..types import StringType
from ..types.compound import ModelType, ListType
from ..models import Model

from ..mockable_list_type import MockableListType
from ..mockable_model_type import MockableModelType

from schematics.exceptions import ValidationError


class ExampleSubmodel(Model):
    attribute = StringType(required=True, min_length=10, max_length=10)


class ExampleModel(Model):
    submodels = MockableListType(MockableModelType(ExampleSubmodel),
                                 required=True)


class ExampleModelWithStrings(Model):
    strings = MockableListType(StringType(min_length=10, max_length=10),
                               required=True)


def test_mockable_list_type_attribute_generates_a_list_of_mocked_models():
    model = ExampleModel.get_mock_object()
    submodel = model.submodels[0]
    assert type(submodel) == ExampleSubmodel
    assert len(submodel.attribute) == 10


def test_mockable_list_type_attribute_works_with_builtin_simple_types():
    model = ExampleModelWithStrings.get_mock_object()
    first_string = model.strings[0]
    assert len(first_string) == 10


def test_list_model_field_exception_with_full_message():
    class User(Model):
        name = StringType(max_length=1)

    class Group(Model):
        users = ListType(ModelType(User))

    g = Group({'users': [{'name': "ToLongName"}]})

    with pytest.raises(ValidationError) as exception:
        g.validate()
    assert exception.value.messages == {
        'users': [{'name': ['String value is too long.']}]
    }
