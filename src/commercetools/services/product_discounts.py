# DO NOT EDIT! This file is automatically generated
import typing

from commercetools.helpers import RemoveEmptyValuesMixin
from commercetools.platform.models.product_discount import (
    ProductDiscount,
    ProductDiscountDraft,
    ProductDiscountMatchQuery,
    ProductDiscountPagedQueryResponse,
    ProductDiscountUpdate,
    ProductDiscountUpdateAction,
)
from commercetools.typing import OptionalListStr

from . import abstract, traits


class _ProductDiscountQuerySchema(
    traits.ExpandableSchema,
    traits.SortableSchema,
    traits.PagingSchema,
    traits.QuerySchema,
):
    pass


class _ProductDiscountUpdateSchema(traits.ExpandableSchema, traits.VersionedSchema):
    pass


class _ProductDiscountDeleteSchema(traits.VersionedSchema, traits.ExpandableSchema):
    pass


class ProductDiscountService(abstract.AbstractService):
    """Product discounts are used to change certain product prices."""

    def get_by_id(self, id: str, *, expand: OptionalListStr = None) -> ProductDiscount:
        params = self._serialize_params({"expand": expand}, traits.ExpandableSchema)
        return self._client._get(
            endpoint=f"product-discounts/{id}",
            params=params,
            response_class=ProductDiscount,
        )

    def get_by_key(
        self, key: str, *, expand: OptionalListStr = None
    ) -> ProductDiscount:
        params = self._serialize_params({"expand": expand}, traits.ExpandableSchema)
        return self._client._get(
            endpoint=f"product-discounts/key={key}",
            params=params,
            response_class=ProductDiscount,
        )

    def query(
        self,
        *,
        expand: OptionalListStr = None,
        sort: OptionalListStr = None,
        limit: int = None,
        offset: int = None,
        with_total: bool = None,
        where: OptionalListStr = None,
        predicate_var: typing.Dict[str, str] = None,
    ) -> ProductDiscountPagedQueryResponse:
        """Product discounts are used to change certain product prices."""
        params = self._serialize_params(
            {
                "expand": expand,
                "sort": sort,
                "limit": limit,
                "offset": offset,
                "with_total": with_total,
                "where": where,
                "predicate_var": predicate_var,
            },
            _ProductDiscountQuerySchema,
        )
        return self._client._get(
            endpoint="product-discounts",
            params=params,
            response_class=ProductDiscountPagedQueryResponse,
        )

    def create(
        self, draft: ProductDiscountDraft, *, expand: OptionalListStr = None
    ) -> ProductDiscount:
        """Product discounts are used to change certain product prices."""
        params = self._serialize_params({"expand": expand}, traits.ExpandableSchema)
        return self._client._post(
            endpoint="product-discounts",
            params=params,
            data_object=draft,
            response_class=ProductDiscount,
        )

    def update_by_id(
        self,
        id: str,
        version: int,
        actions: typing.List[ProductDiscountUpdateAction],
        *,
        expand: OptionalListStr = None,
        force_update: bool = False,
    ) -> ProductDiscount:
        params = self._serialize_params(
            {"expand": expand}, _ProductDiscountUpdateSchema
        )
        update_action = ProductDiscountUpdate(version=version, actions=actions)
        return self._client._post(
            endpoint=f"product-discounts/{id}",
            params=params,
            data_object=update_action,
            response_class=ProductDiscount,
            force_update=force_update,
        )

    def update_by_key(
        self,
        key: str,
        version: int,
        actions: typing.List[ProductDiscountUpdateAction],
        *,
        expand: OptionalListStr = None,
        force_update: bool = False,
    ) -> ProductDiscount:
        params = self._serialize_params(
            {"expand": expand}, _ProductDiscountUpdateSchema
        )
        update_action = ProductDiscountUpdate(version=version, actions=actions)
        return self._client._post(
            endpoint=f"product-discounts/key={key}",
            params=params,
            data_object=update_action,
            response_class=ProductDiscount,
            force_update=force_update,
        )

    def delete_by_id(
        self,
        id: str,
        version: int,
        *,
        expand: OptionalListStr = None,
        force_delete: bool = False,
    ) -> ProductDiscount:
        params = self._serialize_params(
            {"version": version, "expand": expand}, _ProductDiscountDeleteSchema
        )
        return self._client._delete(
            endpoint=f"product-discounts/{id}",
            params=params,
            response_class=ProductDiscount,
            force_delete=force_delete,
        )

    def delete_by_key(
        self,
        key: str,
        version: int,
        *,
        expand: OptionalListStr = None,
        force_delete: bool = False,
    ) -> ProductDiscount:
        params = self._serialize_params(
            {"version": version, "expand": expand}, _ProductDiscountDeleteSchema
        )
        return self._client._delete(
            endpoint=f"product-discounts/key={key}",
            params=params,
            response_class=ProductDiscount,
            force_delete=force_delete,
        )

    def matching(self, action: ProductDiscountMatchQuery) -> ProductDiscount:
        params: typing.Dict[str, str] = {}
        return self._client._post(
            endpoint="product-discounts/matching",
            params=params,
            data_object=action,
            response_class=ProductDiscount,
        )
