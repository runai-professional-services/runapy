import requests


class RunaiError(Exception):
    """Base class for all custom exceptions in the Runai client."""
    pass


class RunaiClientError(RunaiError):
    pass


class RunaiHTTPError(RunaiError):
    def __init__(self, resp=requests.Response):
        self.message = f"[{resp.status_code}] - {resp.text}"
        super().__init__(self.message)


class RunaiBuildModelError(RunaiError):
    def __init__(self, err, message="Failed to build model"):
        super().__init__(f"{message}: {err}")


class RunaiNotImplementedError(RunaiError):
    pass
