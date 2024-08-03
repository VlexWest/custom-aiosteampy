from .constants import EResult


class SteamError(Exception):
    """All errors related to Steam"""


class EResultError(SteamError):
    """Raised when Steam response data contain `success` field with error code"""

    def __init__(self, msg: str, result: EResult, data=None):
        self.msg = msg
        self.result = result
        self.data = data


class LoginError(SteamError):
    """Raised when a problem with login process occurred"""


class SessionExpired(SteamError):
    """Raised when session is expired, and you need to do login"""


class RateLimitExceeded(SteamError):
    """Raised when Steam decided you were in need of a bit of a rest :)"""


class ResourceNotModified(SteamError):
    """
    Special case when `If-Modified-Since` header included
    in request headers and Steam response with 304 status code
    """
