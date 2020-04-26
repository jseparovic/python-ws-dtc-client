

class ClientError(Exception):
    """Base class for exceptions in this module."""

    def __init__(self, message):
        super(ClientError, self).__init__(message)


class InvalidArgumentsError(ClientError):
    def __init__(self, message="Invalid Arguments Error"):
        super(ClientError, self).__init__(message)


class LogonError(ClientError):
    def __init__(self, message="Logon Error"):
        super(ClientError, self).__init__(message)


class MethodNotAllowedError(ClientError):
    def __init__(self, message="Method Not Allowed Error"):
        super(ClientError, self).__init__(message)


class ResponseTimeoutError(ClientError):
    def __init__(self, message="Timed out waiting for a response."):
        super(ClientError, self).__init__(message)


