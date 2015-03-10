from schematics.types.compound import ModelType as SchematicsModelType


class MockableModelType(SchematicsModelType):
    def _mock(self, context=None):
        return self.model_class.get_mock_object()
