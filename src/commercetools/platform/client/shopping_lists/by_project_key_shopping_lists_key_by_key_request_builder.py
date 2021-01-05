# Generated file, please do not change!!!
import typing

from ...models.common import Update
from ...models.shopping_list import ShoppingList


class ByProjectKeyShoppingListsKeyByKeyRequestBuilder:

    _client: "Client"
    _project_key: str
    _key: str

    def __init__(
        self,
        projectKey: str,
        key: str,
        client: "Client",
    ):
        self._project_key = projectKey
        self._key = key
        self._client = client

    def get(
        self, *, expand: "str" = None, headers: typing.Dict[str, str] = None
    ) -> "ShoppingList":
        """Gets a shopping list by Key."""
        return self._client._get(
            endpoint=f"/{self._project_key}/shopping-lists/key={self._key}",
            params={"expand": expand},
            response_class=ShoppingList,
            headers=headers,
        )

    def post(
        self,
        body: "Update",
        *,
        expand: "str" = None,
        headers: typing.Dict[str, str] = None,
    ) -> "ShoppingList":
        """Update a shopping list found by its Key."""
        return self._client._post(
            endpoint=f"/{self._project_key}/shopping-lists/key={self._key}",
            params={"expand": expand},
            data_object=body,
            response_class=ShoppingList,
            headers={"Content-Type": "application/json", **headers},
        )

    def delete(
        self,
        *,
        data_erasure: "bool" = None,
        version: "int",
        expand: "str" = None,
        headers: typing.Dict[str, str] = None,
    ) -> "ShoppingList":
        """Delete ShoppingList by key"""
        return self._client._delete(
            endpoint=f"/{self._project_key}/shopping-lists/key={self._key}",
            params={"dataErasure": data_erasure, "version": version, "expand": expand},
            response_class=ShoppingList,
            headers=headers,
        )
