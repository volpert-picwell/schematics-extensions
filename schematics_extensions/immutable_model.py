from .models import Model as SchematicsModel


class ImmutableModel(SchematicsModel):
    """Model that cannot be changed once it is initialized.

    Any change will raise an ImmutabilityError.
    """

    def __init__(self, *args, **kwargs):
        self._initialized = False
        super(ImmutableModel, self).__init__(*args, **kwargs)
        self._initialized = True

    def __setattr__(self, name, value):
        if name is not '_initialized' and self._initialized:
            raise ImmutabilityError(self, name, value)

        return super(ImmutableModel, self).__setattr__(name, value)


class ImmutabilityError(AttributeError):
    """Raised by an ImmutableModel if it is changed."""

    def __init__(self, model, attr_name, attr_value):
        message_format = "Could not assign value %r to %r on %r" + \
            "because the object is immutable"
        message = message_format % (attr_name, attr_value, model)

        super(ImmutabilityError, self).__init__(message)
