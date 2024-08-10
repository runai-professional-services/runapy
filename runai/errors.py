import requests


class RunaiError(Exception):
    """Base class for all custom exceptions in the Runai client."""

    pass


class RunaiClientError(RunaiError):
    def __init__(self, err: Exception, message: str):
        super().__init__(f"{message}\nError: {err}")


class RunaiHTTPError(RunaiError):
    def __init__(self, resp=requests.Response):
        self.message = f"[{resp.status_code}] - {resp.text}"
        super().__init__(self.message)


class RunaiBuildModelError(RunaiError):
    def __init__(self,
                 err: Exception,
                 message: str = "Failed to build body scheme"):
        super().__init__(f"{message}: {err}")


class RunaiQueryParamsError(RunaiError):
    def __init__(self,
                 err: Exception,
                 message: str = "Failed to build query parameters"):
        super().__init__(f"{message}: {err}")


class RunaiNotImplementedError(RunaiError):
    def __init__(self, message="Class method is not supported"):
        super().__init__(f"{message}")
