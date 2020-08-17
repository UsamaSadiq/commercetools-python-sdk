# DO NOT EDIT! This file is automatically generated
import marshmallow
import marshmallow_enum

from commercetools import helpers, types
from commercetools._schemas._common import (
    BaseResourceSchema,
    LocalizedStringField,
    ReferenceSchema,
    ResourceIdentifierSchema,
)
from commercetools._schemas._type import FieldContainerField

__all__ = [
    "ChannelAddRolesActionSchema",
    "ChannelChangeDescriptionActionSchema",
    "ChannelChangeKeyActionSchema",
    "ChannelChangeNameActionSchema",
    "ChannelDraftSchema",
    "ChannelPagedQueryResponseSchema",
    "ChannelReferenceSchema",
    "ChannelRemoveRolesActionSchema",
    "ChannelResourceIdentifierSchema",
    "ChannelSchema",
    "ChannelSetAddressActionSchema",
    "ChannelSetCustomFieldActionSchema",
    "ChannelSetCustomTypeActionSchema",
    "ChannelSetGeoLocationActionSchema",
    "ChannelSetRolesActionSchema",
    "ChannelUpdateActionSchema",
    "ChannelUpdateSchema",
]


class ChannelDraftSchema(marshmallow.Schema):
    """Marshmallow schema for :class:`commercetools.types.ChannelDraft`."""

    key = marshmallow.fields.String(allow_none=True)
    roles = marshmallow.fields.List(
        marshmallow_enum.EnumField(types.ChannelRoleEnum, by_value=True), missing=None
    )
    name = LocalizedStringField(allow_none=True, missing=None)
    description = LocalizedStringField(allow_none=True, missing=None)
    address = helpers.LazyNestedField(
        nested="commercetools._schemas._common.AddressSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )
    custom = helpers.LazyNestedField(
        nested="commercetools._schemas._type.CustomFieldsDraftSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )
    geo_location = helpers.Discriminator(
        discriminator_field=("type", "type"),
        discriminator_schemas={
            "Point": "commercetools._schemas._common.GeoJsonPointSchema"
        },
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
        data_key="geoLocation",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.ChannelDraft(**data)


class ChannelPagedQueryResponseSchema(marshmallow.Schema):
    """Marshmallow schema for :class:`commercetools.types.ChannelPagedQueryResponse`."""

    limit = marshmallow.fields.Integer(allow_none=True)
    count = marshmallow.fields.Integer(allow_none=True)
    total = marshmallow.fields.Integer(allow_none=True, missing=None)
    offset = marshmallow.fields.Integer(allow_none=True)
    results = helpers.LazyNestedField(
        nested="commercetools._schemas._channel.ChannelSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        many=True,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.ChannelPagedQueryResponse(**data)


class ChannelReferenceSchema(ReferenceSchema):
    """Marshmallow schema for :class:`commercetools.types.ChannelReference`."""

    obj = helpers.LazyNestedField(
        nested="commercetools._schemas._channel.ChannelSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return types.ChannelReference(**data)


class ChannelResourceIdentifierSchema(ResourceIdentifierSchema):
    """Marshmallow schema for :class:`commercetools.types.ChannelResourceIdentifier`."""

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return types.ChannelResourceIdentifier(**data)


class ChannelSchema(BaseResourceSchema):
    """Marshmallow schema for :class:`commercetools.types.Channel`."""

    id = marshmallow.fields.String(allow_none=True)
    version = marshmallow.fields.Integer(allow_none=True)
    created_at = marshmallow.fields.DateTime(allow_none=True, data_key="createdAt")
    last_modified_at = marshmallow.fields.DateTime(
        allow_none=True, data_key="lastModifiedAt"
    )
    last_modified_by = helpers.LazyNestedField(
        nested="commercetools._schemas._common.LastModifiedBySchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
        data_key="lastModifiedBy",
    )
    created_by = helpers.LazyNestedField(
        nested="commercetools._schemas._common.CreatedBySchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
        data_key="createdBy",
    )
    key = marshmallow.fields.String(allow_none=True)
    roles = marshmallow.fields.List(
        marshmallow_enum.EnumField(types.ChannelRoleEnum, by_value=True)
    )
    name = LocalizedStringField(allow_none=True, missing=None)
    description = LocalizedStringField(allow_none=True, missing=None)
    address = helpers.LazyNestedField(
        nested="commercetools._schemas._common.AddressSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )
    review_rating_statistics = helpers.LazyNestedField(
        nested="commercetools._schemas._review.ReviewRatingStatisticsSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
        data_key="reviewRatingStatistics",
    )
    custom = helpers.LazyNestedField(
        nested="commercetools._schemas._type.CustomFieldsSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )
    geo_location = helpers.Discriminator(
        discriminator_field=("type", "type"),
        discriminator_schemas={
            "Point": "commercetools._schemas._common.GeoJsonPointSchema"
        },
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
        data_key="geoLocation",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.Channel(**data)


class ChannelUpdateActionSchema(marshmallow.Schema):
    """Marshmallow schema for :class:`commercetools.types.ChannelUpdateAction`."""

    action = marshmallow.fields.String(allow_none=True)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ChannelUpdateAction(**data)


class ChannelUpdateSchema(marshmallow.Schema):
    """Marshmallow schema for :class:`commercetools.types.ChannelUpdate`."""

    version = marshmallow.fields.Integer(allow_none=True)
    actions = marshmallow.fields.List(
        helpers.Discriminator(
            discriminator_field=("action", "action"),
            discriminator_schemas={
                "addRoles": "commercetools._schemas._channel.ChannelAddRolesActionSchema",
                "changeDescription": "commercetools._schemas._channel.ChannelChangeDescriptionActionSchema",
                "changeKey": "commercetools._schemas._channel.ChannelChangeKeyActionSchema",
                "changeName": "commercetools._schemas._channel.ChannelChangeNameActionSchema",
                "removeRoles": "commercetools._schemas._channel.ChannelRemoveRolesActionSchema",
                "setAddress": "commercetools._schemas._channel.ChannelSetAddressActionSchema",
                "setCustomField": "commercetools._schemas._channel.ChannelSetCustomFieldActionSchema",
                "setCustomType": "commercetools._schemas._channel.ChannelSetCustomTypeActionSchema",
                "setGeoLocation": "commercetools._schemas._channel.ChannelSetGeoLocationActionSchema",
                "setRoles": "commercetools._schemas._channel.ChannelSetRolesActionSchema",
            },
            unknown=marshmallow.EXCLUDE,
            allow_none=True,
        ),
        allow_none=True,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.ChannelUpdate(**data)


class ChannelAddRolesActionSchema(ChannelUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.ChannelAddRolesAction`."""

    roles = marshmallow.fields.List(
        marshmallow_enum.EnumField(types.ChannelRoleEnum, by_value=True)
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ChannelAddRolesAction(**data)


class ChannelChangeDescriptionActionSchema(ChannelUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.ChannelChangeDescriptionAction`."""

    description = LocalizedStringField(allow_none=True)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ChannelChangeDescriptionAction(**data)


class ChannelChangeKeyActionSchema(ChannelUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.ChannelChangeKeyAction`."""

    key = marshmallow.fields.String(allow_none=True)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ChannelChangeKeyAction(**data)


class ChannelChangeNameActionSchema(ChannelUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.ChannelChangeNameAction`."""

    name = LocalizedStringField(allow_none=True)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ChannelChangeNameAction(**data)


class ChannelRemoveRolesActionSchema(ChannelUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.ChannelRemoveRolesAction`."""

    roles = marshmallow.fields.List(
        marshmallow_enum.EnumField(types.ChannelRoleEnum, by_value=True)
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ChannelRemoveRolesAction(**data)


class ChannelSetAddressActionSchema(ChannelUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.ChannelSetAddressAction`."""

    address = helpers.LazyNestedField(
        nested="commercetools._schemas._common.AddressSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ChannelSetAddressAction(**data)


class ChannelSetCustomFieldActionSchema(ChannelUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.ChannelSetCustomFieldAction`."""

    name = marshmallow.fields.String(allow_none=True)
    value = marshmallow.fields.Raw(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ChannelSetCustomFieldAction(**data)


class ChannelSetCustomTypeActionSchema(ChannelUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.ChannelSetCustomTypeAction`."""

    type = helpers.LazyNestedField(
        nested="commercetools._schemas._type.TypeResourceIdentifierSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )
    fields = FieldContainerField(allow_none=True, missing=None)  # type: ignore

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ChannelSetCustomTypeAction(**data)


class ChannelSetGeoLocationActionSchema(ChannelUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.ChannelSetGeoLocationAction`."""

    geo_location = helpers.Discriminator(
        discriminator_field=("type", "type"),
        discriminator_schemas={
            "Point": "commercetools._schemas._common.GeoJsonPointSchema"
        },
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
        data_key="geoLocation",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ChannelSetGeoLocationAction(**data)


class ChannelSetRolesActionSchema(ChannelUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.ChannelSetRolesAction`."""

    roles = marshmallow.fields.List(
        marshmallow_enum.EnumField(types.ChannelRoleEnum, by_value=True)
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ChannelSetRolesAction(**data)
