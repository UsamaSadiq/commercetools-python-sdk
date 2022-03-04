# This file is automatically generated by the rmf-codegen project.
#
# The Python code generator is maintained by Lab Digital. If you want to
# contribute to this project then please do not edit this file directly
# but send a pull request to the Lab Digital fork of rmf-codegen at
# https://github.com/labd/rmf-codegen
import typing
import warnings

from ...models.cart import Cart, CartUpdate
from ...models.error import ErrorResponse

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyInStoreKeyByStoreKeyCartsByIDRequestBuilder:

    _client: "BaseClient"
    _project_key: str
    _store_key: str
    _id: str

    def __init__(
        self,
        project_key: str,
        store_key: str,
        id: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._store_key = store_key
        self._id = id
        self._client = client

    def get(
        self,
        *,
        expand: typing.List["str"] = None,
        headers: typing.Dict[str, str] = None,
        options: typing.Dict[str, typing.Any] = None,
    ) -> typing.Optional["Cart"]:
        """Returns a cart by its ID from a specific Store.
        If the cart exists in the commercetools project but does not have the store field,
        or the store field references a different store, this method returns a ResourceNotFound error.
        The cart may not contain up-to-date prices, discounts etc.
        If you want to ensure they're up-to-date, send an Update request with the Recalculate update action instead.

        """
        headers = {} if headers is None else headers
        response = self._client._get(
            endpoint=f"/{self._project_key}/in-store/key={self._store_key}/carts/{self._id}",
            params={"expand": expand},
            headers=headers,
            options=options,
        )
        if response.status_code == 200:
            return Cart.deserialize(response.json())
        elif response.status_code in (400, 401, 403, 500, 502, 503):
            obj = ErrorResponse.deserialize(response.json())
            raise self._client._create_exception(obj, response)
        elif response.status_code == 404:
            return None
        warnings.warn("Unhandled status code %d" % response.status_code)

    def post(
        self,
        body: "CartUpdate",
        *,
        expand: typing.List["str"] = None,
        headers: typing.Dict[str, str] = None,
        options: typing.Dict[str, typing.Any] = None,
    ) -> typing.Optional["Cart"]:
        """Updates a cart in the store specified by {storeKey}.
        If the cart exists in the commercetools project but does not have the store field,
        or the store field references a different store, this method returns a ResourceNotFound error.

        """
        headers = {} if headers is None else headers
        response = self._client._post(
            endpoint=f"/{self._project_key}/in-store/key={self._store_key}/carts/{self._id}",
            params={"expand": expand},
            json=body.serialize(),
            headers={"Content-Type": "application/json", **headers},
            options=options,
        )
        if response.status_code == 200:
            return Cart.deserialize(response.json())
        elif response.status_code in (409, 400, 401, 403, 500, 502, 503):
            obj = ErrorResponse.deserialize(response.json())
            raise self._client._create_exception(obj, response)
        elif response.status_code == 404:
            return None
        warnings.warn("Unhandled status code %d" % response.status_code)

    def delete(
        self,
        *,
        data_erasure: bool = None,
        version: int,
        expand: typing.List["str"] = None,
        headers: typing.Dict[str, str] = None,
        options: typing.Dict[str, typing.Any] = None,
    ) -> typing.Optional["Cart"]:
        headers = {} if headers is None else headers
        response = self._client._delete(
            endpoint=f"/{self._project_key}/in-store/key={self._store_key}/carts/{self._id}",
            params={"dataErasure": data_erasure, "version": version, "expand": expand},
            headers=headers,
            options=options,
        )
        if response.status_code == 200:
            return Cart.deserialize(response.json())
        elif response.status_code in (409, 400, 401, 403, 500, 502, 503):
            obj = ErrorResponse.deserialize(response.json())
            raise self._client._create_exception(obj, response)
        elif response.status_code == 404:
            return None
        warnings.warn("Unhandled status code %d" % response.status_code)
