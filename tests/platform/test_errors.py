from commercetools.platform import models
from commercetools.platform.client import Client as PlatformClient
from commercetools.platform.models import (
    ErrorResponse,
    ExtensionNoResponseError,
    QueryTimedOutError,
)
from commercetools.platform.models._schemas.error import ErrorResponseSchema


def test_raises_exception(ct_platform_client: PlatformClient):
    channel = (
        ct_platform_client.with_project_key("foo")
        .channels()
        .post(
            models.ChannelDraft(
                key="test-channel2", roles=[models.ChannelRoleEnum.INVENTORY_SUPPLY]
            )
        )
    )

    result = (
        ct_platform_client.with_project_key("foo")
        .channels()
        .with_id(channel.id)
        .post(
            models.ChannelUpdate(
                version=4,
                actions=[
                    models.ChannelSetRolesAction(roles=[models.ChannelRoleEnum.PRIMARY])
                ],
            ),
            options={"force_version": True},
        )
    )

    result = (
        ct_platform_client.with_project_key("foo")
        .channels()
        .with_id(channel.id)
        .delete(version=1, options={"force_version": True})
    )


def test_extension_no_response_error():
    error_response = {
        "errors": [
            {
                "code": "ExtensionNoResponse",
                "extensionId": "eff671fb-d6e9-4fac-85b3-0b39af542762",
                "extensionKey": "create-cart",
                "message": "Extension did not respond in time.",
            }
        ],
        "message": "Extension did not respond in time.",
        "statusCode": 504,
    }

    obj = ErrorResponse.deserialize(error_response)
    error = obj.errors[0]

    assert isinstance(error, ExtensionNoResponseError)
    assert error.extension_id == "eff671fb-d6e9-4fac-85b3-0b39af542762"
    assert error.extension_key == "create-cart"


def test_query_timeout_error():
    error_response = {
        "errors": [{"code": "QueryTimedOut", "message": "The query timed out."}],
        "message": "The query timed out.",
        "statusCode": 400,
    }
    obj = ErrorResponse.deserialize(error_response)
    error = obj.errors[0]

    assert isinstance(error, QueryTimedOutError)


def test_error_response_serialize():
    data = ErrorResponseSchema().dump(
        models.ErrorResponse(
            status_code=409,
            message="Version mismatch. Concurrent modification.",
            errors=[
                models.ConcurrentModificationError(
                    message="Version mismatch. Concurrent modification.",
                    somethingElse="yes",
                    current_version=4,
                )
            ],
        )
    )
    expected = {
        "statusCode": 409,
        "message": "Version mismatch. Concurrent modification.",
        "errors": [
            {
                "currentVersion": 4,
                "code": "ConcurrentModification",
                "somethingElse": "yes",
                "message": "Version mismatch. Concurrent modification.",
            }
        ],
    }
    assert data == expected


def test_error_response_deserialize():
    data = ErrorResponseSchema().load(
        {
            "statusCode": 409,
            "message": "Version mismatch. Concurrent modification.",
            "errors": [
                {
                    "currentVersion": 4,
                    "code": "ConcurrentModification",
                    "message": "Version mismatch. Concurrent modification.",
                    "somethingElse": "yes",
                }
            ],
        }
    )
    assert data.errors[0].somethingElse == "yes"
