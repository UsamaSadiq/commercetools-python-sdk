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

# Fields


# Marshmallow Schemas
class GeneralCategoryRecommendationSchema(helpers.BaseSchema):
    category_name = marshmallow.fields.String(
        allow_none=True, load_default=None, data_key="categoryName"
    )
    confidence = marshmallow.fields.Float(allow_none=True, load_default=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return models.GeneralCategoryRecommendation(**data)


class GeneralCategoryRecommendationPagedQueryResponseSchema(helpers.BaseSchema):
    count = marshmallow.fields.Integer(allow_none=True, load_default=None)
    total = marshmallow.fields.Integer(allow_none=True, load_default=None)
    offset = marshmallow.fields.Integer(allow_none=True, load_default=None)
    results = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".GeneralCategoryRecommendationSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        load_default=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return models.GeneralCategoryRecommendationPagedQueryResponse(**data)
