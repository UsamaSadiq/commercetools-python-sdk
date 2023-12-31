import copy
import datetime
import typing
import uuid

from commercetools.platform import models
from commercetools.platform.models._schemas.extension import (
    ExtensionDraftSchema,
    ExtensionPagedQueryResponseSchema,
    ExtensionSchema,
    ExtensionUpdateSchema,
)
from commercetools.testing.abstract import BaseModel, ServiceBackend
from commercetools.testing.utils import update_attribute, update_nested_object_attribute


class ExtensionsModel(BaseModel):
    _primary_type_name = "extension"
    _resource_schema = ExtensionSchema
    _unique_values = ["key"]

    def _create_from_draft(
        self, draft: models.ExtensionDraft, id: typing.Optional[str] = None
    ) -> models.Extension:
        object_id = str(uuid.UUID(id) if id is not None else uuid.uuid4())
        return models.Extension(
            id=str(object_id),
            version=1,
            created_at=datetime.datetime.now(datetime.timezone.utc),
            last_modified_at=datetime.datetime.now(datetime.timezone.utc),
            key=draft.key,
            destination=draft.destination,
            triggers=draft.triggers,
            timeout_in_ms=draft.timeout_in_ms,
        )


class ExtensionsBackend(ServiceBackend):
    service_path = "extensions"
    model_class = ExtensionsModel
    _schema_draft = ExtensionDraftSchema
    _schema_update = ExtensionUpdateSchema
    _schema_query_response = ExtensionPagedQueryResponseSchema

    def urls(self):
        return [
            ("^$", "GET", self.query),
            ("^$", "POST", self.create),
            ("^(?P<id>[^/]+)$", "GET", self.get_by_id),
            ("^(?P<id>[^/]+)$", "POST", self.update_by_id),
            ("^(?P<id>[^/]+)$", "DELETE", self.delete_by_id),
            ("^key=(?P<key>[^/]+)$", "DELETE", self.delete_by_key),
        ]

    _actions = {
        "changeTriggers": update_nested_object_attribute("triggers", "triggers"),
    }
