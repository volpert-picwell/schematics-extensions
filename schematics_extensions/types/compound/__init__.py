from schematics.types.compound import DictType, ListType, ModelType


class DictType(DictType):

    @classmethod
    def null(self):
        return {}


class ListType(ListType):

    @classmethod
    def null(self):
        return []


class ModelType(ModelType):

    @classmethod
    def null(self):
        return None
