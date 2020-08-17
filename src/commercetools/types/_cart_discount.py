# DO NOT EDIT! This file is automatically generated
import datetime
import enum
import typing

from commercetools.types._abstract import _BaseType
from commercetools.types._common import (
    BaseResource,
    Reference,
    ReferenceTypeId,
    ResourceIdentifier,
)

if typing.TYPE_CHECKING:
    from ._channel import ChannelReference
    from ._common import CreatedBy, LastModifiedBy, LocalizedString, Money, TypedMoney
    from ._product import ProductReference
    from ._type import CustomFields, TypeResourceIdentifier
__all__ = [
    "CartDiscount",
    "CartDiscountChangeCartPredicateAction",
    "CartDiscountChangeIsActiveAction",
    "CartDiscountChangeNameAction",
    "CartDiscountChangeRequiresDiscountCodeAction",
    "CartDiscountChangeSortOrderAction",
    "CartDiscountChangeStackingModeAction",
    "CartDiscountChangeTargetAction",
    "CartDiscountChangeValueAction",
    "CartDiscountCustomLineItemsTarget",
    "CartDiscountDraft",
    "CartDiscountLineItemsTarget",
    "CartDiscountPagedQueryResponse",
    "CartDiscountReference",
    "CartDiscountResourceIdentifier",
    "CartDiscountSetCustomFieldAction",
    "CartDiscountSetCustomTypeAction",
    "CartDiscountSetDescriptionAction",
    "CartDiscountSetKeyAction",
    "CartDiscountSetValidFromAction",
    "CartDiscountSetValidFromAndUntilAction",
    "CartDiscountSetValidUntilAction",
    "CartDiscountShippingCostTarget",
    "CartDiscountTarget",
    "CartDiscountUpdate",
    "CartDiscountUpdateAction",
    "CartDiscountValue",
    "CartDiscountValueAbsolute",
    "CartDiscountValueAbsoluteDraft",
    "CartDiscountValueDraft",
    "CartDiscountValueGiftLineItem",
    "CartDiscountValueGiftLineItemDraft",
    "CartDiscountValueRelative",
    "CartDiscountValueRelativeDraft",
    "MultiBuyCustomLineItemsTarget",
    "MultiBuyLineItemsTarget",
    "SelectionMode",
    "StackingMode",
]


class CartDiscount(BaseResource):
    #: :class:`str`
    id: str
    #: :class:`int`
    version: int
    #: :class:`datetime.datetime` `(Named` ``createdAt`` `in Commercetools)`
    created_at: datetime.datetime
    #: :class:`datetime.datetime` `(Named` ``lastModifiedAt`` `in Commercetools)`
    last_modified_at: datetime.datetime
    #: Optional :class:`commercetools.types.LastModifiedBy` `(Named` ``lastModifiedBy`` `in Commercetools)`
    last_modified_by: typing.Optional["LastModifiedBy"]
    #: Optional :class:`commercetools.types.CreatedBy` `(Named` ``createdBy`` `in Commercetools)`
    created_by: typing.Optional["CreatedBy"]
    #: :class:`commercetools.types.LocalizedString`
    name: "LocalizedString"
    #: Optional :class:`str`
    key: typing.Optional[str]
    #: Optional :class:`commercetools.types.LocalizedString`
    description: typing.Optional["LocalizedString"]
    #: :class:`commercetools.types.CartDiscountValue`
    value: "CartDiscountValue"
    #: :class:`str` `(Named` ``cartPredicate`` `in Commercetools)`
    cart_predicate: str
    #: Optional :class:`commercetools.types.CartDiscountTarget`
    target: typing.Optional["CartDiscountTarget"]
    #: :class:`str` `(Named` ``sortOrder`` `in Commercetools)`
    sort_order: str
    #: :class:`bool` `(Named` ``isActive`` `in Commercetools)`
    is_active: bool
    #: Optional :class:`datetime.datetime` `(Named` ``validFrom`` `in Commercetools)`
    valid_from: typing.Optional[datetime.datetime]
    #: Optional :class:`datetime.datetime` `(Named` ``validUntil`` `in Commercetools)`
    valid_until: typing.Optional[datetime.datetime]
    #: :class:`bool` `(Named` ``requiresDiscountCode`` `in Commercetools)`
    requires_discount_code: bool
    #: List of :class:`commercetools.types.Reference`
    references: typing.List["Reference"]
    #: :class:`commercetools.types.StackingMode` `(Named` ``stackingMode`` `in Commercetools)`
    stacking_mode: "StackingMode"
    #: Optional :class:`commercetools.types.CustomFields`
    custom: typing.Optional["CustomFields"]

    def __init__(
        self,
        *,
        id: str,
        version: int,
        created_at: datetime.datetime,
        last_modified_at: datetime.datetime,
        name: "LocalizedString",
        value: "CartDiscountValue",
        cart_predicate: str,
        sort_order: str,
        is_active: bool,
        requires_discount_code: bool,
        references: typing.List["Reference"],
        stacking_mode: "StackingMode",
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        key: typing.Optional[str] = None,
        description: typing.Optional["LocalizedString"] = None,
        target: typing.Optional["CartDiscountTarget"] = None,
        valid_from: typing.Optional[datetime.datetime] = None,
        valid_until: typing.Optional[datetime.datetime] = None,
        custom: typing.Optional["CustomFields"] = None
    ) -> None:
        self.id = id
        self.version = version
        self.created_at = created_at
        self.last_modified_at = last_modified_at
        self.last_modified_by = last_modified_by
        self.created_by = created_by
        self.name = name
        self.key = key
        self.description = description
        self.value = value
        self.cart_predicate = cart_predicate
        self.target = target
        self.sort_order = sort_order
        self.is_active = is_active
        self.valid_from = valid_from
        self.valid_until = valid_until
        self.requires_discount_code = requires_discount_code
        self.references = references
        self.stacking_mode = stacking_mode
        self.custom = custom
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
        )

    def __repr__(self) -> str:
        return (
            "CartDiscount(id=%r, version=%r, created_at=%r, last_modified_at=%r, last_modified_by=%r, created_by=%r, name=%r, key=%r, description=%r, value=%r, cart_predicate=%r, target=%r, sort_order=%r, is_active=%r, valid_from=%r, valid_until=%r, requires_discount_code=%r, references=%r, stacking_mode=%r, custom=%r)"
            % (
                self.id,
                self.version,
                self.created_at,
                self.last_modified_at,
                self.last_modified_by,
                self.created_by,
                self.name,
                self.key,
                self.description,
                self.value,
                self.cart_predicate,
                self.target,
                self.sort_order,
                self.is_active,
                self.valid_from,
                self.valid_until,
                self.requires_discount_code,
                self.references,
                self.stacking_mode,
                self.custom,
            )
        )


class CartDiscountDraft(_BaseType):
    #: :class:`commercetools.types.LocalizedString`
    name: "LocalizedString"
    #: Optional :class:`str`
    key: typing.Optional[str]
    #: Optional :class:`commercetools.types.LocalizedString`
    description: typing.Optional["LocalizedString"]
    #: :class:`commercetools.types.CartDiscountValueDraft`
    value: "CartDiscountValueDraft"
    #: :class:`str` `(Named` ``cartPredicate`` `in Commercetools)`
    cart_predicate: str
    #: Optional :class:`commercetools.types.CartDiscountTarget`
    target: typing.Optional["CartDiscountTarget"]
    #: :class:`str` `(Named` ``sortOrder`` `in Commercetools)`
    sort_order: str
    #: Optional :class:`bool` `(Named` ``isActive`` `in Commercetools)`
    is_active: typing.Optional[bool]
    #: Optional :class:`datetime.datetime` `(Named` ``validFrom`` `in Commercetools)`
    valid_from: typing.Optional[datetime.datetime]
    #: Optional :class:`datetime.datetime` `(Named` ``validUntil`` `in Commercetools)`
    valid_until: typing.Optional[datetime.datetime]
    #: :class:`bool` `(Named` ``requiresDiscountCode`` `in Commercetools)`
    requires_discount_code: bool
    #: Optional :class:`commercetools.types.StackingMode` `(Named` ``stackingMode`` `in Commercetools)`
    stacking_mode: typing.Optional["StackingMode"]
    #: Optional :class:`commercetools.types.CustomFields`
    custom: typing.Optional["CustomFields"]

    def __init__(
        self,
        *,
        name: "LocalizedString",
        value: "CartDiscountValueDraft",
        cart_predicate: str,
        sort_order: str,
        requires_discount_code: bool,
        key: typing.Optional[str] = None,
        description: typing.Optional["LocalizedString"] = None,
        target: typing.Optional["CartDiscountTarget"] = None,
        is_active: typing.Optional[bool] = None,
        valid_from: typing.Optional[datetime.datetime] = None,
        valid_until: typing.Optional[datetime.datetime] = None,
        stacking_mode: typing.Optional["StackingMode"] = None,
        custom: typing.Optional["CustomFields"] = None
    ) -> None:
        self.name = name
        self.key = key
        self.description = description
        self.value = value
        self.cart_predicate = cart_predicate
        self.target = target
        self.sort_order = sort_order
        self.is_active = is_active
        self.valid_from = valid_from
        self.valid_until = valid_until
        self.requires_discount_code = requires_discount_code
        self.stacking_mode = stacking_mode
        self.custom = custom
        super().__init__()

    def __repr__(self) -> str:
        return (
            "CartDiscountDraft(name=%r, key=%r, description=%r, value=%r, cart_predicate=%r, target=%r, sort_order=%r, is_active=%r, valid_from=%r, valid_until=%r, requires_discount_code=%r, stacking_mode=%r, custom=%r)"
            % (
                self.name,
                self.key,
                self.description,
                self.value,
                self.cart_predicate,
                self.target,
                self.sort_order,
                self.is_active,
                self.valid_from,
                self.valid_until,
                self.requires_discount_code,
                self.stacking_mode,
                self.custom,
            )
        )


class CartDiscountPagedQueryResponse(_BaseType):
    #: :class:`int`
    limit: int
    #: :class:`int`
    count: int
    #: Optional :class:`int`
    total: typing.Optional[int]
    #: :class:`int`
    offset: int
    #: List of :class:`commercetools.types.CartDiscount`
    results: typing.Sequence["CartDiscount"]

    def __init__(
        self,
        *,
        limit: int,
        count: int,
        offset: int,
        results: typing.Sequence["CartDiscount"],
        total: typing.Optional[int] = None
    ) -> None:
        self.limit = limit
        self.count = count
        self.total = total
        self.offset = offset
        self.results = results
        super().__init__()

    def __repr__(self) -> str:
        return (
            "CartDiscountPagedQueryResponse(limit=%r, count=%r, total=%r, offset=%r, results=%r)"
            % (self.limit, self.count, self.total, self.offset, self.results)
        )


class CartDiscountReference(Reference):
    #: Optional :class:`commercetools.types.CartDiscount`
    obj: typing.Optional["CartDiscount"]

    def __init__(self, *, id: str, obj: typing.Optional["CartDiscount"] = None) -> None:
        self.obj = obj
        super().__init__(type_id=ReferenceTypeId.CART_DISCOUNT, id=id)

    def __repr__(self) -> str:
        return "CartDiscountReference(type_id=%r, id=%r, obj=%r)" % (
            self.type_id,
            self.id,
            self.obj,
        )


class CartDiscountResourceIdentifier(ResourceIdentifier):
    def __init__(
        self, *, id: typing.Optional[str] = None, key: typing.Optional[str] = None
    ) -> None:
        super().__init__(type_id=ReferenceTypeId.CART_DISCOUNT, id=id, key=key)

    def __repr__(self) -> str:
        return "CartDiscountResourceIdentifier(type_id=%r, id=%r, key=%r)" % (
            self.type_id,
            self.id,
            self.key,
        )


class CartDiscountTarget(_BaseType):
    #: :class:`str`
    type: str

    def __init__(self, *, type: str) -> None:
        self.type = type
        super().__init__()

    def __repr__(self) -> str:
        return "CartDiscountTarget(type=%r)" % (self.type,)


class CartDiscountUpdate(_BaseType):
    #: :class:`int`
    version: int
    #: :class:`list`
    actions: list

    def __init__(self, *, version: int, actions: list) -> None:
        self.version = version
        self.actions = actions
        super().__init__()

    def __repr__(self) -> str:
        return "CartDiscountUpdate(version=%r, actions=%r)" % (
            self.version,
            self.actions,
        )


class CartDiscountUpdateAction(_BaseType):
    #: :class:`str`
    action: str

    def __init__(self, *, action: str) -> None:
        self.action = action
        super().__init__()

    def __repr__(self) -> str:
        return "CartDiscountUpdateAction(action=%r)" % (self.action,)


class CartDiscountValue(_BaseType):
    #: :class:`str`
    type: str

    def __init__(self, *, type: str) -> None:
        self.type = type
        super().__init__()

    def __repr__(self) -> str:
        return "CartDiscountValue(type=%r)" % (self.type,)


class CartDiscountValueDraft(_BaseType):
    #: :class:`str`
    type: str

    def __init__(self, *, type: str) -> None:
        self.type = type
        super().__init__()

    def __repr__(self) -> str:
        return "CartDiscountValueDraft(type=%r)" % (self.type,)


class SelectionMode(enum.Enum):
    CHEAPEST = "Cheapest"
    MOST_EXPENSIVE = "MostExpensive"


class StackingMode(enum.Enum):
    STACKING = "Stacking"
    STOP_AFTER_THIS_DISCOUNT = "StopAfterThisDiscount"


class CartDiscountChangeCartPredicateAction(CartDiscountUpdateAction):
    #: :class:`str` `(Named` ``cartPredicate`` `in Commercetools)`
    cart_predicate: str

    def __init__(self, *, cart_predicate: str) -> None:
        self.cart_predicate = cart_predicate
        super().__init__(action="changeCartPredicate")

    def __repr__(self) -> str:
        return "CartDiscountChangeCartPredicateAction(action=%r, cart_predicate=%r)" % (
            self.action,
            self.cart_predicate,
        )


class CartDiscountChangeIsActiveAction(CartDiscountUpdateAction):
    #: :class:`bool` `(Named` ``isActive`` `in Commercetools)`
    is_active: bool

    def __init__(self, *, is_active: bool) -> None:
        self.is_active = is_active
        super().__init__(action="changeIsActive")

    def __repr__(self) -> str:
        return "CartDiscountChangeIsActiveAction(action=%r, is_active=%r)" % (
            self.action,
            self.is_active,
        )


class CartDiscountChangeNameAction(CartDiscountUpdateAction):
    #: :class:`commercetools.types.LocalizedString`
    name: "LocalizedString"

    def __init__(self, *, name: "LocalizedString") -> None:
        self.name = name
        super().__init__(action="changeName")

    def __repr__(self) -> str:
        return "CartDiscountChangeNameAction(action=%r, name=%r)" % (
            self.action,
            self.name,
        )


class CartDiscountChangeRequiresDiscountCodeAction(CartDiscountUpdateAction):
    #: :class:`bool` `(Named` ``requiresDiscountCode`` `in Commercetools)`
    requires_discount_code: bool

    def __init__(self, *, requires_discount_code: bool) -> None:
        self.requires_discount_code = requires_discount_code
        super().__init__(action="changeRequiresDiscountCode")

    def __repr__(self) -> str:
        return (
            "CartDiscountChangeRequiresDiscountCodeAction(action=%r, requires_discount_code=%r)"
            % (self.action, self.requires_discount_code)
        )


class CartDiscountChangeSortOrderAction(CartDiscountUpdateAction):
    #: :class:`str` `(Named` ``sortOrder`` `in Commercetools)`
    sort_order: str

    def __init__(self, *, sort_order: str) -> None:
        self.sort_order = sort_order
        super().__init__(action="changeSortOrder")

    def __repr__(self) -> str:
        return "CartDiscountChangeSortOrderAction(action=%r, sort_order=%r)" % (
            self.action,
            self.sort_order,
        )


class CartDiscountChangeStackingModeAction(CartDiscountUpdateAction):
    #: :class:`commercetools.types.StackingMode` `(Named` ``stackingMode`` `in Commercetools)`
    stacking_mode: "StackingMode"

    def __init__(self, *, stacking_mode: "StackingMode") -> None:
        self.stacking_mode = stacking_mode
        super().__init__(action="changeStackingMode")

    def __repr__(self) -> str:
        return "CartDiscountChangeStackingModeAction(action=%r, stacking_mode=%r)" % (
            self.action,
            self.stacking_mode,
        )


class CartDiscountChangeTargetAction(CartDiscountUpdateAction):
    #: :class:`commercetools.types.CartDiscountTarget`
    target: "CartDiscountTarget"

    def __init__(self, *, target: "CartDiscountTarget") -> None:
        self.target = target
        super().__init__(action="changeTarget")

    def __repr__(self) -> str:
        return "CartDiscountChangeTargetAction(action=%r, target=%r)" % (
            self.action,
            self.target,
        )


class CartDiscountChangeValueAction(CartDiscountUpdateAction):
    #: :class:`commercetools.types.CartDiscountValueDraft`
    value: "CartDiscountValueDraft"

    def __init__(self, *, value: "CartDiscountValueDraft") -> None:
        self.value = value
        super().__init__(action="changeValue")

    def __repr__(self) -> str:
        return "CartDiscountChangeValueAction(action=%r, value=%r)" % (
            self.action,
            self.value,
        )


class CartDiscountCustomLineItemsTarget(CartDiscountTarget):
    #: :class:`str`
    predicate: str

    def __init__(self, *, predicate: str) -> None:
        self.predicate = predicate
        super().__init__(type="customLineItems")

    def __repr__(self) -> str:
        return "CartDiscountCustomLineItemsTarget(type=%r, predicate=%r)" % (
            self.type,
            self.predicate,
        )


class CartDiscountLineItemsTarget(CartDiscountTarget):
    #: :class:`str`
    predicate: str

    def __init__(self, *, predicate: str) -> None:
        self.predicate = predicate
        super().__init__(type="lineItems")

    def __repr__(self) -> str:
        return "CartDiscountLineItemsTarget(type=%r, predicate=%r)" % (
            self.type,
            self.predicate,
        )


class CartDiscountSetCustomFieldAction(CartDiscountUpdateAction):
    #: :class:`str`
    name: str
    #: Optional :class:`typing.Any`
    value: typing.Optional[typing.Any]

    def __init__(self, *, name: str, value: typing.Optional[typing.Any] = None) -> None:
        self.name = name
        self.value = value
        super().__init__(action="setCustomField")

    def __repr__(self) -> str:
        return "CartDiscountSetCustomFieldAction(action=%r, name=%r, value=%r)" % (
            self.action,
            self.name,
            self.value,
        )


class CartDiscountSetCustomTypeAction(CartDiscountUpdateAction):
    #: Optional :class:`commercetools.types.TypeResourceIdentifier`
    type: typing.Optional["TypeResourceIdentifier"]
    #: Optional :class:`object`
    fields: typing.Optional[object]

    def __init__(
        self,
        *,
        type: typing.Optional["TypeResourceIdentifier"] = None,
        fields: typing.Optional[object] = None
    ) -> None:
        self.type = type
        self.fields = fields
        super().__init__(action="setCustomType")

    def __repr__(self) -> str:
        return "CartDiscountSetCustomTypeAction(action=%r, type=%r, fields=%r)" % (
            self.action,
            self.type,
            self.fields,
        )


class CartDiscountSetDescriptionAction(CartDiscountUpdateAction):
    #: Optional :class:`commercetools.types.LocalizedString`
    description: typing.Optional["LocalizedString"]

    def __init__(
        self, *, description: typing.Optional["LocalizedString"] = None
    ) -> None:
        self.description = description
        super().__init__(action="setDescription")

    def __repr__(self) -> str:
        return "CartDiscountSetDescriptionAction(action=%r, description=%r)" % (
            self.action,
            self.description,
        )


class CartDiscountSetKeyAction(CartDiscountUpdateAction):
    #: Optional :class:`str`
    key: typing.Optional[str]

    def __init__(self, *, key: typing.Optional[str] = None) -> None:
        self.key = key
        super().__init__(action="setKey")

    def __repr__(self) -> str:
        return "CartDiscountSetKeyAction(action=%r, key=%r)" % (self.action, self.key)


class CartDiscountSetValidFromAction(CartDiscountUpdateAction):
    #: Optional :class:`datetime.datetime` `(Named` ``validFrom`` `in Commercetools)`
    valid_from: typing.Optional[datetime.datetime]

    def __init__(
        self, *, valid_from: typing.Optional[datetime.datetime] = None
    ) -> None:
        self.valid_from = valid_from
        super().__init__(action="setValidFrom")

    def __repr__(self) -> str:
        return "CartDiscountSetValidFromAction(action=%r, valid_from=%r)" % (
            self.action,
            self.valid_from,
        )


class CartDiscountSetValidFromAndUntilAction(CartDiscountUpdateAction):
    #: Optional :class:`datetime.datetime` `(Named` ``validFrom`` `in Commercetools)`
    valid_from: typing.Optional[datetime.datetime]
    #: Optional :class:`datetime.datetime` `(Named` ``validUntil`` `in Commercetools)`
    valid_until: typing.Optional[datetime.datetime]

    def __init__(
        self,
        *,
        valid_from: typing.Optional[datetime.datetime] = None,
        valid_until: typing.Optional[datetime.datetime] = None
    ) -> None:
        self.valid_from = valid_from
        self.valid_until = valid_until
        super().__init__(action="setValidFromAndUntil")

    def __repr__(self) -> str:
        return (
            "CartDiscountSetValidFromAndUntilAction(action=%r, valid_from=%r, valid_until=%r)"
            % (self.action, self.valid_from, self.valid_until)
        )


class CartDiscountSetValidUntilAction(CartDiscountUpdateAction):
    #: Optional :class:`datetime.datetime` `(Named` ``validUntil`` `in Commercetools)`
    valid_until: typing.Optional[datetime.datetime]

    def __init__(
        self, *, valid_until: typing.Optional[datetime.datetime] = None
    ) -> None:
        self.valid_until = valid_until
        super().__init__(action="setValidUntil")

    def __repr__(self) -> str:
        return "CartDiscountSetValidUntilAction(action=%r, valid_until=%r)" % (
            self.action,
            self.valid_until,
        )


class CartDiscountShippingCostTarget(CartDiscountTarget):
    def __init__(self) -> None:
        super().__init__(type="shipping")

    def __repr__(self) -> str:
        return "CartDiscountShippingCostTarget(type=%r)" % (self.type,)


class CartDiscountValueAbsolute(CartDiscountValue):
    #: List of :class:`commercetools.types.TypedMoney`
    money: typing.List["TypedMoney"]

    def __init__(self, *, money: typing.List["TypedMoney"]) -> None:
        self.money = money
        super().__init__(type="absolute")

    def __repr__(self) -> str:
        return "CartDiscountValueAbsolute(type=%r, money=%r)" % (self.type, self.money)


class CartDiscountValueAbsoluteDraft(CartDiscountValueDraft):
    #: List of :class:`commercetools.types.Money`
    money: typing.List["Money"]

    def __init__(self, *, money: typing.List["Money"]) -> None:
        self.money = money
        super().__init__(type="absolute")

    def __repr__(self) -> str:
        return "CartDiscountValueAbsoluteDraft(type=%r, money=%r)" % (
            self.type,
            self.money,
        )


class CartDiscountValueGiftLineItem(CartDiscountValue):
    #: :class:`commercetools.types.ProductReference`
    product: "ProductReference"
    #: :class:`int` `(Named` ``variantId`` `in Commercetools)`
    variant_id: int
    #: Optional :class:`commercetools.types.ChannelReference` `(Named` ``supplyChannel`` `in Commercetools)`
    supply_channel: typing.Optional["ChannelReference"]
    #: Optional :class:`commercetools.types.ChannelReference` `(Named` ``distributionChannel`` `in Commercetools)`
    distribution_channel: typing.Optional["ChannelReference"]

    def __init__(
        self,
        *,
        product: "ProductReference",
        variant_id: int,
        supply_channel: typing.Optional["ChannelReference"] = None,
        distribution_channel: typing.Optional["ChannelReference"] = None
    ) -> None:
        self.product = product
        self.variant_id = variant_id
        self.supply_channel = supply_channel
        self.distribution_channel = distribution_channel
        super().__init__(type="giftLineItem")

    def __repr__(self) -> str:
        return (
            "CartDiscountValueGiftLineItem(type=%r, product=%r, variant_id=%r, supply_channel=%r, distribution_channel=%r)"
            % (
                self.type,
                self.product,
                self.variant_id,
                self.supply_channel,
                self.distribution_channel,
            )
        )


class CartDiscountValueGiftLineItemDraft(CartDiscountValueDraft):
    #: :class:`commercetools.types.ProductReference`
    product: "ProductReference"
    #: :class:`int` `(Named` ``variantId`` `in Commercetools)`
    variant_id: int
    #: Optional :class:`commercetools.types.ChannelReference` `(Named` ``supplyChannel`` `in Commercetools)`
    supply_channel: typing.Optional["ChannelReference"]
    #: Optional :class:`commercetools.types.ChannelReference` `(Named` ``distributionChannel`` `in Commercetools)`
    distribution_channel: typing.Optional["ChannelReference"]

    def __init__(
        self,
        *,
        product: "ProductReference",
        variant_id: int,
        supply_channel: typing.Optional["ChannelReference"] = None,
        distribution_channel: typing.Optional["ChannelReference"] = None
    ) -> None:
        self.product = product
        self.variant_id = variant_id
        self.supply_channel = supply_channel
        self.distribution_channel = distribution_channel
        super().__init__(type="giftLineItem")

    def __repr__(self) -> str:
        return (
            "CartDiscountValueGiftLineItemDraft(type=%r, product=%r, variant_id=%r, supply_channel=%r, distribution_channel=%r)"
            % (
                self.type,
                self.product,
                self.variant_id,
                self.supply_channel,
                self.distribution_channel,
            )
        )


class CartDiscountValueRelative(CartDiscountValue):
    #: :class:`int`
    permyriad: int

    def __init__(self, *, permyriad: int) -> None:
        self.permyriad = permyriad
        super().__init__(type="relative")

    def __repr__(self) -> str:
        return "CartDiscountValueRelative(type=%r, permyriad=%r)" % (
            self.type,
            self.permyriad,
        )


class CartDiscountValueRelativeDraft(CartDiscountValueDraft):
    #: :class:`int`
    permyriad: int

    def __init__(self, *, permyriad: int) -> None:
        self.permyriad = permyriad
        super().__init__(type="relative")

    def __repr__(self) -> str:
        return "CartDiscountValueRelativeDraft(type=%r, permyriad=%r)" % (
            self.type,
            self.permyriad,
        )


class MultiBuyCustomLineItemsTarget(CartDiscountTarget):
    #: :class:`str`
    predicate: str
    #: :class:`int` `(Named` ``triggerQuantity`` `in Commercetools)`
    trigger_quantity: int
    #: :class:`int` `(Named` ``discountedQuantity`` `in Commercetools)`
    discounted_quantity: int
    #: Optional :class:`int` `(Named` ``maxOccurrence`` `in Commercetools)`
    max_occurrence: typing.Optional[int]
    #: :class:`commercetools.types.SelectionMode` `(Named` ``selectionMode`` `in Commercetools)`
    selection_mode: "SelectionMode"

    def __init__(
        self,
        *,
        predicate: str,
        trigger_quantity: int,
        discounted_quantity: int,
        selection_mode: "SelectionMode",
        max_occurrence: typing.Optional[int] = None
    ) -> None:
        self.predicate = predicate
        self.trigger_quantity = trigger_quantity
        self.discounted_quantity = discounted_quantity
        self.max_occurrence = max_occurrence
        self.selection_mode = selection_mode
        super().__init__(type="multiBuyCustomLineItems")

    def __repr__(self) -> str:
        return (
            "MultiBuyCustomLineItemsTarget(type=%r, predicate=%r, trigger_quantity=%r, discounted_quantity=%r, max_occurrence=%r, selection_mode=%r)"
            % (
                self.type,
                self.predicate,
                self.trigger_quantity,
                self.discounted_quantity,
                self.max_occurrence,
                self.selection_mode,
            )
        )


class MultiBuyLineItemsTarget(CartDiscountTarget):
    #: :class:`str`
    predicate: str
    #: :class:`int` `(Named` ``triggerQuantity`` `in Commercetools)`
    trigger_quantity: int
    #: :class:`int` `(Named` ``discountedQuantity`` `in Commercetools)`
    discounted_quantity: int
    #: Optional :class:`int` `(Named` ``maxOccurrence`` `in Commercetools)`
    max_occurrence: typing.Optional[int]
    #: :class:`commercetools.types.SelectionMode` `(Named` ``selectionMode`` `in Commercetools)`
    selection_mode: "SelectionMode"

    def __init__(
        self,
        *,
        predicate: str,
        trigger_quantity: int,
        discounted_quantity: int,
        selection_mode: "SelectionMode",
        max_occurrence: typing.Optional[int] = None
    ) -> None:
        self.predicate = predicate
        self.trigger_quantity = trigger_quantity
        self.discounted_quantity = discounted_quantity
        self.max_occurrence = max_occurrence
        self.selection_mode = selection_mode
        super().__init__(type="multiBuyLineItems")

    def __repr__(self) -> str:
        return (
            "MultiBuyLineItemsTarget(type=%r, predicate=%r, trigger_quantity=%r, discounted_quantity=%r, max_occurrence=%r, selection_mode=%r)"
            % (
                self.type,
                self.predicate,
                self.trigger_quantity,
                self.discounted_quantity,
                self.max_occurrence,
                self.selection_mode,
            )
        )
