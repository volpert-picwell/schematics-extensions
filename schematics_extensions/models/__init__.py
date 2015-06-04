from schematics.models import Model
from schematics.exceptions import BaseError, ModelValidationError
from .validate import validate


class Model(Model):

    @classmethod
    def mock(cls, *args, **kwargs):
        return cls.get_mock_object(overrides=kwargs)

    @classmethod
    def get_null_object(cls, overrides=None):
        if overrides is None:
            overrides = {}
        values = {}
        for name, field in cls.fields.items():
            if name not in overrides:
                values[name] = field.null()
        values.update(overrides)
        return cls(values)

    def validate(self, partial=False, strict=False):
        """
        Validates the state of the model and adding additional untrusted data
        as well. If the models is invalid, raises ValidationError with error
        messages.

        THIS IS BEING OVERRIDDEN TEMPORARILY UNTIL THE VALIDATION ORDERING
        FIX IS RELEASED TO SCHEMATICS

        :param partial:
            Allow partial data to validate; useful for PATCH requests.
            Essentially drops the ``required=True`` arguments from field
            definitions. Default: False
        :param strict:
            Complain about unrecognized keys. Default: False
        """
        try:
            data = validate(self.__class__, self._data, partial=partial,
                            strict=strict)
            self._data.update(**data)
        except BaseError as exc:
            raise ModelValidationError(exc.messages)

    def __repr__(self):
        return "{}({!r})".format(self.__class__.__name__, self._data)
