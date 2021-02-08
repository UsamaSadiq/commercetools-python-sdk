# This file is automatically generated by the rmf-codegen project.
#
# The Python code generator is maintained by Lab Digital. If you want to
# contribute to this project then please do not edit this file directly
# but send a pull request to the Lab Digital fork of rmf-codegen at
# https://github.com/labd/rmf-codegen
import typing
import warnings

from ..attributes.by_project_key_missing_data_attributes_request_builder import (
    ByProjectKeyMissingDataAttributesRequestBuilder,
)
from ..images.by_project_key_missing_data_images_request_builder import (
    ByProjectKeyMissingDataImagesRequestBuilder,
)
from ..prices.by_project_key_missing_data_prices_request_builder import (
    ByProjectKeyMissingDataPricesRequestBuilder,
)

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyMissingDataRequestBuilder:

    _client: "BaseClient"
    _project_key: str

    def __init__(
        self,
        project_key: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._client = client

    def attributes(self) -> ByProjectKeyMissingDataAttributesRequestBuilder:
        return ByProjectKeyMissingDataAttributesRequestBuilder(
            project_key=self._project_key,
            client=self._client,
        )

    def images(self) -> ByProjectKeyMissingDataImagesRequestBuilder:
        return ByProjectKeyMissingDataImagesRequestBuilder(
            project_key=self._project_key,
            client=self._client,
        )

    def prices(self) -> ByProjectKeyMissingDataPricesRequestBuilder:
        return ByProjectKeyMissingDataPricesRequestBuilder(
            project_key=self._project_key,
            client=self._client,
        )