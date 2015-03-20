from schematics.types.compound import DictType as SchematicsDictType
import random
import string


class MockableDictType(SchematicsDictType):
    """Version of DictType that will generate a list of mocks.

    refer to the MockableListType docs to motivation & caveats.
    """
    def _mock(self, context=None):
        return {self.__rand_key(): self.field._mock()
                for _ in range(random.randint(1, 3)) }


    def __rand_key(self):
        return ''.join(random.choice(string.ascii_letters) for _ in range(5))
