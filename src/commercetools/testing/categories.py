import datetime
import typing
import uuid

from commercetools.platform import models
from commercetools.platform.models._schemas.category import (
    CategoryDraftSchema,
    CategoryPagedQueryResponseSchema,
    CategorySchema,
    CategoryUpdateSchema,
)
from commercetools.testing import utils
from commercetools.testing.abstract import BaseModel, ServiceBackend


class CategoriesModel(BaseModel):
    _primary_type_name = "category"
    _resource_schema = CategorySchema
    _unique_values = ["key"]

    def _create_from_draft(
        self, draft: models.CategoryDraft, id: typing.Optional[str] = None
    ) -> models.Category:
        object_id = str(uuid.UUID(id) if id is not None else uuid.uuid4())
        return models.Category(
            id=str(object_id),
            version=1,
            name=draft.name,
            description=draft.description,
            slug=draft.slug,
            key=draft.key,
            created_at=datetime.datetime.now(datetime.timezone.utc),
            last_modified_at=datetime.datetime.now(datetime.timezone.utc),
            ancestors=[],
            order_hint=draft.order_hint,
            custom=utils.create_from_draft(draft.custom),
            parent=draft.parent,
        )


class CategoriesBackend(ServiceBackend):
    service_path = "categories"
    model_class = CategoriesModel
    _schema_draft = CategoryDraftSchema
    _schema_update = CategoryUpdateSchema
    _schema_query_response = CategoryPagedQueryResponseSchema

    def urls(self):
        return [
            ("^$", "GET", self.query),
            ("^$", "POST", self.create),
            ("^key=(?P<key>[^/]+)$", "GET", self.get_by_key),
            ("^key=(?P<key>[^/]+)$", "POST", self.update_by_key),
            ("^key=(?P<key>[^/]+)$", "DELETE", self.delete_by_key),
            ("^(?P<id>[^/]+)$", "GET", self.get_by_id),
            ("^(?P<id>[^/]+)$", "POST", self.update_by_id),
            ("^(?P<id>[^/]+)$", "DELETE", self.delete_by_id),
        ]

    _actions = {
        "setDescription": utils.update_attribute("description", "description"),
    }
