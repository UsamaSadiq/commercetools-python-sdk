# This file is automatically generated by the rmf-codegen project.
#
# The Python code generator is maintained by Lab Digital. If you want to
# contribute to this project then please do not edit this file directly
# but send a pull request to the Lab Digital fork of rmf-codegen at
# https://github.com/labd/rmf-codegen
import typing
import warnings

from ..business_units.by_project_key_as_associate_by_associate_id_business_units_request_builder import (
    ByProjectKeyAsAssociateByAssociateIdBusinessUnitsRequestBuilder,
)
from ..in_business_unit.by_project_key_as_associate_by_associate_id_in_business_unit_key_by_business_unit_key_request_builder import (
    ByProjectKeyAsAssociateByAssociateIdInBusinessUnitKeyByBusinessUnitKeyRequestBuilder,
)

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyAsAssociateByAssociateIdRequestBuilder:
    _client: "BaseClient"
    _project_key: str
    _associate_id: str

    def __init__(
        self,
        project_key: str,
        associate_id: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._associate_id = associate_id
        self._client = client

    def business_units(
        self,
    ) -> ByProjectKeyAsAssociateByAssociateIdBusinessUnitsRequestBuilder:
        """A Business Unit can represent a Company or a Division."""
        return ByProjectKeyAsAssociateByAssociateIdBusinessUnitsRequestBuilder(
            project_key=self._project_key,
            associate_id=self._associate_id,
            client=self._client,
        )

    def in_business_unit_key_with_business_unit_key_value(
        self, business_unit_key: str
    ) -> ByProjectKeyAsAssociateByAssociateIdInBusinessUnitKeyByBusinessUnitKeyRequestBuilder:
        return ByProjectKeyAsAssociateByAssociateIdInBusinessUnitKeyByBusinessUnitKeyRequestBuilder(
            business_unit_key=business_unit_key,
            project_key=self._project_key,
            associate_id=self._associate_id,
            client=self._client,
        )