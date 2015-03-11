from schematics.types.compound import ListType as SchematicsListType
from random import randint


class MockableListType(SchematicsListType):
    """Version of ModelListType that will generate a list of mocks.

    By default, in Schematics, if you have a field of type `ModelListType`,
    when you call `get_mock_object()`, that field will be `None`, instead of a
    list. E.g.:

        class MyModel(Model):
            my_strings = ListType(StringType)

        MyModel.get_mock_object().my_strings # => None

    If you use `MockableListType`, that field will be created by using the
    class' `get_mock_object()` for that type. E.g.:

        class MyModel(Model):
            my_strings = MockableListType(StringType)

        MyModel.get_mock_object().my_field # => ['mncxvxcv', 'cvriytr', ...]

    Caveat: if you have a list of model objects that you want to be mockable,
    you must use MockableListType in conjunction with MockableModelType. E.g.:

        class MyModel(Model):
            my_field = MockableListType(MockableModelType(OtherModel))

    """

    def _mock(self, context=None):
        return [self.field._mock()
                for _ in range(randint(1, 3))]
