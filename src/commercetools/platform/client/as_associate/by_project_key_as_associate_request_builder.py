# This file is automatically generated by the rmf-codegen project.
#
# The Python code generator is maintained by Lab Digital. If you want to
# contribute to this project then please do not edit this file directly
# but send a pull request to the Lab Digital fork of rmf-codegen at
# https://github.com/labd/rmf-codegen
import typing
import warnings

from .by_project_key_as_associate_by_associate_id_request_builder import (
    ByProjectKeyAsAssociateByAssociateIdRequestBuilder,
)

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyAsAssociateRequestBuilder:
    _client: "BaseClient"
    _project_key: str

    def __init__(
        self,
        project_key: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._client = client

    def with_associate_id_value(
        self, associate_id: str
    ) -> ByProjectKeyAsAssociateByAssociateIdRequestBuilder:
        return ByProjectKeyAsAssociateByAssociateIdRequestBuilder(
            associate_id=associate_id,
            project_key=self._project_key,
            client=self._client,
        )
