from schematics.types.compound import ListType as SchematicsListType
from random import randint


class MockableListType(SchematicsListType):
    def _mock(self, context=None):
        return [self.field._mock()
                for _ in range(randint(1, 3))]
