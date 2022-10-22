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
from .cart import InventoryMode, RoundingMode, TaxCalculationMode, TaxMode
from .common import BaseResource, Reference, ReferenceTypeId, ResourceIdentifier

if typing.TYPE_CHECKING:
    from .business_unit import BusinessUnitKeyReference
    from .cart import (
        CartResourceIdentifier,
        CustomLineItem,
        DirectDiscount,
        InventoryMode,
        LineItem,
        RoundingMode,
        ShippingInfo,
        ShippingRateInput,
        TaxCalculationMode,
        TaxedPrice,
        TaxMode,
    )
    from .common import Address, CreatedBy, LastModifiedBy, ReferenceTypeId, TypedMoney
    from .customer import CustomerReference
    from .customer_group import CustomerGroupReference
    from .order import PaymentInfo
    from .state import StateReference, StateResourceIdentifier
    from .store import StoreKeyReference
    from .type import (
        CustomFields,
        CustomFieldsDraft,
        FieldContainer,
        TypeResourceIdentifier,
    )

__all__ = [
    "QuoteRequest",
    "QuoteRequestChangeQuoteRequestStateAction",
    "QuoteRequestDraft",
    "QuoteRequestPagedQueryResponse",
    "QuoteRequestReference",
    "QuoteRequestResourceIdentifier",
    "QuoteRequestSetCustomFieldAction",
    "QuoteRequestSetCustomTypeAction",
    "QuoteRequestState",
    "QuoteRequestTransitionStateAction",
    "QuoteRequestUpdate",
    "QuoteRequestUpdateAction",
]


class QuoteRequest(BaseResource):
    #: User-defined unique identifier of the QuoteRequest.
    key: typing.Optional[str]
    #: Present on resources created after 1 February 2019 except for [events not tracked](/client-logging#events-tracked).
    last_modified_by: typing.Optional["LastModifiedBy"]
    #: Present on resources created after 1 February 2019 except for [events not tracked](/client-logging#events-tracked).
    created_by: typing.Optional["CreatedBy"]
    #: Indicates the current state of the Quote Request in the negotiation process.
    quote_request_state: "QuoteRequestState"
    #: Message from the Buyer included in the Quote Request.
    comment: typing.Optional[str]
    #: The [Buyer](/../api/quotes-overview#buyer) who raised the request.
    customer: "CustomerReference"
    #: Set automatically when `customer` is set and the Customer is a member of a Customer Group.
    #: Used for Product Variant price selection.
    customer_group: typing.Optional["CustomerGroupReference"]
    #: The Store to which the [Buyer](/../api/quotes-overview#buyer) belongs.
    store: typing.Optional["StoreKeyReference"]
    #: The Line Items for which a Quote is requested.
    line_items: typing.List["LineItem"]
    #: The Custom Line Items for which a Quote is requested.
    custom_line_items: typing.List["CustomLineItem"]
    #: Sum of all `totalPrice` fields of the `lineItems` and `customLineItems`, as well as the `price` field of `shippingInfo` (if it exists).
    #: `totalPrice` may or may not include the taxes: it depends on the taxRate.includedInPrice property of each price.
    total_price: "TypedMoney"
    #: Not set until the shipping address is set.
    #: Will be set automatically in the `Platform` TaxMode.
    #: For the `External` tax mode it will be set  as soon as the external tax rates for all line items, custom line items, and shipping in the cart are set.
    taxed_price: typing.Optional["TaxedPrice"]
    #: Used to determine the eligible [ShippingMethods](ctp:api:type:ShippingMethod)
    #: and rates as well as the tax rate of the Line Items.
    shipping_address: typing.Optional["Address"]
    #: Address used for invoicing.
    billing_address: typing.Optional["Address"]
    #: Inventory mode of the Cart referenced in the [QuoteRequestDraft](ctp:api:type:QuoteRequestDraft).
    inventory_mode: typing.Optional["InventoryMode"]
    #: Tax mode of the Cart referenced in the [QuoteRequestDraft](ctp:api:type:QuoteRequestDraft).
    tax_mode: "TaxMode"
    #: When calculating taxes for `taxedPrice`, the selected mode is used for rounding.
    tax_rounding_mode: "RoundingMode"
    #: When calculating taxes for `taxedPrice`, the selected mode is used for calculating the price with `LineItemLevel` (horizontally) or `UnitPriceLevel` (vertically) calculation mode.
    tax_calculation_mode: "TaxCalculationMode"
    #: Used for Product Variant price selection.
    country: typing.Optional[str]
    #: Set automatically once the [ShippingMethod](ctp:api:type:ShippingMethod) is set.
    shipping_info: typing.Optional["ShippingInfo"]
    #: Log of payment transactions related to the Quote.
    payment_info: typing.Optional["PaymentInfo"]
    #: Used to select a [ShippingRatePriceTier](ctp:api:type:ShippingRatePriceTier).
    shipping_rate_input: typing.Optional["ShippingRateInput"]
    #: Contains addresses for carts with multiple shipping addresses.
    #: Line items reference these addresses under their `shippingDetails`.
    #: The addresses captured here are not used to determine eligible shipping methods or the applicable tax rate.
    #: Only the cart's `shippingAddress` is used for this.
    item_shipping_addresses: typing.Optional[typing.List["Address"]]
    #: Discounts that are only valid for the Quote and cannot be associated to any other Cart or Order.
    direct_discounts: typing.Optional[typing.List["DirectDiscount"]]
    #: Custom Fields of the Quote Request.
    custom: typing.Optional["CustomFields"]
    #: [State](ctp:api:type:State) of the Quote Request.
    #: This reference can point to a State in a custom workflow.
    state: typing.Optional["StateReference"]
    #: The [BusinessUnit](ctp:api:type:BusinessUnit) for the Quote Request.
    business_unit: typing.Optional["BusinessUnitKeyReference"]

    def __init__(
        self,
        *,
        id: str,
        version: int,
        created_at: datetime.datetime,
        last_modified_at: datetime.datetime,
        key: typing.Optional[str] = None,
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        quote_request_state: "QuoteRequestState",
        comment: typing.Optional[str] = None,
        customer: "CustomerReference",
        customer_group: typing.Optional["CustomerGroupReference"] = None,
        store: typing.Optional["StoreKeyReference"] = None,
        line_items: typing.List["LineItem"],
        custom_line_items: typing.List["CustomLineItem"],
        total_price: "TypedMoney",
        taxed_price: typing.Optional["TaxedPrice"] = None,
        shipping_address: typing.Optional["Address"] = None,
        billing_address: typing.Optional["Address"] = None,
        inventory_mode: typing.Optional["InventoryMode"] = None,
        tax_mode: "TaxMode",
        tax_rounding_mode: "RoundingMode",
        tax_calculation_mode: "TaxCalculationMode",
        country: typing.Optional[str] = None,
        shipping_info: typing.Optional["ShippingInfo"] = None,
        payment_info: typing.Optional["PaymentInfo"] = None,
        shipping_rate_input: typing.Optional["ShippingRateInput"] = None,
        item_shipping_addresses: typing.Optional[typing.List["Address"]] = None,
        direct_discounts: typing.Optional[typing.List["DirectDiscount"]] = None,
        custom: typing.Optional["CustomFields"] = None,
        state: typing.Optional["StateReference"] = None,
        business_unit: typing.Optional["BusinessUnitKeyReference"] = None
    ):
        self.key = key
        self.last_modified_by = last_modified_by
        self.created_by = created_by
        self.quote_request_state = quote_request_state
        self.comment = comment
        self.customer = customer
        self.customer_group = customer_group
        self.store = store
        self.line_items = line_items
        self.custom_line_items = custom_line_items
        self.total_price = total_price
        self.taxed_price = taxed_price
        self.shipping_address = shipping_address
        self.billing_address = billing_address
        self.inventory_mode = inventory_mode
        self.tax_mode = tax_mode
        self.tax_rounding_mode = tax_rounding_mode
        self.tax_calculation_mode = tax_calculation_mode
        self.country = country
        self.shipping_info = shipping_info
        self.payment_info = payment_info
        self.shipping_rate_input = shipping_rate_input
        self.item_shipping_addresses = item_shipping_addresses
        self.direct_discounts = direct_discounts
        self.custom = custom
        self.state = state
        self.business_unit = business_unit

        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
        )

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "QuoteRequest":
        from ._schemas.quote_request import QuoteRequestSchema

        return QuoteRequestSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.quote_request import QuoteRequestSchema

        return QuoteRequestSchema().dump(self)


class QuoteRequestDraft(_BaseType):
    #: Cart for which a Quote is requested.
    #: Anonymous Carts, Carts with [Discount Codes](ctp:api:type:DiscountCode), or Carts with a `Multiple` [ShippingMode](ctp:api:type:ShippingMode) are not supported.
    cart: "CartResourceIdentifier"
    #: Current version of the referenced Cart.
    cart_version: int
    #: User-defined unique identifier for the QuoteRequest.
    key: typing.Optional[str]
    #: Message from the Buyer included in the Quote Request.
    comment: str
    #: Custom Fields to be added to the Quote Request.
    custom: typing.Optional["CustomFieldsDraft"]
    #: [State](ctp:api:type:State) of this Quote Request.
    #: This reference can point to a State in a custom workflow.
    state: typing.Optional["StateReference"]

    def __init__(
        self,
        *,
        cart: "CartResourceIdentifier",
        cart_version: int,
        key: typing.Optional[str] = None,
        comment: str,
        custom: typing.Optional["CustomFieldsDraft"] = None,
        state: typing.Optional["StateReference"] = None
    ):
        self.cart = cart
        self.cart_version = cart_version
        self.key = key
        self.comment = comment
        self.custom = custom
        self.state = state

        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "QuoteRequestDraft":
        from ._schemas.quote_request import QuoteRequestDraftSchema

        return QuoteRequestDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.quote_request import QuoteRequestDraftSchema

        return QuoteRequestDraftSchema().dump(self)


class QuoteRequestPagedQueryResponse(_BaseType):
    """[PagedQueryResult](/../api/general-concepts#pagedqueryresult) with results containing an array of [QuoteRequest](ctp:api:type:QuoteRequest)."""

    #: Number of [results requested](/../api/general-concepts#limit).
    limit: int
    #: Number of [elements skipped](/../api/general-concepts#offset).
    offset: int
    #: Actual number of results returned.
    count: int
    #: Total number of results matching the query.
    #: This number is an estimation that is not [strongly consistent](/../api/general-concepts#strong-consistency).
    #: This field is returned by default.
    #: For improved performance, calculating this field can be deactivated by using the query parameter `withTotal=false`.
    #: When the results are filtered with a [Query Predicate](/../api/predicates/query), `total` is subject to a [limit](/../api/limits#queries).
    total: typing.Optional[int]
    #: Quote Requests matching the query.
    results: typing.List["QuoteRequest"]

    def __init__(
        self,
        *,
        limit: int,
        offset: int,
        count: int,
        total: typing.Optional[int] = None,
        results: typing.List["QuoteRequest"]
    ):
        self.limit = limit
        self.offset = offset
        self.count = count
        self.total = total
        self.results = results

        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "QuoteRequestPagedQueryResponse":
        from ._schemas.quote_request import QuoteRequestPagedQueryResponseSchema

        return QuoteRequestPagedQueryResponseSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.quote_request import QuoteRequestPagedQueryResponseSchema

        return QuoteRequestPagedQueryResponseSchema().dump(self)


class QuoteRequestReference(Reference):
    """[Reference](ctp:api:type:Reference) to a [QuoteRequest](ctp:api:type:QuoteRequest)."""

    #: Contains the representation of the expanded QuoteRequest.
    #: Only present in responses to requests with [Reference Expansion](/../api/general-concepts#reference-expansion) for QuoteRequest.
    obj: typing.Optional["QuoteRequest"]

    def __init__(self, *, id: str, obj: typing.Optional["QuoteRequest"] = None):
        self.obj = obj

        super().__init__(id=id, type_id=ReferenceTypeId.QUOTE_REQUEST)

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "QuoteRequestReference":
        from ._schemas.quote_request import QuoteRequestReferenceSchema

        return QuoteRequestReferenceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.quote_request import QuoteRequestReferenceSchema

        return QuoteRequestReferenceSchema().dump(self)


class QuoteRequestResourceIdentifier(ResourceIdentifier):
    """[ResourceIdentifier](ctp:api:type:ResourceIdentifier) to a [QuoteRequest](ctp:api:type:QuoteRequest)."""

    def __init__(
        self, *, id: typing.Optional[str] = None, key: typing.Optional[str] = None
    ):

        super().__init__(id=id, key=key, type_id=ReferenceTypeId.QUOTE_REQUEST)

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "QuoteRequestResourceIdentifier":
        from ._schemas.quote_request import QuoteRequestResourceIdentifierSchema

        return QuoteRequestResourceIdentifierSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.quote_request import QuoteRequestResourceIdentifierSchema

        return QuoteRequestResourceIdentifierSchema().dump(self)


class QuoteRequestState(enum.Enum):
    """Predefined states tracking the status of the Quote Request in the negotiation process."""

    SUBMITTED = "Submitted"
    ACCEPTED = "Accepted"
    CLOSED = "Closed"
    REJECTED = "Rejected"
    CANCELLED = "Cancelled"


class QuoteRequestUpdate(_BaseType):
    #: Expected version of the [QuoteRequest](ctp:api:type:QuoteRequest) to which the changes should be applied.
    #: If the expected version does not match the actual version, a [409 Conflict](/../api/errors#409-conflict) error will be returned.
    version: int
    #: Update actions to be performed on the [QuoteRequest](ctp:api:type:QuoteRequest).
    actions: typing.List["QuoteRequestUpdateAction"]

    def __init__(
        self, *, version: int, actions: typing.List["QuoteRequestUpdateAction"]
    ):
        self.version = version
        self.actions = actions

        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "QuoteRequestUpdate":
        from ._schemas.quote_request import QuoteRequestUpdateSchema

        return QuoteRequestUpdateSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.quote_request import QuoteRequestUpdateSchema

        return QuoteRequestUpdateSchema().dump(self)


class QuoteRequestUpdateAction(_BaseType):
    action: str

    def __init__(self, *, action: str):
        self.action = action

        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "QuoteRequestUpdateAction":
        if data["action"] == "changeQuoteRequestState":
            from ._schemas.quote_request import (
                QuoteRequestChangeQuoteRequestStateActionSchema,
            )

            return QuoteRequestChangeQuoteRequestStateActionSchema().load(data)
        if data["action"] == "setCustomField":
            from ._schemas.quote_request import QuoteRequestSetCustomFieldActionSchema

            return QuoteRequestSetCustomFieldActionSchema().load(data)
        if data["action"] == "setCustomType":
            from ._schemas.quote_request import QuoteRequestSetCustomTypeActionSchema

            return QuoteRequestSetCustomTypeActionSchema().load(data)
        if data["action"] == "transitionState":
            from ._schemas.quote_request import QuoteRequestTransitionStateActionSchema

            return QuoteRequestTransitionStateActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.quote_request import QuoteRequestUpdateActionSchema

        return QuoteRequestUpdateActionSchema().dump(self)


class QuoteRequestChangeQuoteRequestStateAction(QuoteRequestUpdateAction):
    """Transitions the Quote Request to a different state.
    A Buyer is only allowed to cancel a Quote Request when it is in `Submitted` state.

    """

    #: New state to be set for the Quote Request.
    quote_request_state: "QuoteRequestState"

    def __init__(self, *, quote_request_state: "QuoteRequestState"):
        self.quote_request_state = quote_request_state

        super().__init__(action="changeQuoteRequestState")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "QuoteRequestChangeQuoteRequestStateAction":
        from ._schemas.quote_request import (
            QuoteRequestChangeQuoteRequestStateActionSchema,
        )

        return QuoteRequestChangeQuoteRequestStateActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.quote_request import (
            QuoteRequestChangeQuoteRequestStateActionSchema,
        )

        return QuoteRequestChangeQuoteRequestStateActionSchema().dump(self)


class QuoteRequestSetCustomFieldAction(QuoteRequestUpdateAction):
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
    ) -> "QuoteRequestSetCustomFieldAction":
        from ._schemas.quote_request import QuoteRequestSetCustomFieldActionSchema

        return QuoteRequestSetCustomFieldActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.quote_request import QuoteRequestSetCustomFieldActionSchema

        return QuoteRequestSetCustomFieldActionSchema().dump(self)


class QuoteRequestSetCustomTypeAction(QuoteRequestUpdateAction):
    #: Defines the [Type](ctp:api:type:Type) that extends the QuoteRequest with [Custom Fields](/../api/projects/custom-fields).
    #: If absent, any existing Type and Custom Fields are removed from the QuoteRequest.
    type: typing.Optional["TypeResourceIdentifier"]
    #: Sets the [Custom Fields](/../api/projects/custom-fields) fields for the QuoteRequest.
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
    ) -> "QuoteRequestSetCustomTypeAction":
        from ._schemas.quote_request import QuoteRequestSetCustomTypeActionSchema

        return QuoteRequestSetCustomTypeActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.quote_request import QuoteRequestSetCustomTypeActionSchema

        return QuoteRequestSetCustomTypeActionSchema().dump(self)


class QuoteRequestTransitionStateAction(QuoteRequestUpdateAction):
    """If the existing [State](ctp:api:type:State) has set `transitions`, there must be a direct transition to the new State. If `transitions` is not set, no validation is performed. This update action produces the [Quote Request State Transition](ctp:api:type:QuoteRequestStateTransitionMessage) Message."""

    #: Value to set.
    #: If there is no State yet, this must be an initial State.
    state: "StateResourceIdentifier"
    #: Switch validations on or off.
    force: typing.Optional[bool]

    def __init__(
        self, *, state: "StateResourceIdentifier", force: typing.Optional[bool] = None
    ):
        self.state = state
        self.force = force

        super().__init__(action="transitionState")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "QuoteRequestTransitionStateAction":
        from ._schemas.quote_request import QuoteRequestTransitionStateActionSchema

        return QuoteRequestTransitionStateActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.quote_request import QuoteRequestTransitionStateActionSchema

        return QuoteRequestTransitionStateActionSchema().dump(self)