import logging
import typing as t

import requests

from apps.cryptocurrency.exceptions import (
    CryptoCompareAPIError,
    InvalidJsonError,
    InvalidResponseError,
)
from apps.cryptocurrency.utils import JsonDict, extract_json

ExchangeRateSymbols = t.List[str]
RequestParams = t.Dict[str, str]


class CryptoCompareAPI:
    """Represents API of CryptoCompare service - https://min-api.cryptocompare.com."""

    BASE_API_URL = "https://min-api.cryptocompare.com/data/pricemulti"

    def __init__(self) -> None:
        pass

    def __repr__(self) -> str:
        cls_name = self.__class__.__name__
        return f"<{cls_name} ({self.__dict__})>"

    def _request_exchange_rates(
        self, request_params: RequestParams
    ) -> requests.Response:
        """Make a request to API with params."""

        response = requests.get(url=self.BASE_API_URL, params=request_params)
        return response

    @staticmethod
    def _convert_to_request_params(
        from_: ExchangeRateSymbols, to_: ExchangeRateSymbols
    ) -> RequestParams:
        """Convert ExchangeRateSymbols to request params."""

        from_str = ",".join(from_)
        to_str = ",".join(to_)
        params = {
            "fsyms": from_str,
            "tsyms": to_str,
        }
        return params

    @staticmethod
    def _parse_response(response: requests.Response) -> t.Optional[JsonDict]:
        """Parse a json response from API and returns json dict object or None.

        Raise CryptoCompareAPIError in case if response status code is not 200.
        """

        if response.status_code == 200:
            try:
                json_dict = extract_json(response)
            except (InvalidResponseError, InvalidJsonError) as e:
                logging.error(e)
                return None
            return json_dict
        raise CryptoCompareAPIError(response.status_code)

    def get_exchange_rates(
        self, from_: ExchangeRateSymbols, to_: ExchangeRateSymbols
    ) -> t.Optional[JsonDict]:
        """Get and return the current price of any cryptocurrency (from_) in any other currency (to_).
        If the crypto does not trade directly into the toSymbol requested, BTC will be used for conversion.

        Return None in case if CryptoCompareAPIError occurs.
        """

        request_params = self._convert_to_request_params(from_, to_)
        response = self._request_exchange_rates(request_params)
        try:
            exchange_rates = self._parse_response(response)
        except CryptoCompareAPIError as e:
            logging.error(e)
            return None
        return exchange_rates
