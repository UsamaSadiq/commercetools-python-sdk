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
from .common import (
    BaseResource,
    KeyReference,
    Reference,
    ReferenceTypeId,
    ResourceIdentifier,
)

if typing.TYPE_CHECKING:
    from .channel import ChannelReference, ChannelResourceIdentifier
    from .common import (
        CreatedBy,
        LastModifiedBy,
        LocalizedString,
        ReferenceTypeId,
        ResourceIdentifier,
    )
    from .product_selection import (
        ProductSelectionReference,
        ProductSelectionResourceIdentifier,
    )
    from .type import (
        CustomFields,
        CustomFieldsDraft,
        FieldContainer,
        TypeResourceIdentifier,
    )

__all__ = [
    "ProductSelectionSetting",
    "ProductSelectionSettingDraft",
    "Store",
    "StoreAddDistributionChannelAction",
    "StoreAddProductSelectionAction",
    "StoreAddSupplyChannelAction",
    "StoreChangeProductSelectionAction",
    "StoreDraft",
    "StoreKeyReference",
    "StorePagedQueryResponse",
    "StoreReference",
    "StoreRemoveDistributionChannelAction",
    "StoreRemoveProductSelectionAction",
    "StoreRemoveSupplyChannelAction",
    "StoreResourceIdentifier",
    "StoreSetCustomFieldAction",
    "StoreSetCustomTypeAction",
    "StoreSetDistributionChannelsAction",
    "StoreSetLanguagesAction",
    "StoreSetNameAction",
    "StoreSetProductSelectionsAction",
    "StoreSetSupplyChannelsAction",
    "StoreUpdate",
    "StoreUpdateAction",
]


class ProductSelectionSetting(_BaseType):
    #: Reference to a Product Selection
    product_selection: "ProductSelectionReference"
    #: If `true` all Products assigned to this Product Selection are part of the Store's assortment.
    active: bool

    def __init__(self, *, product_selection: "ProductSelectionReference", active: bool):
        self.product_selection = product_selection
        self.active = active
        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductSelectionSetting":
        from ._schemas.store import ProductSelectionSettingSchema

        return ProductSelectionSettingSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.store import ProductSelectionSettingSchema

        return ProductSelectionSettingSchema().dump(self)


class ProductSelectionSettingDraft(_BaseType):
    #: Resource Identifier of a Product Selection
    product_selection: "ProductSelectionResourceIdentifier"
    #: If `true` all Products assigned to this Product Selection become part of the Store's assortment.
    active: typing.Optional[bool]

    def __init__(
        self,
        *,
        product_selection: "ProductSelectionResourceIdentifier",
        active: typing.Optional[bool] = None
    ):
        self.product_selection = product_selection
        self.active = active
        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductSelectionSettingDraft":
        from ._schemas.store import ProductSelectionSettingDraftSchema

        return ProductSelectionSettingDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.store import ProductSelectionSettingDraftSchema

        return ProductSelectionSettingDraftSchema().dump(self)


class Store(BaseResource):
    #: Present on resources created after 1 February 2019 except for [events not tracked](/client-logging#events-tracked).
    last_modified_by: typing.Optional["LastModifiedBy"]
    #: Present on resources created after 1 February 2019 except for [events not tracked](/client-logging#events-tracked).
    created_by: typing.Optional["CreatedBy"]
    #: User-specific unique identifier for the store.
    #: The `key` is mandatory and immutable.
    #: It is used to reference the store.
    key: str
    #: The name of the store
    name: typing.Optional["LocalizedString"]
    languages: typing.Optional[typing.List["str"]]
    #: Set of References to a Channel with `ProductDistribution` role
    distribution_channels: typing.List["ChannelReference"]
    #: Set of ResourceIdentifiers of Channels with `InventorySupply` role
    supply_channels: typing.Optional[typing.List["ChannelReference"]]
    #: Set of References to Product Selections along with settings.
    #: If `productSelections` is empty all products in the project are available in this Store.
    #: If `productSelections` is not empty but there exists no `active` Product Selection then no Product is available in this Store.
    product_selections: typing.Optional[typing.List["ProductSelectionSetting"]]
    custom: typing.Optional["CustomFields"]

    def __init__(
        self,
        *,
        id: str,
        version: int,
        created_at: datetime.datetime,
        last_modified_at: datetime.datetime,
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        key: str,
        name: typing.Optional["LocalizedString"] = None,
        languages: typing.Optional[typing.List["str"]] = None,
        distribution_channels: typing.List["ChannelReference"],
        supply_channels: typing.Optional[typing.List["ChannelReference"]] = None,
        product_selections: typing.Optional[
            typing.List["ProductSelectionSetting"]
        ] = None,
        custom: typing.Optional["CustomFields"] = None
    ):
        self.last_modified_by = last_modified_by
        self.created_by = created_by
        self.key = key
        self.name = name
        self.languages = languages
        self.distribution_channels = distribution_channels
        self.supply_channels = supply_channels
        self.product_selections = product_selections
        self.custom = custom
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
        )

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "Store":
        from ._schemas.store import StoreSchema

        return StoreSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.store import StoreSchema

        return StoreSchema().dump(self)


class StoreDraft(_BaseType):
    #: User-specific unique identifier for the store.
    #: The `key` is mandatory and immutable.
    #: It is used to reference the store.
    key: str
    #: The name of the store
    name: typing.Optional["LocalizedString"]
    languages: typing.Optional[typing.List["str"]]
    #: Set of ResourceIdentifiers to a Channel with `ProductDistribution` role
    distribution_channels: typing.Optional[typing.List["ChannelResourceIdentifier"]]
    #: Set of ResourceIdentifiers of Channels with `InventorySupply` role
    supply_channels: typing.Optional[typing.List["ChannelResourceIdentifier"]]
    #: Set of ResourceIdentifiers of Product Selections along with settings.
    #: If `productSelections` is empty all products in the project are available in this Store.
    #: If `productSelections` is not empty but there exists no `active` Product Selection then no Product is available in this Store.
    product_selections: typing.Optional[typing.List["ProductSelectionSettingDraft"]]
    custom: typing.Optional["CustomFieldsDraft"]

    def __init__(
        self,
        *,
        key: str,
        name: typing.Optional["LocalizedString"] = None,
        languages: typing.Optional[typing.List["str"]] = None,
        distribution_channels: typing.Optional[
            typing.List["ChannelResourceIdentifier"]
        ] = None,
        supply_channels: typing.Optional[
            typing.List["ChannelResourceIdentifier"]
        ] = None,
        product_selections: typing.Optional[
            typing.List["ProductSelectionSettingDraft"]
        ] = None,
        custom: typing.Optional["CustomFieldsDraft"] = None
    ):
        self.key = key
        self.name = name
        self.languages = languages
        self.distribution_channels = distribution_channels
        self.supply_channels = supply_channels
        self.product_selections = product_selections
        self.custom = custom
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "StoreDraft":
        from ._schemas.store import StoreDraftSchema

        return StoreDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.store import StoreDraftSchema

        return StoreDraftSchema().dump(self)


class StoreKeyReference(KeyReference):
    def __init__(self, *, key: str):

        super().__init__(key=key, type_id=ReferenceTypeId.STORE)

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "StoreKeyReference":
        from ._schemas.store import StoreKeyReferenceSchema

        return StoreKeyReferenceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.store import StoreKeyReferenceSchema

        return StoreKeyReferenceSchema().dump(self)


class StorePagedQueryResponse(_BaseType):
    limit: int
    count: int
    total: typing.Optional[int]
    offset: int
    results: typing.List["Store"]

    def __init__(
        self,
        *,
        limit: int,
        count: int,
        total: typing.Optional[int] = None,
        offset: int,
        results: typing.List["Store"]
    ):
        self.limit = limit
        self.count = count
        self.total = total
        self.offset = offset
        self.results = results
        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StorePagedQueryResponse":
        from ._schemas.store import StorePagedQueryResponseSchema

        return StorePagedQueryResponseSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.store import StorePagedQueryResponseSchema

        return StorePagedQueryResponseSchema().dump(self)


class StoreReference(Reference):
    obj: typing.Optional["Store"]

    def __init__(self, *, id: str, obj: typing.Optional["Store"] = None):
        self.obj = obj
        super().__init__(id=id, type_id=ReferenceTypeId.STORE)

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "StoreReference":
        from ._schemas.store import StoreReferenceSchema

        return StoreReferenceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.store import StoreReferenceSchema

        return StoreReferenceSchema().dump(self)


class StoreResourceIdentifier(ResourceIdentifier):
    def __init__(
        self, *, id: typing.Optional[str] = None, key: typing.Optional[str] = None
    ):

        super().__init__(id=id, key=key, type_id=ReferenceTypeId.STORE)

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StoreResourceIdentifier":
        from ._schemas.store import StoreResourceIdentifierSchema

        return StoreResourceIdentifierSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.store import StoreResourceIdentifierSchema

        return StoreResourceIdentifierSchema().dump(self)


class StoreUpdate(_BaseType):
    version: int
    actions: typing.List["StoreUpdateAction"]

    def __init__(self, *, version: int, actions: typing.List["StoreUpdateAction"]):
        self.version = version
        self.actions = actions
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "StoreUpdate":
        from ._schemas.store import StoreUpdateSchema

        return StoreUpdateSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.store import StoreUpdateSchema

        return StoreUpdateSchema().dump(self)


class StoreUpdateAction(_BaseType):
    action: str

    def __init__(self, *, action: str):
        self.action = action
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "StoreUpdateAction":
        if data["action"] == "addDistributionChannel":
            from ._schemas.store import StoreAddDistributionChannelActionSchema

            return StoreAddDistributionChannelActionSchema().load(data)
        if data["action"] == "addProductSelection":
            from ._schemas.store import StoreAddProductSelectionActionSchema

            return StoreAddProductSelectionActionSchema().load(data)
        if data["action"] == "addSupplyChannel":
            from ._schemas.store import StoreAddSupplyChannelActionSchema

            return StoreAddSupplyChannelActionSchema().load(data)
        if data["action"] == "changeProductSelectionActive":
            from ._schemas.store import StoreChangeProductSelectionActionSchema

            return StoreChangeProductSelectionActionSchema().load(data)
        if data["action"] == "removeDistributionChannel":
            from ._schemas.store import StoreRemoveDistributionChannelActionSchema

            return StoreRemoveDistributionChannelActionSchema().load(data)
        if data["action"] == "removeProductSelection":
            from ._schemas.store import StoreRemoveProductSelectionActionSchema

            return StoreRemoveProductSelectionActionSchema().load(data)
        if data["action"] == "removeSupplyChannel":
            from ._schemas.store import StoreRemoveSupplyChannelActionSchema

            return StoreRemoveSupplyChannelActionSchema().load(data)
        if data["action"] == "setCustomField":
            from ._schemas.store import StoreSetCustomFieldActionSchema

            return StoreSetCustomFieldActionSchema().load(data)
        if data["action"] == "setCustomType":
            from ._schemas.store import StoreSetCustomTypeActionSchema

            return StoreSetCustomTypeActionSchema().load(data)
        if data["action"] == "setDistributionChannels":
            from ._schemas.store import StoreSetDistributionChannelsActionSchema

            return StoreSetDistributionChannelsActionSchema().load(data)
        if data["action"] == "setLanguages":
            from ._schemas.store import StoreSetLanguagesActionSchema

            return StoreSetLanguagesActionSchema().load(data)
        if data["action"] == "setName":
            from ._schemas.store import StoreSetNameActionSchema

            return StoreSetNameActionSchema().load(data)
        if data["action"] == "setProductSelections":
            from ._schemas.store import StoreSetProductSelectionsActionSchema

            return StoreSetProductSelectionsActionSchema().load(data)
        if data["action"] == "setSupplyChannels":
            from ._schemas.store import StoreSetSupplyChannelsActionSchema

            return StoreSetSupplyChannelsActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.store import StoreUpdateActionSchema

        return StoreUpdateActionSchema().dump(self)


class StoreAddDistributionChannelAction(StoreUpdateAction):
    distribution_channel: "ChannelResourceIdentifier"

    def __init__(self, *, distribution_channel: "ChannelResourceIdentifier"):
        self.distribution_channel = distribution_channel
        super().__init__(action="addDistributionChannel")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StoreAddDistributionChannelAction":
        from ._schemas.store import StoreAddDistributionChannelActionSchema

        return StoreAddDistributionChannelActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.store import StoreAddDistributionChannelActionSchema

        return StoreAddDistributionChannelActionSchema().dump(self)


class StoreAddProductSelectionAction(StoreUpdateAction):
    #: A Product Selection to be added to the current Product Selections of this Store.
    product_selection: "ProductSelectionSettingDraft"

    def __init__(self, *, product_selection: "ProductSelectionSettingDraft"):
        self.product_selection = product_selection
        super().__init__(action="addProductSelection")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StoreAddProductSelectionAction":
        from ._schemas.store import StoreAddProductSelectionActionSchema

        return StoreAddProductSelectionActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.store import StoreAddProductSelectionActionSchema

        return StoreAddProductSelectionActionSchema().dump(self)


class StoreAddSupplyChannelAction(StoreUpdateAction):
    supply_channel: typing.Optional["ChannelResourceIdentifier"]

    def __init__(
        self, *, supply_channel: typing.Optional["ChannelResourceIdentifier"] = None
    ):
        self.supply_channel = supply_channel
        super().__init__(action="addSupplyChannel")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StoreAddSupplyChannelAction":
        from ._schemas.store import StoreAddSupplyChannelActionSchema

        return StoreAddSupplyChannelActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.store import StoreAddSupplyChannelActionSchema

        return StoreAddSupplyChannelActionSchema().dump(self)


class StoreChangeProductSelectionAction(StoreUpdateAction):
    #: A current Product Selection of this Store that is to be activated or deactivated.
    product_selection: "ResourceIdentifier"
    #: If `true` all Products assigned to the Product Selection become part of the Store's assortment.
    active: typing.Optional[bool]

    def __init__(
        self,
        *,
        product_selection: "ResourceIdentifier",
        active: typing.Optional[bool] = None
    ):
        self.product_selection = product_selection
        self.active = active
        super().__init__(action="changeProductSelectionActive")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StoreChangeProductSelectionAction":
        from ._schemas.store import StoreChangeProductSelectionActionSchema

        return StoreChangeProductSelectionActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.store import StoreChangeProductSelectionActionSchema

        return StoreChangeProductSelectionActionSchema().dump(self)


class StoreRemoveDistributionChannelAction(StoreUpdateAction):
    distribution_channel: "ChannelResourceIdentifier"

    def __init__(self, *, distribution_channel: "ChannelResourceIdentifier"):
        self.distribution_channel = distribution_channel
        super().__init__(action="removeDistributionChannel")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StoreRemoveDistributionChannelAction":
        from ._schemas.store import StoreRemoveDistributionChannelActionSchema

        return StoreRemoveDistributionChannelActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.store import StoreRemoveDistributionChannelActionSchema

        return StoreRemoveDistributionChannelActionSchema().dump(self)


class StoreRemoveProductSelectionAction(StoreUpdateAction):
    #: A Product Selection to be removed from the current Product Selections of this Store.
    product_selection: "ResourceIdentifier"

    def __init__(self, *, product_selection: "ResourceIdentifier"):
        self.product_selection = product_selection
        super().__init__(action="removeProductSelection")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StoreRemoveProductSelectionAction":
        from ._schemas.store import StoreRemoveProductSelectionActionSchema

        return StoreRemoveProductSelectionActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.store import StoreRemoveProductSelectionActionSchema

        return StoreRemoveProductSelectionActionSchema().dump(self)


class StoreRemoveSupplyChannelAction(StoreUpdateAction):
    supply_channel: typing.Optional["ChannelResourceIdentifier"]

    def __init__(
        self, *, supply_channel: typing.Optional["ChannelResourceIdentifier"] = None
    ):
        self.supply_channel = supply_channel
        super().__init__(action="removeSupplyChannel")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StoreRemoveSupplyChannelAction":
        from ._schemas.store import StoreRemoveSupplyChannelActionSchema

        return StoreRemoveSupplyChannelActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.store import StoreRemoveSupplyChannelActionSchema

        return StoreRemoveSupplyChannelActionSchema().dump(self)


class StoreSetCustomFieldAction(StoreUpdateAction):
    #: Name of the [Custom Field](/../api/projects/custom-fields).
    name: str
    #: If `value` is absent or `null`, this field will be removed if it exists.
    #: Trying to remove a field that does not exist will fail with an [InvalidOperation](/../api/errors#general-400-invalid-operation) error.
    #: If `value` is provided, it is set for the field defined by `name`.
    value: typing.Optional[typing.Any]

    def __init__(self, *, name: str, value: typing.Optional[typing.Any] = None):
        self.name = name
        self.value = value
        super().__init__(action="setCustomField")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StoreSetCustomFieldAction":
        from ._schemas.store import StoreSetCustomFieldActionSchema

        return StoreSetCustomFieldActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.store import StoreSetCustomFieldActionSchema

        return StoreSetCustomFieldActionSchema().dump(self)


class StoreSetCustomTypeAction(StoreUpdateAction):
    #: Defines the [Type](ctp:api:type:Type) that extends the Store with [Custom Fields](/../api/projects/custom-fields).
    #: If absent, any existing Type and Custom Fields are removed from the Store.
    type: typing.Optional["TypeResourceIdentifier"]
    #: Sets the [Custom Fields](/../api/projects/custom-fields) fields for the Store.
    fields: typing.Optional["FieldContainer"]

    def __init__(
        self,
        *,
        type: typing.Optional["TypeResourceIdentifier"] = None,
        fields: typing.Optional["FieldContainer"] = None
    ):
        self.type = type
        self.fields = fields
        super().__init__(action="setCustomType")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StoreSetCustomTypeAction":
        from ._schemas.store import StoreSetCustomTypeActionSchema

        return StoreSetCustomTypeActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.store import StoreSetCustomTypeActionSchema

        return StoreSetCustomTypeActionSchema().dump(self)


class StoreSetDistributionChannelsAction(StoreUpdateAction):
    distribution_channels: typing.Optional[typing.List["ChannelResourceIdentifier"]]

    def __init__(
        self,
        *,
        distribution_channels: typing.Optional[
            typing.List["ChannelResourceIdentifier"]
        ] = None
    ):
        self.distribution_channels = distribution_channels
        super().__init__(action="setDistributionChannels")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StoreSetDistributionChannelsAction":
        from ._schemas.store import StoreSetDistributionChannelsActionSchema

        return StoreSetDistributionChannelsActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.store import StoreSetDistributionChannelsActionSchema

        return StoreSetDistributionChannelsActionSchema().dump(self)


class StoreSetLanguagesAction(StoreUpdateAction):
    languages: typing.Optional[typing.List["str"]]

    def __init__(self, *, languages: typing.Optional[typing.List["str"]] = None):
        self.languages = languages
        super().__init__(action="setLanguages")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StoreSetLanguagesAction":
        from ._schemas.store import StoreSetLanguagesActionSchema

        return StoreSetLanguagesActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.store import StoreSetLanguagesActionSchema

        return StoreSetLanguagesActionSchema().dump(self)


class StoreSetNameAction(StoreUpdateAction):
    #: The updated name of the store
    name: typing.Optional["LocalizedString"]

    def __init__(self, *, name: typing.Optional["LocalizedString"] = None):
        self.name = name
        super().__init__(action="setName")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "StoreSetNameAction":
        from ._schemas.store import StoreSetNameActionSchema

        return StoreSetNameActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.store import StoreSetNameActionSchema

        return StoreSetNameActionSchema().dump(self)


class StoreSetProductSelectionsAction(StoreUpdateAction):
    #: The total of Product Selections to be set for this Store.
    product_selections: typing.List["ProductSelectionSettingDraft"]

    def __init__(
        self, *, product_selections: typing.List["ProductSelectionSettingDraft"]
    ):
        self.product_selections = product_selections
        super().__init__(action="setProductSelections")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StoreSetProductSelectionsAction":
        from ._schemas.store import StoreSetProductSelectionsActionSchema

        return StoreSetProductSelectionsActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.store import StoreSetProductSelectionsActionSchema

        return StoreSetProductSelectionsActionSchema().dump(self)


class StoreSetSupplyChannelsAction(StoreUpdateAction):
    supply_channels: typing.Optional[typing.List["ChannelResourceIdentifier"]]

    def __init__(
        self,
        *,
        supply_channels: typing.Optional[
            typing.List["ChannelResourceIdentifier"]
        ] = None
    ):
        self.supply_channels = supply_channels
        super().__init__(action="setSupplyChannels")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StoreSetSupplyChannelsAction":
        from ._schemas.store import StoreSetSupplyChannelsActionSchema

        return StoreSetSupplyChannelsActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.store import StoreSetSupplyChannelsActionSchema

        return StoreSetSupplyChannelsActionSchema().dump(self)
