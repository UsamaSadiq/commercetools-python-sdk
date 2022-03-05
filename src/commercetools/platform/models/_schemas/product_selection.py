# This file is automatically generated by the rmf-codegen project.
#
# The Python code generator is maintained by Lab Digital. If you want to
# contribute to this project then please do not edit this file directly
# but send a pull request to the Lab Digital fork of rmf-codegen at
# https://github.com/labd/rmf-codegen
import re
import typing

import marshmallow
import marshmallow_enum

from commercetools import helpers

from ... import models
from ..common import ReferenceTypeId
from ..product_selection import ProductSelectionTypeEnum
from .common import (
    BaseResourceSchema,
    LocalizedStringField,
    ReferenceSchema,
    ResourceIdentifierSchema,
)
from .type import FieldContainerField

# Fields


# Marshmallow Schemas
class AssignedProductReferenceSchema(helpers.BaseSchema):
    product = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".product.ProductReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.AssignedProductReference(**data)


class AssignedProductSelectionSchema(helpers.BaseSchema):
    product_selection = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ProductSelectionReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="productSelection",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.AssignedProductSelection(**data)


class AssignedProductSelectionPagedQueryResponseSchema(helpers.BaseSchema):
    limit = marshmallow.fields.Integer(allow_none=True, missing=None)
    offset = marshmallow.fields.Integer(allow_none=True, missing=None)
    count = marshmallow.fields.Integer(allow_none=True, missing=None)
    total = marshmallow.fields.Integer(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    results = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".AssignedProductSelectionSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.AssignedProductSelectionPagedQueryResponse(**data)


class ProductSelectionSchema(BaseResourceSchema):
    last_modified_by = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.LastModifiedBySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="lastModifiedBy",
    )
    created_by = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.CreatedBySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="createdBy",
    )
    key = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    name = LocalizedStringField(
        allow_none=True, values=marshmallow.fields.String(allow_none=True), missing=None
    )
    product_count = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="productCount"
    )
    type = marshmallow_enum.EnumField(
        ProductSelectionTypeEnum, by_value=True, allow_none=True, missing=None
    )
    custom = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".type.CustomFieldsSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ProductSelection(**data)


class ProductSelectionAssignmentSchema(helpers.BaseSchema):
    product = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".product.ProductReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    product_selection = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ProductSelectionReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="productSelection",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ProductSelectionAssignment(**data)


class ProductSelectionDraftSchema(helpers.BaseSchema):
    key = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    name = LocalizedStringField(
        allow_none=True, values=marshmallow.fields.String(allow_none=True), missing=None
    )
    custom = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".type.CustomFieldsDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ProductSelectionDraft(**data)


class ProductSelectionPagedQueryResponseSchema(helpers.BaseSchema):
    limit = marshmallow.fields.Integer(allow_none=True, missing=None)
    offset = marshmallow.fields.Integer(allow_none=True, missing=None)
    count = marshmallow.fields.Integer(allow_none=True, missing=None)
    total = marshmallow.fields.Integer(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    results = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ProductSelectionSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ProductSelectionPagedQueryResponse(**data)


class ProductSelectionProductPagedQueryResponseSchema(helpers.BaseSchema):
    limit = marshmallow.fields.Integer(allow_none=True, missing=None)
    offset = marshmallow.fields.Integer(allow_none=True, missing=None)
    count = marshmallow.fields.Integer(allow_none=True, missing=None)
    total = marshmallow.fields.Integer(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    results = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".AssignedProductReferenceSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ProductSelectionProductPagedQueryResponse(**data)


class ProductSelectionReferenceSchema(ReferenceSchema):
    obj = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ProductSelectionSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return models.ProductSelectionReference(**data)


class ProductSelectionResourceIdentifierSchema(ResourceIdentifierSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return models.ProductSelectionResourceIdentifier(**data)


class ProductSelectionTypeSchema(helpers.BaseSchema):
    type = marshmallow_enum.EnumField(
        ProductSelectionTypeEnum, by_value=True, allow_none=True, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.ProductSelectionType(**data)


class IndividualProductSelectionTypeSchema(ProductSelectionTypeSchema):
    name = LocalizedStringField(
        allow_none=True, values=marshmallow.fields.String(allow_none=True), missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.IndividualProductSelectionType(**data)


class ProductSelectionUpdateSchema(helpers.BaseSchema):
    version = marshmallow.fields.Integer(allow_none=True, missing=None)
    actions = marshmallow.fields.List(
        helpers.Discriminator(
            allow_none=True,
            discriminator_field=("action", "action"),
            discriminator_schemas={
                "addProduct": helpers.absmod(
                    __name__, ".ProductSelectionAddProductActionSchema"
                ),
                "changeName": helpers.absmod(
                    __name__, ".ProductSelectionChangeNameActionSchema"
                ),
                "removeProduct": helpers.absmod(
                    __name__, ".ProductSelectionRemoveProductActionSchema"
                ),
                "setCustomField": helpers.absmod(
                    __name__, ".ProductSelectionSetCustomFieldActionSchema"
                ),
                "setCustomType": helpers.absmod(
                    __name__, ".ProductSelectionSetCustomTypeActionSchema"
                ),
                "setKey": helpers.absmod(
                    __name__, ".ProductSelectionSetKeyActionSchema"
                ),
            },
        ),
        allow_none=True,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ProductSelectionUpdate(**data)


class ProductSelectionUpdateActionSchema(helpers.BaseSchema):
    action = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductSelectionUpdateAction(**data)


class ProductsInStorePagedQueryResponseSchema(helpers.BaseSchema):
    limit = marshmallow.fields.Integer(allow_none=True, missing=None)
    offset = marshmallow.fields.Integer(allow_none=True, missing=None)
    count = marshmallow.fields.Integer(allow_none=True, missing=None)
    total = marshmallow.fields.Integer(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    results = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ProductSelectionAssignmentSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ProductsInStorePagedQueryResponse(**data)


class ProductSelectionAddProductActionSchema(ProductSelectionUpdateActionSchema):
    product = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".product.ProductResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductSelectionAddProductAction(**data)


class ProductSelectionChangeNameActionSchema(ProductSelectionUpdateActionSchema):
    name = LocalizedStringField(
        allow_none=True, values=marshmallow.fields.String(allow_none=True), missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductSelectionChangeNameAction(**data)


class ProductSelectionRemoveProductActionSchema(ProductSelectionUpdateActionSchema):
    product = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".product.ProductResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductSelectionRemoveProductAction(**data)


class ProductSelectionSetCustomFieldActionSchema(ProductSelectionUpdateActionSchema):
    name = marshmallow.fields.String(allow_none=True, missing=None)
    value = marshmallow.fields.Raw(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductSelectionSetCustomFieldAction(**data)


class ProductSelectionSetCustomTypeActionSchema(ProductSelectionUpdateActionSchema):
    type = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".type.TypeResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )
    fields = FieldContainerField(
        allow_none=True,
        values=marshmallow.fields.Raw(allow_none=True),
        metadata={"omit_empty": True},
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductSelectionSetCustomTypeAction(**data)


class ProductSelectionSetKeyActionSchema(ProductSelectionUpdateActionSchema):
    key = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProductSelectionSetKeyAction(**data)