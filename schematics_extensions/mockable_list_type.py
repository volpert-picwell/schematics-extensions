from schematics.types.compound import ListType as SchematicsListType
from random import randint


class MockableListType(SchematicsListType):
    def _mock(self, context=None):
        return [self.model_class.get_mock_object()
                for _ in range(randint(1, 3))]
