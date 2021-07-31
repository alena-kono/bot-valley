from core.exceptions import BaseProjectException


class InvalidJsonError(BaseProjectException):
    """Exception is raised when Response object contains invalid
    json or does not contain any.
    """

    def __init__(self) -> None:
        msg = "Response object contains invalid json"
        super().__init__(msg)


class InvalidResponseError(BaseProjectException):
    """Exception is raised when object is not an instance of
    a class <requests.Response>.
    """

    pass


class CryptoCompareAPIError(BaseProjectException):
    """Exception is raised when CryptoCompareAPI is not available."""

    def __init__(self, *args: object) -> None:
        msg = "CryptoCompareAPI service is not available at the moment."
        super().__init__(msg, *args)
