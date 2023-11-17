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
from .common import BaseResource, Reference, ReferenceTypeId, ResourceIdentifier

if typing.TYPE_CHECKING:
    from .common import CreatedBy, LastModifiedBy, LocalizedString, ReferenceTypeId

__all__ = [
    "AttributeGroup",
    "AttributeGroupAddAttributeAction",
    "AttributeGroupChangeNameAction",
    "AttributeGroupDraft",
    "AttributeGroupPagedQueryResponse",
    "AttributeGroupReference",
    "AttributeGroupRemoveAttributeAction",
    "AttributeGroupResourceIdentifier",
    "AttributeGroupSetAttributesAction",
    "AttributeGroupSetDescriptionAction",
    "AttributeGroupSetKeyAction",
    "AttributeGroupUpdate",
    "AttributeGroupUpdateAction",
    "AttributeReference",
]


class AttributeGroup(BaseResource):
    #: Present on resources created after 1 February 2019 except for [events not tracked](/../api/client-logging#events-tracked).
    last_modified_by: typing.Optional["LastModifiedBy"]
    #: Present on resources created after 1 February 2019 except for [events not tracked](/../api/client-logging#events-tracked).
    created_by: typing.Optional["CreatedBy"]
    #: Name of the AttributeGroup.
    name: "LocalizedString"
    #: Description of the AttributeGroup.
    description: typing.Optional["LocalizedString"]
    #: [Attributes](ctp:api:type:AttributeDefinition) with unique values.
    attributes: typing.List["AttributeReference"]
    #: User-defined unique identifier of the AttributeGroup.
    key: typing.Optional[str]

    def __init__(
        self,
        *,
        id: str,
        version: int,
        created_at: datetime.datetime,
        last_modified_at: datetime.datetime,
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        name: "LocalizedString",
        description: typing.Optional["LocalizedString"] = None,
        attributes: typing.List["AttributeReference"],
        key: typing.Optional[str] = None
    ):
        self.last_modified_by = last_modified_by
        self.created_by = created_by
        self.name = name
        self.description = description
        self.attributes = attributes
        self.key = key

        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
        )

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "AttributeGroup":
        from ._schemas.attribute_group import AttributeGroupSchema

        return AttributeGroupSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.attribute_group import AttributeGroupSchema

        return AttributeGroupSchema().dump(self)


class AttributeGroupDraft(_BaseType):
    #: Name of the AttributeGroup.
    name: "LocalizedString"
    #: Description of the AttributeGroup.
    description: typing.Optional["LocalizedString"]
    #: [Attributes](ctp:api:type:AttributeDefinition) with unique values.
    attributes: typing.List["AttributeReference"]
    #: User-defined unique identifier for the AttributeGroup.
    key: typing.Optional[str]

    def __init__(
        self,
        *,
        name: "LocalizedString",
        description: typing.Optional["LocalizedString"] = None,
        attributes: typing.List["AttributeReference"],
        key: typing.Optional[str] = None
    ):
        self.name = name
        self.description = description
        self.attributes = attributes
        self.key = key

        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "AttributeGroupDraft":
        from ._schemas.attribute_group import AttributeGroupDraftSchema

        return AttributeGroupDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.attribute_group import AttributeGroupDraftSchema

        return AttributeGroupDraftSchema().dump(self)


class AttributeGroupPagedQueryResponse(_BaseType):
    """[PagedQueryResult](/../api/general-concepts#pagedqueryresult) with `results` containing an array of [AttributeGroup](ctp:api:type:AttributeGroup)."""

    #: Number of results requested in the query request.
    limit: int
    #: Offset supplied by the client or the server default.
    #: It is the number of elements skipped, not a page number.
    offset: int
    #: Actual number of results returned.
    count: int
    #: Total number of results matching the query.
    #: This number is an estimation that is not [strongly consistent](/../api/general-concepts#strong-consistency).
    #: This field is returned by default.
    #: For improved performance, calculating this field can be deactivated by using the query parameter `withTotal=false`.
    #: When the results are filtered with a [Query Predicate](/../api/predicates/query), `total` is subject to a [limit](/../api/limits#queries).
    total: typing.Optional[int]
    #: [AttributeGroups](ctp:api:type:AttributeGroup) matching the query.
    results: typing.List["AttributeGroup"]

    def __init__(
        self,
        *,
        limit: int,
        offset: int,
        count: int,
        total: typing.Optional[int] = None,
        results: typing.List["AttributeGroup"]
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
    ) -> "AttributeGroupPagedQueryResponse":
        from ._schemas.attribute_group import AttributeGroupPagedQueryResponseSchema

        return AttributeGroupPagedQueryResponseSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.attribute_group import AttributeGroupPagedQueryResponseSchema

        return AttributeGroupPagedQueryResponseSchema().dump(self)


class AttributeGroupReference(Reference):
    """[Reference](/../api/types#reference) to an [AttributeGroup](ctp:api:type:AttributeGroup)."""

    #: Contains the representation of the expanded AttributeGroup. Only present in responses to requests with [Reference Expansion](/../api/general-concepts#reference-expansion) for AttributeGroup.
    obj: typing.Optional["AttributeGroup"]

    def __init__(self, *, id: str, obj: typing.Optional["AttributeGroup"] = None):
        self.obj = obj

        super().__init__(id=id, type_id=ReferenceTypeId.ATTRIBUTE_GROUP)

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "AttributeGroupReference":
        from ._schemas.attribute_group import AttributeGroupReferenceSchema

        return AttributeGroupReferenceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.attribute_group import AttributeGroupReferenceSchema

        return AttributeGroupReferenceSchema().dump(self)


class AttributeGroupResourceIdentifier(ResourceIdentifier):
    """[ResourceIdentifier](/../api/types#resourceidentifier) to an [AttributeGroup](ctp:api:type:AttributeGroup). Either `id` or `key` is required. If both are set, an [InvalidJsonInput](/../api/errors#invalidjsoninput) error is returned."""

    def __init__(
        self, *, id: typing.Optional[str] = None, key: typing.Optional[str] = None
    ):
        super().__init__(id=id, key=key, type_id=ReferenceTypeId.ATTRIBUTE_GROUP)

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "AttributeGroupResourceIdentifier":
        from ._schemas.attribute_group import AttributeGroupResourceIdentifierSchema

        return AttributeGroupResourceIdentifierSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.attribute_group import AttributeGroupResourceIdentifierSchema

        return AttributeGroupResourceIdentifierSchema().dump(self)


class AttributeGroupUpdate(_BaseType):
    #: Expected version of the AttributeGroup on which the changes should be applied. If the expected version does not match the actual version, a [409 Conflict](/../api/errors#409-conflict) will be returned.
    version: int
    #: Update actions to be performed on the AttributeGroup.
    actions: typing.List["AttributeGroupUpdateAction"]

    def __init__(
        self, *, version: int, actions: typing.List["AttributeGroupUpdateAction"]
    ):
        self.version = version
        self.actions = actions

        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "AttributeGroupUpdate":
        from ._schemas.attribute_group import AttributeGroupUpdateSchema

        return AttributeGroupUpdateSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.attribute_group import AttributeGroupUpdateSchema

        return AttributeGroupUpdateSchema().dump(self)


class AttributeGroupUpdateAction(_BaseType):
    action: str

    def __init__(self, *, action: str):
        self.action = action

        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "AttributeGroupUpdateAction":
        if data["action"] == "addAttribute":
            from ._schemas.attribute_group import AttributeGroupAddAttributeActionSchema

            return AttributeGroupAddAttributeActionSchema().load(data)
        if data["action"] == "changeName":
            from ._schemas.attribute_group import AttributeGroupChangeNameActionSchema

            return AttributeGroupChangeNameActionSchema().load(data)
        if data["action"] == "removeAttribute":
            from ._schemas.attribute_group import (
                AttributeGroupRemoveAttributeActionSchema,
            )

            return AttributeGroupRemoveAttributeActionSchema().load(data)
        if data["action"] == "setAttributes":
            from ._schemas.attribute_group import (
                AttributeGroupSetAttributesActionSchema,
            )

            return AttributeGroupSetAttributesActionSchema().load(data)
        if data["action"] == "setDescription":
            from ._schemas.attribute_group import (
                AttributeGroupSetDescriptionActionSchema,
            )

            return AttributeGroupSetDescriptionActionSchema().load(data)
        if data["action"] == "setKey":
            from ._schemas.attribute_group import AttributeGroupSetKeyActionSchema

            return AttributeGroupSetKeyActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.attribute_group import AttributeGroupUpdateActionSchema

        return AttributeGroupUpdateActionSchema().dump(self)


class AttributeReference(_BaseType):
    #: The Attribute's `name` as given in its [AttributeDefinition](ctp:api:type:AttributeDefinition).
    key: str

    def __init__(self, *, key: str):
        self.key = key

        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "AttributeReference":
        from ._schemas.attribute_group import AttributeReferenceSchema

        return AttributeReferenceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.attribute_group import AttributeReferenceSchema

        return AttributeReferenceSchema().dump(self)


class AttributeGroupAddAttributeAction(AttributeGroupUpdateAction):
    #: Value to add.
    attribute: "AttributeReference"

    def __init__(self, *, attribute: "AttributeReference"):
        self.attribute = attribute

        super().__init__(action="addAttribute")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "AttributeGroupAddAttributeAction":
        from ._schemas.attribute_group import AttributeGroupAddAttributeActionSchema

        return AttributeGroupAddAttributeActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.attribute_group import AttributeGroupAddAttributeActionSchema

        return AttributeGroupAddAttributeActionSchema().dump(self)


class AttributeGroupChangeNameAction(AttributeGroupUpdateAction):
    #: New value to set.
    #: Must not be empty.
    name: "LocalizedString"

    def __init__(self, *, name: "LocalizedString"):
        self.name = name

        super().__init__(action="changeName")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "AttributeGroupChangeNameAction":
        from ._schemas.attribute_group import AttributeGroupChangeNameActionSchema

        return AttributeGroupChangeNameActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.attribute_group import AttributeGroupChangeNameActionSchema

        return AttributeGroupChangeNameActionSchema().dump(self)


class AttributeGroupRemoveAttributeAction(AttributeGroupUpdateAction):
    #: Value to remove.
    attribute: "AttributeReference"

    def __init__(self, *, attribute: "AttributeReference"):
        self.attribute = attribute

        super().__init__(action="removeAttribute")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "AttributeGroupRemoveAttributeAction":
        from ._schemas.attribute_group import AttributeGroupRemoveAttributeActionSchema

        return AttributeGroupRemoveAttributeActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.attribute_group import AttributeGroupRemoveAttributeActionSchema

        return AttributeGroupRemoveAttributeActionSchema().dump(self)


class AttributeGroupSetAttributesAction(AttributeGroupUpdateAction):
    #: New unique values to set.
    attributes: typing.List["AttributeReference"]

    def __init__(self, *, attributes: typing.List["AttributeReference"]):
        self.attributes = attributes

        super().__init__(action="setAttributes")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "AttributeGroupSetAttributesAction":
        from ._schemas.attribute_group import AttributeGroupSetAttributesActionSchema

        return AttributeGroupSetAttributesActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.attribute_group import AttributeGroupSetAttributesActionSchema

        return AttributeGroupSetAttributesActionSchema().dump(self)


class AttributeGroupSetDescriptionAction(AttributeGroupUpdateAction):
    #: Value to set.
    #: If empty, any existing value will be removed.
    description: typing.Optional["LocalizedString"]

    def __init__(self, *, description: typing.Optional["LocalizedString"] = None):
        self.description = description

        super().__init__(action="setDescription")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "AttributeGroupSetDescriptionAction":
        from ._schemas.attribute_group import AttributeGroupSetDescriptionActionSchema

        return AttributeGroupSetDescriptionActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.attribute_group import AttributeGroupSetDescriptionActionSchema

        return AttributeGroupSetDescriptionActionSchema().dump(self)


class AttributeGroupSetKeyAction(AttributeGroupUpdateAction):
    #: If `key` is absent or `null`, the existing key, if any, will be removed.
    key: typing.Optional[str]

    def __init__(self, *, key: typing.Optional[str] = None):
        self.key = key

        super().__init__(action="setKey")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "AttributeGroupSetKeyAction":
        from ._schemas.attribute_group import AttributeGroupSetKeyActionSchema

        return AttributeGroupSetKeyActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.attribute_group import AttributeGroupSetKeyActionSchema

        return AttributeGroupSetKeyActionSchema().dump(self)
