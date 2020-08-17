# DO NOT EDIT! This file is automatically generated
import datetime
import typing

from commercetools.types._abstract import _BaseType
from commercetools.types._shipping_method import ShippingRateTierType

if typing.TYPE_CHECKING:
    from ._message import MessageConfiguration, MessageConfigurationDraft
__all__ = [
    "CartClassificationType",
    "CartScoreType",
    "CartValueType",
    "CartsConfiguration",
    "ExternalOAuth",
    "Project",
    "ProjectChangeCountriesAction",
    "ProjectChangeCountryTaxRateFallbackEnabledAction",
    "ProjectChangeCurrenciesAction",
    "ProjectChangeLanguagesAction",
    "ProjectChangeMessagesConfigurationAction",
    "ProjectChangeMessagesEnabledAction",
    "ProjectChangeNameAction",
    "ProjectSetExternalOAuthAction",
    "ProjectSetShippingRateInputTypeAction",
    "ProjectUpdate",
    "ProjectUpdateAction",
    "ShippingRateInputType",
]


class CartsConfiguration(_BaseType):
    #: Optional :class:`bool` `(Named` ``countryTaxRateFallbackEnabled`` `in Commercetools)`
    country_tax_rate_fallback_enabled: typing.Optional[bool]

    def __init__(
        self, *, country_tax_rate_fallback_enabled: typing.Optional[bool] = None
    ) -> None:
        self.country_tax_rate_fallback_enabled = country_tax_rate_fallback_enabled
        super().__init__()

    def __repr__(self) -> str:
        return "CartsConfiguration(country_tax_rate_fallback_enabled=%r)" % (
            self.country_tax_rate_fallback_enabled,
        )


class ExternalOAuth(_BaseType):
    #: :class:`str`
    url: str
    #: :class:`str` `(Named` ``authorizationHeader`` `in Commercetools)`
    authorization_header: str

    def __init__(self, *, url: str, authorization_header: str) -> None:
        self.url = url
        self.authorization_header = authorization_header
        super().__init__()

    def __repr__(self) -> str:
        return "ExternalOAuth(url=%r, authorization_header=%r)" % (
            self.url,
            self.authorization_header,
        )


class Project(_BaseType):
    #: :class:`int`
    version: int
    #: :class:`str`
    key: str
    #: :class:`str`
    name: str
    #: List of :class:`str`
    countries: typing.List["str"]
    #: List of :class:`str`
    currencies: typing.List["str"]
    #: List of :class:`str`
    languages: typing.List["str"]
    #: :class:`datetime.datetime` `(Named` ``createdAt`` `in Commercetools)`
    created_at: datetime.datetime
    #: Optional :class:`str` `(Named` ``trialUntil`` `in Commercetools)`
    trial_until: typing.Optional[str]
    #: :class:`commercetools.types.MessageConfiguration`
    messages: "MessageConfiguration"
    #: Optional :class:`commercetools.types.ShippingRateInputType` `(Named` ``shippingRateInputType`` `in Commercetools)`
    shipping_rate_input_type: typing.Optional["ShippingRateInputType"]
    #: Optional :class:`commercetools.types.ExternalOAuth` `(Named` ``externalOAuth`` `in Commercetools)`
    external_oauth: typing.Optional["ExternalOAuth"]
    #: :class:`commercetools.types.CartsConfiguration`
    carts: "CartsConfiguration"

    def __init__(
        self,
        *,
        version: int,
        key: str,
        name: str,
        countries: typing.List["str"],
        currencies: typing.List["str"],
        languages: typing.List["str"],
        created_at: datetime.datetime,
        messages: "MessageConfiguration",
        carts: "CartsConfiguration",
        trial_until: typing.Optional[str] = None,
        shipping_rate_input_type: typing.Optional["ShippingRateInputType"] = None,
        external_oauth: typing.Optional["ExternalOAuth"] = None
    ) -> None:
        self.version = version
        self.key = key
        self.name = name
        self.countries = countries
        self.currencies = currencies
        self.languages = languages
        self.created_at = created_at
        self.trial_until = trial_until
        self.messages = messages
        self.shipping_rate_input_type = shipping_rate_input_type
        self.external_oauth = external_oauth
        self.carts = carts
        super().__init__()

    def __repr__(self) -> str:
        return (
            "Project(version=%r, key=%r, name=%r, countries=%r, currencies=%r, languages=%r, created_at=%r, trial_until=%r, messages=%r, shipping_rate_input_type=%r, external_oauth=%r, carts=%r)"
            % (
                self.version,
                self.key,
                self.name,
                self.countries,
                self.currencies,
                self.languages,
                self.created_at,
                self.trial_until,
                self.messages,
                self.shipping_rate_input_type,
                self.external_oauth,
                self.carts,
            )
        )


class ProjectUpdate(_BaseType):
    #: :class:`int`
    version: int
    #: :class:`list`
    actions: list

    def __init__(self, *, version: int, actions: list) -> None:
        self.version = version
        self.actions = actions
        super().__init__()

    def __repr__(self) -> str:
        return "ProjectUpdate(version=%r, actions=%r)" % (self.version, self.actions)


class ProjectUpdateAction(_BaseType):
    #: :class:`str`
    action: str

    def __init__(self, *, action: str) -> None:
        self.action = action
        super().__init__()

    def __repr__(self) -> str:
        return "ProjectUpdateAction(action=%r)" % (self.action,)


class ShippingRateInputType(_BaseType):
    #: :class:`commercetools.types.ShippingRateTierType`
    type: "ShippingRateTierType"

    def __init__(self, *, type: "ShippingRateTierType") -> None:
        self.type = type
        super().__init__()

    def __repr__(self) -> str:
        return "ShippingRateInputType(type=%r)" % (self.type,)


class CartClassificationType(ShippingRateInputType):
    #: :class:`list`
    values: list

    def __init__(self, *, values: list) -> None:
        self.values = values
        super().__init__(type=ShippingRateTierType.CART_CLASSIFICATION)

    def __repr__(self) -> str:
        return "CartClassificationType(type=%r, values=%r)" % (self.type, self.values)


class CartScoreType(ShippingRateInputType):
    def __init__(self) -> None:
        super().__init__(type=ShippingRateTierType.CART_SCORE)

    def __repr__(self) -> str:
        return "CartScoreType(type=%r)" % (self.type,)


class CartValueType(ShippingRateInputType):
    def __init__(self) -> None:
        super().__init__(type=ShippingRateTierType.CART_VALUE)

    def __repr__(self) -> str:
        return "CartValueType(type=%r)" % (self.type,)


class ProjectChangeCountriesAction(ProjectUpdateAction):
    #: List of :class:`str`
    countries: typing.List["str"]

    def __init__(self, *, countries: typing.List["str"]) -> None:
        self.countries = countries
        super().__init__(action="changeCountries")

    def __repr__(self) -> str:
        return "ProjectChangeCountriesAction(action=%r, countries=%r)" % (
            self.action,
            self.countries,
        )


class ProjectChangeCountryTaxRateFallbackEnabledAction(ProjectUpdateAction):
    #: :class:`bool` `(Named` ``countryTaxRateFallbackEnabled`` `in Commercetools)`
    country_tax_rate_fallback_enabled: bool

    def __init__(self, *, country_tax_rate_fallback_enabled: bool) -> None:
        self.country_tax_rate_fallback_enabled = country_tax_rate_fallback_enabled
        super().__init__(action="changeCountryTaxRateFallbackEnabled")

    def __repr__(self) -> str:
        return (
            "ProjectChangeCountryTaxRateFallbackEnabledAction(action=%r, country_tax_rate_fallback_enabled=%r)"
            % (self.action, self.country_tax_rate_fallback_enabled)
        )


class ProjectChangeCurrenciesAction(ProjectUpdateAction):
    #: List of :class:`str`
    currencies: typing.List["str"]

    def __init__(self, *, currencies: typing.List["str"]) -> None:
        self.currencies = currencies
        super().__init__(action="changeCurrencies")

    def __repr__(self) -> str:
        return "ProjectChangeCurrenciesAction(action=%r, currencies=%r)" % (
            self.action,
            self.currencies,
        )


class ProjectChangeLanguagesAction(ProjectUpdateAction):
    #: List of :class:`str`
    languages: typing.List["str"]

    def __init__(self, *, languages: typing.List["str"]) -> None:
        self.languages = languages
        super().__init__(action="changeLanguages")

    def __repr__(self) -> str:
        return "ProjectChangeLanguagesAction(action=%r, languages=%r)" % (
            self.action,
            self.languages,
        )


class ProjectChangeMessagesConfigurationAction(ProjectUpdateAction):
    #: :class:`commercetools.types.MessageConfigurationDraft` `(Named` ``messagesConfiguration`` `in Commercetools)`
    messages_configuration: "MessageConfigurationDraft"

    def __init__(self, *, messages_configuration: "MessageConfigurationDraft") -> None:
        self.messages_configuration = messages_configuration
        super().__init__(action="changeMessagesConfiguration")

    def __repr__(self) -> str:
        return (
            "ProjectChangeMessagesConfigurationAction(action=%r, messages_configuration=%r)"
            % (self.action, self.messages_configuration)
        )


class ProjectChangeMessagesEnabledAction(ProjectUpdateAction):
    #: :class:`bool` `(Named` ``messagesEnabled`` `in Commercetools)`
    messages_enabled: bool

    def __init__(self, *, messages_enabled: bool) -> None:
        self.messages_enabled = messages_enabled
        super().__init__(action="changeMessagesEnabled")

    def __repr__(self) -> str:
        return "ProjectChangeMessagesEnabledAction(action=%r, messages_enabled=%r)" % (
            self.action,
            self.messages_enabled,
        )


class ProjectChangeNameAction(ProjectUpdateAction):
    #: :class:`str`
    name: str

    def __init__(self, *, name: str) -> None:
        self.name = name
        super().__init__(action="changeName")

    def __repr__(self) -> str:
        return "ProjectChangeNameAction(action=%r, name=%r)" % (self.action, self.name)


class ProjectSetExternalOAuthAction(ProjectUpdateAction):
    #: Optional :class:`commercetools.types.ExternalOAuth` `(Named` ``externalOAuth`` `in Commercetools)`
    external_oauth: typing.Optional["ExternalOAuth"]

    def __init__(
        self, *, external_oauth: typing.Optional["ExternalOAuth"] = None
    ) -> None:
        self.external_oauth = external_oauth
        super().__init__(action="setExternalOAuth")

    def __repr__(self) -> str:
        return "ProjectSetExternalOAuthAction(action=%r, external_oauth=%r)" % (
            self.action,
            self.external_oauth,
        )


class ProjectSetShippingRateInputTypeAction(ProjectUpdateAction):
    #: Optional :class:`commercetools.types.ShippingRateInputType` `(Named` ``shippingRateInputType`` `in Commercetools)`
    shipping_rate_input_type: typing.Optional["ShippingRateInputType"]

    def __init__(
        self,
        *,
        shipping_rate_input_type: typing.Optional["ShippingRateInputType"] = None
    ) -> None:
        self.shipping_rate_input_type = shipping_rate_input_type
        super().__init__(action="setShippingRateInputType")

    def __repr__(self) -> str:
        return (
            "ProjectSetShippingRateInputTypeAction(action=%r, shipping_rate_input_type=%r)"
            % (self.action, self.shipping_rate_input_type)
        )
