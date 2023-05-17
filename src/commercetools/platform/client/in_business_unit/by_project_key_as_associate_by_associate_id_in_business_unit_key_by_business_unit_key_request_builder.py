# This file is automatically generated by the rmf-codegen project.
#
# The Python code generator is maintained by Lab Digital. If you want to
# contribute to this project then please do not edit this file directly
# but send a pull request to the Lab Digital fork of rmf-codegen at
# https://github.com/labd/rmf-codegen
import typing
import warnings

from ..carts.by_project_key_as_associate_by_associate_id_in_business_unit_key_by_business_unit_key_carts_request_builder import (
    ByProjectKeyAsAssociateByAssociateIdInBusinessUnitKeyByBusinessUnitKeyCartsRequestBuilder,
)
from ..orders.by_project_key_as_associate_by_associate_id_in_business_unit_key_by_business_unit_key_orders_request_builder import (
    ByProjectKeyAsAssociateByAssociateIdInBusinessUnitKeyByBusinessUnitKeyOrdersRequestBuilder,
)
from ..quote_requests.by_project_key_as_associate_by_associate_id_in_business_unit_key_by_business_unit_key_quote_requests_request_builder import (
    ByProjectKeyAsAssociateByAssociateIdInBusinessUnitKeyByBusinessUnitKeyQuoteRequestsRequestBuilder,
)
from ..quotes.by_project_key_as_associate_by_associate_id_in_business_unit_key_by_business_unit_key_quotes_request_builder import (
    ByProjectKeyAsAssociateByAssociateIdInBusinessUnitKeyByBusinessUnitKeyQuotesRequestBuilder,
)

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyAsAssociateByAssociateIdInBusinessUnitKeyByBusinessUnitKeyRequestBuilder:
    _client: "BaseClient"
    _project_key: str
    _associate_id: str
    _business_unit_key: str

    def __init__(
        self,
        project_key: str,
        associate_id: str,
        business_unit_key: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._associate_id = associate_id
        self._business_unit_key = business_unit_key
        self._client = client

    def carts(
        self,
    ) -> ByProjectKeyAsAssociateByAssociateIdInBusinessUnitKeyByBusinessUnitKeyCartsRequestBuilder:
        """A shopping cart holds product variants and can be ordered."""
        return ByProjectKeyAsAssociateByAssociateIdInBusinessUnitKeyByBusinessUnitKeyCartsRequestBuilder(
            project_key=self._project_key,
            associate_id=self._associate_id,
            business_unit_key=self._business_unit_key,
            client=self._client,
        )

    def orders(
        self,
    ) -> ByProjectKeyAsAssociateByAssociateIdInBusinessUnitKeyByBusinessUnitKeyOrdersRequestBuilder:
        return ByProjectKeyAsAssociateByAssociateIdInBusinessUnitKeyByBusinessUnitKeyOrdersRequestBuilder(
            project_key=self._project_key,
            associate_id=self._associate_id,
            business_unit_key=self._business_unit_key,
            client=self._client,
        )

    def quotes(
        self,
    ) -> ByProjectKeyAsAssociateByAssociateIdInBusinessUnitKeyByBusinessUnitKeyQuotesRequestBuilder:
        """A quote holds the negotiated offer."""
        return ByProjectKeyAsAssociateByAssociateIdInBusinessUnitKeyByBusinessUnitKeyQuotesRequestBuilder(
            project_key=self._project_key,
            associate_id=self._associate_id,
            business_unit_key=self._business_unit_key,
            client=self._client,
        )

    def quote_requests(
        self,
    ) -> ByProjectKeyAsAssociateByAssociateIdInBusinessUnitKeyByBusinessUnitKeyQuoteRequestsRequestBuilder:
        return ByProjectKeyAsAssociateByAssociateIdInBusinessUnitKeyByBusinessUnitKeyQuoteRequestsRequestBuilder(
            project_key=self._project_key,
            associate_id=self._associate_id,
            business_unit_key=self._business_unit_key,
            client=self._client,
        )
