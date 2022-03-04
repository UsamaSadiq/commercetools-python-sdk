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
    from .common import CreatedBy, LastModifiedBy, ReferenceTypeId

__all__ = [
    "Location",
    "Zone",
    "ZoneAddLocationAction",
    "ZoneChangeNameAction",
    "ZoneDraft",
    "ZonePagedQueryResponse",
    "ZoneReference",
    "ZoneRemoveLocationAction",
    "ZoneResourceIdentifier",
    "ZoneSetDescriptionAction",
    "ZoneSetKeyAction",
    "ZoneUpdate",
    "ZoneUpdateAction",
]


class Location(_BaseType):
    """A geographical location representing a country and optionally a state within this country.  A location can only be assigned to one Zone."""

    #: Country code of the geographic location.
    country: str
    #: State within the country.
    state: typing.Optional[str]

    def __init__(self, *, country: str, state: typing.Optional[str] = None):
        self.country = country
        self.state = state
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "Location":
        from ._schemas.zone import LocationSchema

        return LocationSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.zone import LocationSchema

        return LocationSchema().dump(self)


class Zone(BaseResource):
    #: Present on resources created after 1 February 2019 except for [events not tracked](/../api/client-logging#events-tracked).
    last_modified_by: typing.Optional["LastModifiedBy"]
    #: Present on resources created after 1 February 2019 except for [events not tracked](/../api/client-logging#events-tracked).
    created_by: typing.Optional["CreatedBy"]
    #: User-defined unique identifier for the Zone.
    key: typing.Optional[str]
    #: Name of the Zone.
    name: str
    #: Description of the Zone.
    description: typing.Optional[str]
    #: List of locations that belong to the Zone.
    locations: typing.List["Location"]

    def __init__(
        self,
        *,
        id: str,
        version: int,
        created_at: datetime.datetime,
        last_modified_at: datetime.datetime,
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        key: typing.Optional[str] = None,
        name: str,
        description: typing.Optional[str] = None,
        locations: typing.List["Location"]
    ):
        self.last_modified_by = last_modified_by
        self.created_by = created_by
        self.key = key
        self.name = name
        self.description = description
        self.locations = locations
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
        )

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "Zone":
        from ._schemas.zone import ZoneSchema

        return ZoneSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.zone import ZoneSchema

        return ZoneSchema().dump(self)


class ZoneDraft(_BaseType):
    #: User-defined unique identifier for the Zone.
    key: typing.Optional[str]
    #: Name of the Zone.
    name: str
    #: Description of the Zone.
    description: typing.Optional[str]
    #: List of locations that belong to the Zone.
    locations: typing.Optional[typing.List["Location"]]

    def __init__(
        self,
        *,
        key: typing.Optional[str] = None,
        name: str,
        description: typing.Optional[str] = None,
        locations: typing.Optional[typing.List["Location"]] = None
    ):
        self.key = key
        self.name = name
        self.description = description
        self.locations = locations
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ZoneDraft":
        from ._schemas.zone import ZoneDraftSchema

        return ZoneDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.zone import ZoneDraftSchema

        return ZoneDraftSchema().dump(self)


class ZonePagedQueryResponse(_BaseType):
    """[PagedQueryResult](/general-concepts#pagedqueryresult) with `results` containing an array of [Zone](ctp:api:type:Zone)."""

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
    #: [Zones](ctp:api:type:Zone) matching the query.
    results: typing.List["Zone"]

    def __init__(
        self,
        *,
        limit: int,
        offset: int,
        count: int,
        total: typing.Optional[int] = None,
        results: typing.List["Zone"]
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
    ) -> "ZonePagedQueryResponse":
        from ._schemas.zone import ZonePagedQueryResponseSchema

        return ZonePagedQueryResponseSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.zone import ZonePagedQueryResponseSchema

        return ZonePagedQueryResponseSchema().dump(self)


class ZoneReference(Reference):
    """[Reference](/types#reference) to a [Zone](ctp:api:type:Zone)."""

    #: Contains the representation of the expanded Zone. Only present in responses to requests with [Reference Expansion](/../api/general-concepts#reference-expansion) for Zones.
    obj: typing.Optional["Zone"]

    def __init__(self, *, id: str, obj: typing.Optional["Zone"] = None):
        self.obj = obj
        super().__init__(id=id, type_id=ReferenceTypeId.ZONE)

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ZoneReference":
        from ._schemas.zone import ZoneReferenceSchema

        return ZoneReferenceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.zone import ZoneReferenceSchema

        return ZoneReferenceSchema().dump(self)


class ZoneResourceIdentifier(ResourceIdentifier):
    """[ResourceIdentifier](/../api/types#resourceidentifier) to a [Zone](ctp:api:type:Zone)."""

    def __init__(
        self, *, id: typing.Optional[str] = None, key: typing.Optional[str] = None
    ):

        super().__init__(id=id, key=key, type_id=ReferenceTypeId.ZONE)

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ZoneResourceIdentifier":
        from ._schemas.zone import ZoneResourceIdentifierSchema

        return ZoneResourceIdentifierSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.zone import ZoneResourceIdentifierSchema

        return ZoneResourceIdentifierSchema().dump(self)


class ZoneUpdate(_BaseType):
    #: Expected version of the Zone on which the changes should be applied. If the expected version does not match the actual version, a [409 Conflict](/../api/errors#409-conflict) will be returned.
    version: int
    #: Update actions to be performed on the Zone.
    actions: typing.List["ZoneUpdateAction"]

    def __init__(self, *, version: int, actions: typing.List["ZoneUpdateAction"]):
        self.version = version
        self.actions = actions
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ZoneUpdate":
        from ._schemas.zone import ZoneUpdateSchema

        return ZoneUpdateSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.zone import ZoneUpdateSchema

        return ZoneUpdateSchema().dump(self)


class ZoneUpdateAction(_BaseType):
    action: str

    def __init__(self, *, action: str):
        self.action = action
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ZoneUpdateAction":
        if data["action"] == "addLocation":
            from ._schemas.zone import ZoneAddLocationActionSchema

            return ZoneAddLocationActionSchema().load(data)
        if data["action"] == "changeName":
            from ._schemas.zone import ZoneChangeNameActionSchema

            return ZoneChangeNameActionSchema().load(data)
        if data["action"] == "removeLocation":
            from ._schemas.zone import ZoneRemoveLocationActionSchema

            return ZoneRemoveLocationActionSchema().load(data)
        if data["action"] == "setDescription":
            from ._schemas.zone import ZoneSetDescriptionActionSchema

            return ZoneSetDescriptionActionSchema().load(data)
        if data["action"] == "setKey":
            from ._schemas.zone import ZoneSetKeyActionSchema

            return ZoneSetKeyActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.zone import ZoneUpdateActionSchema

        return ZoneUpdateActionSchema().dump(self)


class ZoneAddLocationAction(ZoneUpdateAction):
    #: Location to be added to the Zone.
    location: "Location"

    def __init__(self, *, location: "Location"):
        self.location = location
        super().__init__(action="addLocation")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ZoneAddLocationAction":
        from ._schemas.zone import ZoneAddLocationActionSchema

        return ZoneAddLocationActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.zone import ZoneAddLocationActionSchema

        return ZoneAddLocationActionSchema().dump(self)


class ZoneChangeNameAction(ZoneUpdateAction):
    #: New name of the Zone.
    name: str

    def __init__(self, *, name: str):
        self.name = name
        super().__init__(action="changeName")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ZoneChangeNameAction":
        from ._schemas.zone import ZoneChangeNameActionSchema

        return ZoneChangeNameActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.zone import ZoneChangeNameActionSchema

        return ZoneChangeNameActionSchema().dump(self)


class ZoneRemoveLocationAction(ZoneUpdateAction):
    #: Location to be removed from the Zone.
    location: "Location"

    def __init__(self, *, location: "Location"):
        self.location = location
        super().__init__(action="removeLocation")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ZoneRemoveLocationAction":
        from ._schemas.zone import ZoneRemoveLocationActionSchema

        return ZoneRemoveLocationActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.zone import ZoneRemoveLocationActionSchema

        return ZoneRemoveLocationActionSchema().dump(self)


class ZoneSetDescriptionAction(ZoneUpdateAction):
    #: Description of the Zone.
    description: typing.Optional[str]

    def __init__(self, *, description: typing.Optional[str] = None):
        self.description = description
        super().__init__(action="setDescription")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ZoneSetDescriptionAction":
        from ._schemas.zone import ZoneSetDescriptionActionSchema

        return ZoneSetDescriptionActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.zone import ZoneSetDescriptionActionSchema

        return ZoneSetDescriptionActionSchema().dump(self)


class ZoneSetKeyAction(ZoneUpdateAction):
    #: If `key` is absent or `null`, the existing key, if any, will be removed.
    key: typing.Optional[str]

    def __init__(self, *, key: typing.Optional[str] = None):
        self.key = key
        super().__init__(action="setKey")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ZoneSetKeyAction":
        from ._schemas.zone import ZoneSetKeyActionSchema

        return ZoneSetKeyActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.zone import ZoneSetKeyActionSchema

        return ZoneSetKeyActionSchema().dump(self)
