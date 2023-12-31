# This file is automatically generated by the rmf-codegen project.
#
# The Python code generator is maintained by Lab Digital. If you want to
# contribute to this project then please do not edit this file directly
# but send a pull request to the Lab Digital fork of rmf-codegen at
# https://github.com/labd/rmf-codegen

import datetime
import enum
import typing

from ._abstract import _BaseType

__all__ = ["StoreCountry"]


class StoreCountry(_BaseType):
    #: Two-digit country code as per [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).
    code: str

    def __init__(self, *, code: str):
        self.code = code

        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "StoreCountry":
        from ._schemas.store_country import StoreCountrySchema

        return StoreCountrySchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.store_country import StoreCountrySchema

        return StoreCountrySchema().dump(self)
