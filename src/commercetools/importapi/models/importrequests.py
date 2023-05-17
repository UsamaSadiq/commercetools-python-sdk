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
from .common import ImportResourceType

if typing.TYPE_CHECKING:
    from .categories import CategoryImport
    from .common import ImportResourceType
    from .customers import CustomerImport
    from .importoperations import ImportOperationStatus
    from .inventories import InventoryImport
    from .order_patches import OrderPatchImport
    from .orders import OrderImport
    from .prices import PriceImport
    from .productdrafts import ProductDraftImport
    from .products import ProductImport
    from .producttypes import ProductTypeImport
    from .productvariants import ProductVariantImport, ProductVariantPatch
    from .standalone_prices import StandalonePriceImport
    from .types import TypeImport

__all__ = [
    "CategoryImportRequest",
    "CustomerImportRequest",
    "ImportRequest",
    "ImportResponse",
    "InventoryImportRequest",
    "OrderImportRequest",
    "OrderPatchImportRequest",
    "PriceImportRequest",
    "ProductDraftImportRequest",
    "ProductImportRequest",
    "ProductTypeImportRequest",
    "ProductVariantImportRequest",
    "ProductVariantPatchRequest",
    "StandalonePriceImportRequest",
    "TypeImportRequest",
]


class ImportRequest(_BaseType):
    """An import request batches multiple import resources of the same import resource type for processing by an import container."""

    #: The resource types that can be imported.
    type: "ImportResourceType"

    def __init__(self, *, type: "ImportResourceType"):
        self.type = type

        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ImportRequest":
        if data["type"] == "category":
            from ._schemas.importrequests import CategoryImportRequestSchema

            return CategoryImportRequestSchema().load(data)
        if data["type"] == "product":
            from ._schemas.importrequests import ProductImportRequestSchema

            return ProductImportRequestSchema().load(data)
        if data["type"] == "product-draft":
            from ._schemas.importrequests import ProductDraftImportRequestSchema

            return ProductDraftImportRequestSchema().load(data)
        if data["type"] == "product-type":
            from ._schemas.importrequests import ProductTypeImportRequestSchema

            return ProductTypeImportRequestSchema().load(data)
        if data["type"] == "product-variant":
            from ._schemas.importrequests import ProductVariantImportRequestSchema

            return ProductVariantImportRequestSchema().load(data)
        if data["type"] == "price":
            from ._schemas.importrequests import PriceImportRequestSchema

            return PriceImportRequestSchema().load(data)
        if data["type"] == "standalone-price":
            from ._schemas.importrequests import StandalonePriceImportRequestSchema

            return StandalonePriceImportRequestSchema().load(data)
        if data["type"] == "order":
            from ._schemas.importrequests import OrderImportRequestSchema

            return OrderImportRequestSchema().load(data)
        if data["type"] == "order-patch":
            from ._schemas.importrequests import OrderPatchImportRequestSchema

            return OrderPatchImportRequestSchema().load(data)
        if data["type"] == "product-variant-patch":
            from ._schemas.importrequests import ProductVariantPatchRequestSchema

            return ProductVariantPatchRequestSchema().load(data)
        if data["type"] == "customer":
            from ._schemas.importrequests import CustomerImportRequestSchema

            return CustomerImportRequestSchema().load(data)
        if data["type"] == "inventory":
            from ._schemas.importrequests import InventoryImportRequestSchema

            return InventoryImportRequestSchema().load(data)
        if data["type"] == "type":
            from ._schemas.importrequests import TypeImportRequestSchema

            return TypeImportRequestSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.importrequests import ImportRequestSchema

        return ImportRequestSchema().dump(self)


class ImportResponse(_BaseType):
    """A list of the ID's and validation statuses of newly created [ImportOperations](#importoperation).
    Used as a response at each resource-specific import endpoint, for example, at [Import Categories](/category#import-categories) and [Import ProductTypes](/product-type#import-producttypes).

    """

    operation_status: typing.List["ImportOperationStatus"]

    def __init__(self, *, operation_status: typing.List["ImportOperationStatus"]):
        self.operation_status = operation_status

        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ImportResponse":
        from ._schemas.importrequests import ImportResponseSchema

        return ImportResponseSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.importrequests import ImportResponseSchema

        return ImportResponseSchema().dump(self)


class CategoryImportRequest(ImportRequest):
    """The request body to [import Categories](#import-categories). Contains data for [Categories](/../api/projects/categories#category) to be created or updated in a Project."""

    #: The category import resources of this request.
    resources: typing.List["CategoryImport"]

    def __init__(self, *, resources: typing.List["CategoryImport"]):
        self.resources = resources

        super().__init__(type=ImportResourceType.CATEGORY)

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "CategoryImportRequest":
        from ._schemas.importrequests import CategoryImportRequestSchema

        return CategoryImportRequestSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.importrequests import CategoryImportRequestSchema

        return CategoryImportRequestSchema().dump(self)


class ProductImportRequest(ImportRequest):
    """The request body to [import Products](#import-products). Contains data for [Products](/../api/projects/products#product) to be created or updated in a Project."""

    #: The product import resources of this request.
    resources: typing.List["ProductImport"]

    def __init__(self, *, resources: typing.List["ProductImport"]):
        self.resources = resources

        super().__init__(type=ImportResourceType.PRODUCT)

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ProductImportRequest":
        from ._schemas.importrequests import ProductImportRequestSchema

        return ProductImportRequestSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.importrequests import ProductImportRequestSchema

        return ProductImportRequestSchema().dump(self)


class ProductDraftImportRequest(ImportRequest):
    """The request body to [import ProductDrafts](#import-productdrafts). Contains data for [Products](/../api/projects/products#productdraft) to be created or updated in a Project."""

    #: The product draft import resources of this request.
    resources: typing.List["ProductDraftImport"]

    def __init__(self, *, resources: typing.List["ProductDraftImport"]):
        self.resources = resources

        super().__init__(type=ImportResourceType.PRODUCT_DRAFT)

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductDraftImportRequest":
        from ._schemas.importrequests import ProductDraftImportRequestSchema

        return ProductDraftImportRequestSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.importrequests import ProductDraftImportRequestSchema

        return ProductDraftImportRequestSchema().dump(self)


class ProductTypeImportRequest(ImportRequest):
    """The request body to [import ProductTypes](#import-producttypes). Contains data for [ProductTypes](/../api/projects/productTypes#producttype) to be created or updated in a Project."""

    #: The product type import resources of this request.
    resources: typing.List["ProductTypeImport"]

    def __init__(self, *, resources: typing.List["ProductTypeImport"]):
        self.resources = resources

        super().__init__(type=ImportResourceType.PRODUCT_TYPE)

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductTypeImportRequest":
        from ._schemas.importrequests import ProductTypeImportRequestSchema

        return ProductTypeImportRequestSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.importrequests import ProductTypeImportRequestSchema

        return ProductTypeImportRequestSchema().dump(self)


class ProductVariantImportRequest(ImportRequest):
    """The request body to [import ProductVariants](#import-productvariants). Contains data for [ProductVariants](/../api/projects/products#productvariant) to be created or updated in a Project."""

    #: The product variant import resources of this request.
    resources: typing.List["ProductVariantImport"]

    def __init__(self, *, resources: typing.List["ProductVariantImport"]):
        self.resources = resources

        super().__init__(type=ImportResourceType.PRODUCT_VARIANT)

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductVariantImportRequest":
        from ._schemas.importrequests import ProductVariantImportRequestSchema

        return ProductVariantImportRequestSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.importrequests import ProductVariantImportRequestSchema

        return ProductVariantImportRequestSchema().dump(self)


class PriceImportRequest(ImportRequest):
    """The request body to [import Embedded Prices](#import-embedded-prices). Contains data for [Embedded Prices](/../api/projects/products#embedded-price) to be created or updated in a Project."""

    #: The price import resources of this request.
    resources: typing.List["PriceImport"]

    def __init__(self, *, resources: typing.List["PriceImport"]):
        self.resources = resources

        super().__init__(type=ImportResourceType.PRICE)

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "PriceImportRequest":
        from ._schemas.importrequests import PriceImportRequestSchema

        return PriceImportRequestSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.importrequests import PriceImportRequestSchema

        return PriceImportRequestSchema().dump(self)


class StandalonePriceImportRequest(ImportRequest):
    """The request body to [import Standalone Prices](#import-standalone-prices). Contains data for [Standalone Prices](/../api/projects/standalone-prices#standaloneprice) to be created or updated in a Project."""

    #: The Standalone Price import resources of this request.
    resources: typing.List["StandalonePriceImport"]

    def __init__(self, *, resources: typing.List["StandalonePriceImport"]):
        self.resources = resources

        super().__init__(type=ImportResourceType.STANDALONE_PRICE)

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StandalonePriceImportRequest":
        from ._schemas.importrequests import StandalonePriceImportRequestSchema

        return StandalonePriceImportRequestSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.importrequests import StandalonePriceImportRequestSchema

        return StandalonePriceImportRequestSchema().dump(self)


class OrderImportRequest(ImportRequest):
    """The request body to [import Orders](#import-orders). Contains data for [Orders](/../api/projects/orders#order) to be created in a Project."""

    #: The order import resources of this request.
    resources: typing.List["OrderImport"]

    def __init__(self, *, resources: typing.List["OrderImport"]):
        self.resources = resources

        super().__init__(type=ImportResourceType.ORDER)

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "OrderImportRequest":
        from ._schemas.importrequests import OrderImportRequestSchema

        return OrderImportRequestSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.importrequests import OrderImportRequestSchema

        return OrderImportRequestSchema().dump(self)


class OrderPatchImportRequest(ImportRequest):
    """The request body to [import OrderPatches](#import-orderpatches). The data to be imported are represented by [OrderPatchImport](#orderpatchimport)."""

    #: The order patches of this request
    patches: typing.List["OrderPatchImport"]

    def __init__(self, *, patches: typing.List["OrderPatchImport"]):
        self.patches = patches

        super().__init__(type=ImportResourceType.ORDER_PATCH)

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "OrderPatchImportRequest":
        from ._schemas.importrequests import OrderPatchImportRequestSchema

        return OrderPatchImportRequestSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.importrequests import OrderPatchImportRequestSchema

        return OrderPatchImportRequestSchema().dump(self)


class ProductVariantPatchRequest(ImportRequest):
    """The request body to [import ProductVariantPatches](#import-productvariantpatches). The data to be imported are represented by [ProductVariantPatch](#productvariantpatch)."""

    #: The product variant patches of this request.
    patches: typing.List["ProductVariantPatch"]

    def __init__(self, *, patches: typing.List["ProductVariantPatch"]):
        self.patches = patches

        super().__init__(type=ImportResourceType.PRODUCT_VARIANT_PATCH)

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductVariantPatchRequest":
        from ._schemas.importrequests import ProductVariantPatchRequestSchema

        return ProductVariantPatchRequestSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.importrequests import ProductVariantPatchRequestSchema

        return ProductVariantPatchRequestSchema().dump(self)


class CustomerImportRequest(ImportRequest):
    """The request body to [import Customers](#import-customers). Contains data for [Customers](/../api/projects/customers#customer) to be created or updated in a Project."""

    #: The customer import resources of this request.
    resources: typing.List["CustomerImport"]

    def __init__(self, *, resources: typing.List["CustomerImport"]):
        self.resources = resources

        super().__init__(type=ImportResourceType.CUSTOMER)

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "CustomerImportRequest":
        from ._schemas.importrequests import CustomerImportRequestSchema

        return CustomerImportRequestSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.importrequests import CustomerImportRequestSchema

        return CustomerImportRequestSchema().dump(self)


class InventoryImportRequest(ImportRequest):
    """The request body to [import Inventories](#import-inventory). Contains data for [InventoryEntries](/../api/projects/inventory#inventoryentry) to be created or updated in a commercetools Project."""

    #: The inventory import resources of this request.
    resources: typing.List["InventoryImport"]

    def __init__(self, *, resources: typing.List["InventoryImport"]):
        self.resources = resources

        super().__init__(type=ImportResourceType.INVENTORY)

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "InventoryImportRequest":
        from ._schemas.importrequests import InventoryImportRequestSchema

        return InventoryImportRequestSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.importrequests import InventoryImportRequestSchema

        return InventoryImportRequestSchema().dump(self)


class TypeImportRequest(ImportRequest):
    """The request body to [import Types](#import-types). Contains data for [Types](/../api/projects/types#type) to be created or updated in a Project."""

    #: The type import resources of this request.
    resources: typing.List["TypeImport"]

    def __init__(self, *, resources: typing.List["TypeImport"]):
        self.resources = resources

        super().__init__(type=ImportResourceType.TYPE)

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "TypeImportRequest":
        from ._schemas.importrequests import TypeImportRequestSchema

        return TypeImportRequestSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.importrequests import TypeImportRequestSchema

        return TypeImportRequestSchema().dump(self)
