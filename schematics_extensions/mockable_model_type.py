from schematics.types.compound import ModelType as SchematicsModelType


class MockableModelType(SchematicsModelType):
    """Version of ModelType that will generate mocks.

    By default, in Schematics, if you have a field of type `ModelType`, when
    you call `get_mock_object()`, that field will be `None`. E.g.:

        class MyModel(Model):
            my_field = ModelType(OtherModel)

        MyModel.get_mock_object().my_field # => None

    If you use MockableModelType, that field will be created by using the
    class' `get_mock_object()`. E.g.:

        class MyModel(MockableModelType):
            my_field = ModelType(OtherModel)

        MyModel.get_mock_object().my_field # => instance of OtherModel

    """

    def _mock(self, context=None):
        return self.model_class.get_mock_object()
