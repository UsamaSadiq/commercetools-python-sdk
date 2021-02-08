# This file is automatically generated by the rmf-codegen project.
#
# The Python code generator is maintained by Lab Digital. If you want to
# contribute to this project then please do not edit this file directly
# but send a pull request to the Lab Digital fork of rmf-codegen at
# https://github.com/labd/rmf-codegen
import typing
import warnings

from ...models.common import ProcessingState
from ...models.importoperations import ImportOperationPagedResponse
from .by_project_key_orders_import_sink_key_by_import_sink_key_import_operations_by_id_request_builder import (
    ByProjectKeyOrdersImportSinkKeyByImportSinkKeyImportOperationsByIdRequestBuilder,
)

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyOrdersImportSinkKeyByImportSinkKeyImportOperationsRequestBuilder:

    _client: "BaseClient"
    _project_key: str
    _import_sink_key: str

    def __init__(
        self,
        project_key: str,
        import_sink_key: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._import_sink_key = import_sink_key
        self._client = client

    def with_id_value(
        self, id: str
    ) -> ByProjectKeyOrdersImportSinkKeyByImportSinkKeyImportOperationsByIdRequestBuilder:
        return ByProjectKeyOrdersImportSinkKeyByImportSinkKeyImportOperationsByIdRequestBuilder(
            id=id,
            project_key=self._project_key,
            import_sink_key=self._import_sink_key,
            client=self._client,
        )

    def get(
        self,
        *,
        limit: float = None,
        offset: float = None,
        sort: typing.List["str"] = None,
        resource_key: str = None,
        state: "ProcessingState" = None,
        headers: typing.Dict[str, str] = None,
        options: typing.Dict[str, typing.Any] = None,
    ) -> "ImportOperationPagedResponse":
        """Retrieves all order import operations of an import sink key."""
        headers = {} if headers is None else headers
        response = self._client._get(
            endpoint=f"/{self._project_key}/orders/importSinkKey={self._import_sink_key}/import-operations",
            params={
                "limit": limit,
                "offset": offset,
                "sort": sort,
                "resourceKey": resource_key,
                "state": state,
            },
            headers=headers,
            options=options,
        )
        if response.status_code == 200:
            return ImportOperationPagedResponse.deserialize(response.json())
        warnings.warn("Unhandled status code %d" % response.status_code)