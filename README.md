# schematics-extensions [![Build Status](https://travis-ci.org/picwell/schematics-extensions.svg?branch=master)](https://travis-ci.org/picwell/schematics-extensions)

Adds new functionality to [Schematics models](https://github.com/schematics/schematics)


# Mockable ModelType and ListType

Schematics has a really useful `get_mock_object` function.

However, for models which contain ListType and ModelType fields, the behavior is broken


```
> Household.get_mock_object().validate()
*** ModelValidationError: {'members': [u'This field is required.']}`
```

If a field is ListType or ModelType, get_mock_object sets the field to None.

MockableListType and MockableModelType inherit from the Schematics ListType and ModelType, but have the correct behavior for get_mock_object():

```
# this will not raise an AttributeError
Household.get_mock_object().validate()
```


It's easy to drop the mockable versions in as replacements:

```
from schematics_extensions import MockableModelType as ModelType
from schematics_extensions import MockableListType as ListType
```

# Immutable models

A subclass of SchematicsModel which raises exceptions if you try to assign a new value to a field. Because sometimes you want immutable values.


```
> x = Household.get_mock_object()
> x.income = 4000
*** ImmutabilityError: Could not assign value 'income' to 4000 on <Household: Household object>because the object is immutable
```



# NumericString Type

A new type which is only valid if the value is a string of decimal digits.

# Changelog

## 0.0.3
  - Add `get_null_object` to return null-types.
