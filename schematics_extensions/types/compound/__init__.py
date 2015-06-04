from schematics.types.compound import DictType, ListType, ModelType
from schematics.exceptions import ValidationError


class DictType(DictType):

    @classmethod
    def null(self):
        return {}


class ListType(ListType):

    @classmethod
    def null(self):
        return []

    # TODO: Remove the following hacks once Schematics 1.0.5 is released.

    # Remove the broken `validate_items` function
    ListType._validators = [
        v for v in ListType._validators
        if v.__name__ is not ListType.validate_items.__name__
    ]

    # Create a new `validate_items` function for the ListType
    def validate_items(self, items):
        errors = []
        for item in items:
            try:
                self.field.validate(item)
            except ValidationError as exc:
                errors.append(exc.messages)

        if errors:
            raise ValidationError(errors)


class ModelType(ModelType):

    @classmethod
    def null(self):
        return None
