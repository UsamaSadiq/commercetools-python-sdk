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
from .common import ImportResource

if typing.TYPE_CHECKING:
    from .common import LocalizedString

__all__ = [
    "CustomFieldBooleanType",
    "CustomFieldDateTimeType",
    "CustomFieldDateType",
    "CustomFieldEnumType",
    "CustomFieldEnumValue",
    "CustomFieldLocalizedEnumType",
    "CustomFieldLocalizedEnumValue",
    "CustomFieldLocalizedStringType",
    "CustomFieldMoneyType",
    "CustomFieldNumberType",
    "CustomFieldReferenceType",
    "CustomFieldReferenceValue",
    "CustomFieldSetType",
    "CustomFieldStringType",
    "CustomFieldTimeType",
    "FieldDefinition",
    "FieldType",
    "ResourceTypeId",
    "TypeImport",
    "TypeTextInputHint",
]


class TypeTextInputHint(enum.Enum):
    """Provides a visual representation type for this field. It is only relevant for string-based field types like [CustomFieldStringType](ctp:import:type:CustomFieldStringType) and [CustomFieldLocalizedStringType](ctp:import:type:CustomFieldLocalizedStringType)."""

    SINGLE_LINE = "SingleLine"
    MULTI_LINE = "MultiLine"


class ResourceTypeId(enum.Enum):
    """IDs indicating the [customizable resources and data types](/../api/projects/types#list-of-customizable-data-types). Maps to `Type.resourceTypeId`."""

    ADDRESS = "address"
    ASSET = "asset"
    BUSINESS_UNIT = "business-unit"
    CART_DISCOUNT = "cart-discount"
    CATEGORY = "category"
    CHANNEL = "channel"
    CUSTOMER = "customer"
    CUSTOMER_GROUP = "customer-group"
    CUSTOM_LINE_ITEM = "custom-line-item"
    DISCOUNT_CODE = "discount-code"
    INVENTORY_ENTRY = "inventory-entry"
    LINE_ITEM = "line-item"
    ORDER = "order"
    ORDER_EDIT = "order-edit"
    ORDER_DELIVERY = "order-delivery"
    ORDER_PARCEL = "order-parcel"
    ORDER_RETURN_ITEM = "order-return-item"
    PAYMENT = "payment"
    PAYMENT_INTERFACE_INTERACTION = "payment-interface-interaction"
    PRODUCT_PRICE = "product-price"
    PRODUCT_SELECTION = "product-selection"
    QUOTE = "quote"
    REVIEW = "review"
    SHIPPING = "shipping"
    SHIPPING_METHOD = "shipping-method"
    SHOPPING_LIST = "shopping-list"
    SHOPPING_LIST_TEXT_LINE_ITEM = "shopping-list-text-line-item"
    STANDALONE_PRICE = "standalone-price"
    STORE = "store"
    TRANSACTION = "transaction"


class FieldType(_BaseType):
    name: str

    def __init__(self, *, name: str):
        self.name = name

        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "FieldType":
        if data["name"] == "Boolean":
            from ._schemas.types import CustomFieldBooleanTypeSchema

            return CustomFieldBooleanTypeSchema().load(data)
        if data["name"] == "DateTime":
            from ._schemas.types import CustomFieldDateTimeTypeSchema

            return CustomFieldDateTimeTypeSchema().load(data)
        if data["name"] == "Date":
            from ._schemas.types import CustomFieldDateTypeSchema

            return CustomFieldDateTypeSchema().load(data)
        if data["name"] == "Enum":
            from ._schemas.types import CustomFieldEnumTypeSchema

            return CustomFieldEnumTypeSchema().load(data)
        if data["name"] == "LocalizedEnum":
            from ._schemas.types import CustomFieldLocalizedEnumTypeSchema

            return CustomFieldLocalizedEnumTypeSchema().load(data)
        if data["name"] == "LocalizedString":
            from ._schemas.types import CustomFieldLocalizedStringTypeSchema

            return CustomFieldLocalizedStringTypeSchema().load(data)
        if data["name"] == "Money":
            from ._schemas.types import CustomFieldMoneyTypeSchema

            return CustomFieldMoneyTypeSchema().load(data)
        if data["name"] == "Number":
            from ._schemas.types import CustomFieldNumberTypeSchema

            return CustomFieldNumberTypeSchema().load(data)
        if data["name"] == "Reference":
            from ._schemas.types import CustomFieldReferenceTypeSchema

            return CustomFieldReferenceTypeSchema().load(data)
        if data["name"] == "Set":
            from ._schemas.types import CustomFieldSetTypeSchema

            return CustomFieldSetTypeSchema().load(data)
        if data["name"] == "String":
            from ._schemas.types import CustomFieldStringTypeSchema

            return CustomFieldStringTypeSchema().load(data)
        if data["name"] == "Time":
            from ._schemas.types import CustomFieldTimeTypeSchema

            return CustomFieldTimeTypeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.types import FieldTypeSchema

        return FieldTypeSchema().dump(self)


class CustomFieldBooleanType(FieldType):
    """Field type for Boolean values."""

    def __init__(self):
        super().__init__(name="Boolean")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CustomFieldBooleanType":
        from ._schemas.types import CustomFieldBooleanTypeSchema

        return CustomFieldBooleanTypeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.types import CustomFieldBooleanTypeSchema

        return CustomFieldBooleanTypeSchema().dump(self)


class CustomFieldDateTimeType(FieldType):
    """Field type for [DateTime](ctp:import:type:DateTime) values."""

    def __init__(self):
        super().__init__(name="DateTime")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CustomFieldDateTimeType":
        from ._schemas.types import CustomFieldDateTimeTypeSchema

        return CustomFieldDateTimeTypeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.types import CustomFieldDateTimeTypeSchema

        return CustomFieldDateTimeTypeSchema().dump(self)


class CustomFieldDateType(FieldType):
    """Field type for [Date](ctp:import:type:Date) values."""

    def __init__(self):
        super().__init__(name="Date")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "CustomFieldDateType":
        from ._schemas.types import CustomFieldDateTypeSchema

        return CustomFieldDateTypeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.types import CustomFieldDateTypeSchema

        return CustomFieldDateTypeSchema().dump(self)


class CustomFieldEnumType(FieldType):
    """Field type for enum values."""

    #: Allowed values.
    values: typing.List["CustomFieldEnumValue"]

    def __init__(self, *, values: typing.List["CustomFieldEnumValue"]):
        self.values = values

        super().__init__(name="Enum")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "CustomFieldEnumType":
        from ._schemas.types import CustomFieldEnumTypeSchema

        return CustomFieldEnumTypeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.types import CustomFieldEnumTypeSchema

        return CustomFieldEnumTypeSchema().dump(self)


class CustomFieldEnumValue(_BaseType):
    """Defines an allowed value of a [CustomFieldEnumType](ctp:import:type:CustomFieldEnumType) field."""

    #: Key of the value used as a programmatic identifier.
    key: str
    #: Descriptive label of the value.
    label: str

    def __init__(self, *, key: str, label: str):
        self.key = key
        self.label = label

        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "CustomFieldEnumValue":
        from ._schemas.types import CustomFieldEnumValueSchema

        return CustomFieldEnumValueSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.types import CustomFieldEnumValueSchema

        return CustomFieldEnumValueSchema().dump(self)


class CustomFieldLocalizedEnumType(FieldType):
    """Field type for localized enum values."""

    #: Allowed values.
    values: typing.List["CustomFieldLocalizedEnumValue"]

    def __init__(self, *, values: typing.List["CustomFieldLocalizedEnumValue"]):
        self.values = values

        super().__init__(name="LocalizedEnum")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CustomFieldLocalizedEnumType":
        from ._schemas.types import CustomFieldLocalizedEnumTypeSchema

        return CustomFieldLocalizedEnumTypeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.types import CustomFieldLocalizedEnumTypeSchema

        return CustomFieldLocalizedEnumTypeSchema().dump(self)


class CustomFieldLocalizedEnumValue(_BaseType):
    """Defines an allowed value of a [CustomFieldLocalizedEnumType](ctp:import:type:CustomFieldLocalizedEnumType) field."""

    #: Key of the value used as a programmatic identifier.
    key: str
    #: Descriptive localized label of the value.
    label: "LocalizedString"

    def __init__(self, *, key: str, label: "LocalizedString"):
        self.key = key
        self.label = label

        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CustomFieldLocalizedEnumValue":
        from ._schemas.types import CustomFieldLocalizedEnumValueSchema

        return CustomFieldLocalizedEnumValueSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.types import CustomFieldLocalizedEnumValueSchema

        return CustomFieldLocalizedEnumValueSchema().dump(self)


class CustomFieldLocalizedStringType(FieldType):
    """Field type for [LocalizedString](ctp:import:type:LocalizedString) values."""

    def __init__(self):
        super().__init__(name="LocalizedString")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CustomFieldLocalizedStringType":
        from ._schemas.types import CustomFieldLocalizedStringTypeSchema

        return CustomFieldLocalizedStringTypeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.types import CustomFieldLocalizedStringTypeSchema

        return CustomFieldLocalizedStringTypeSchema().dump(self)


class CustomFieldMoneyType(FieldType):
    """Field type for [CentPrecisionMoney](ctp:import:type:CentPrecisionMoney) values."""

    def __init__(self):
        super().__init__(name="Money")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "CustomFieldMoneyType":
        from ._schemas.types import CustomFieldMoneyTypeSchema

        return CustomFieldMoneyTypeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.types import CustomFieldMoneyTypeSchema

        return CustomFieldMoneyTypeSchema().dump(self)


class CustomFieldNumberType(FieldType):
    """Field type for number values."""

    def __init__(self):
        super().__init__(name="Number")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "CustomFieldNumberType":
        from ._schemas.types import CustomFieldNumberTypeSchema

        return CustomFieldNumberTypeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.types import CustomFieldNumberTypeSchema

        return CustomFieldNumberTypeSchema().dump(self)


class CustomFieldReferenceType(FieldType):
    """Field type for [Reference](ctp:import:type:Reference) values."""

    #: Resource type the Custom Field can reference.
    reference_type_id: "CustomFieldReferenceValue"

    def __init__(self, *, reference_type_id: "CustomFieldReferenceValue"):
        self.reference_type_id = reference_type_id

        super().__init__(name="Reference")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CustomFieldReferenceType":
        from ._schemas.types import CustomFieldReferenceTypeSchema

        return CustomFieldReferenceTypeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.types import CustomFieldReferenceTypeSchema

        return CustomFieldReferenceTypeSchema().dump(self)


class CustomFieldReferenceValue(enum.Enum):
    """Defines which resource type a [CustomFieldReferenceType](ctp:import:type:CustomFieldReferenceType) can reference."""

    ASSOCIATE_ROLE = "associate-role"
    BUSINESS_UNIT = "business-unit"
    CART = "cart"
    CATEGORY = "category"
    CHANNEL = "channel"
    CUSTOMER = "customer"
    KEY_VALUE_DOCUMENT = "key-value-document"
    ORDER = "order"
    PRODUCT = "product"
    PRODUCT_TYPE = "product-type"
    REVIEW = "review"
    STATE = "state"
    SHIPPING_METHOD = "shipping-method"
    ZONE = "zone"


class CustomFieldSetType(FieldType):
    """Values of a SetType Custom Field are sets of values of the specified `elementType` (without duplicate elements)."""

    #: Field type of the elements in the set.
    element_type: "FieldType"

    def __init__(self, *, element_type: "FieldType"):
        self.element_type = element_type

        super().__init__(name="Set")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "CustomFieldSetType":
        from ._schemas.types import CustomFieldSetTypeSchema

        return CustomFieldSetTypeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.types import CustomFieldSetTypeSchema

        return CustomFieldSetTypeSchema().dump(self)


class CustomFieldStringType(FieldType):
    """Field type for string values."""

    def __init__(self):
        super().__init__(name="String")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "CustomFieldStringType":
        from ._schemas.types import CustomFieldStringTypeSchema

        return CustomFieldStringTypeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.types import CustomFieldStringTypeSchema

        return CustomFieldStringTypeSchema().dump(self)


class CustomFieldTimeType(FieldType):
    """Field type for [Time](ctp:import:type:Time) values."""

    def __init__(self):
        super().__init__(name="Time")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "CustomFieldTimeType":
        from ._schemas.types import CustomFieldTimeTypeSchema

        return CustomFieldTimeTypeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.types import CustomFieldTimeTypeSchema

        return CustomFieldTimeTypeSchema().dump(self)


class FieldDefinition(_BaseType):
    """Defines a [Custom Field](/../api/projects/custom-fields) and its meta-information. Maps to `Type.FieldDefinition`."""

    #: Data type of the Custom Field to define.
    type: "FieldType"
    #: Name of the Custom Field to define. Must be unique for a given [ResourceTypeId](ctp:import:type:ResourceTypeId). In case there is a FieldDefinition with the same `name` in another Type, both FieldDefinitions must have the same `type`. This value cannot be changed after the Type is imported.
    name: str
    #: A human-readable label for the field.
    label: "LocalizedString"
    #: Defines whether the field is required to have a value. This value cannot be changed after the Type is imported.
    required: bool
    #: Provides a visual representation type for this field. It is only relevant for string-based field types like [CustomFieldStringType](ctp:import:type:CustomFieldStringType) and [CustomFieldLocalizedStringType](ctp:import:type:CustomFieldLocalizedStringType).
    input_hint: typing.Optional["TypeTextInputHint"]

    def __init__(
        self,
        *,
        type: "FieldType",
        name: str,
        label: "LocalizedString",
        required: bool,
        input_hint: typing.Optional["TypeTextInputHint"] = None
    ):
        self.type = type
        self.name = name
        self.label = label
        self.required = required
        self.input_hint = input_hint

        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "FieldDefinition":
        from ._schemas.types import FieldDefinitionSchema

        return FieldDefinitionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.types import FieldDefinitionSchema

        return FieldDefinitionSchema().dump(self)


class TypeImport(ImportResource):
    """The data representation for a Type to be imported that is persisted as a [Type](/../api/projects/types#type) in the Project."""

    #: Maps to `Type.name`.
    name: "LocalizedString"
    #: Maps to `Type.description`.
    description: typing.Optional["LocalizedString"]
    #: Maps to `Type.resourceTypeIds`. This value cannot be changed after the Type is imported.
    resource_type_ids: typing.List["ResourceTypeId"]
    #: Maps to `Type.fieldDefinitions`.
    field_definitions: typing.Optional[typing.List["FieldDefinition"]]

    def __init__(
        self,
        *,
        key: str,
        name: "LocalizedString",
        description: typing.Optional["LocalizedString"] = None,
        resource_type_ids: typing.List["ResourceTypeId"],
        field_definitions: typing.Optional[typing.List["FieldDefinition"]] = None
    ):
        self.name = name
        self.description = description
        self.resource_type_ids = resource_type_ids
        self.field_definitions = field_definitions

        super().__init__(key=key)

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "TypeImport":
        from ._schemas.types import TypeImportSchema

        return TypeImportSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.types import TypeImportSchema

        return TypeImportSchema().dump(self)
