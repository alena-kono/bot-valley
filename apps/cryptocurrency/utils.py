import json
import typing as t

import requests

from apps.cryptocurrency.exceptions import InvalidJsonError, InvalidResponseError

JsonDict = t.Dict[str, t.Any]


def extract_json(response: requests.Response) -> JsonDict:
    if not isinstance(response, requests.Response):
        raise InvalidResponseError(
            "response should be an instance of a class <requests.Response>,",
            f"not {type(response)}",
        )
    try:
        extracted_json = response.json()
    except json.decoder.JSONDecodeError:
        raise InvalidJsonError()
    return extracted_json
