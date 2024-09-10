import requests


class RunaiError(Exception):
    """Base class for all custom exceptions in the Runai client."""

    pass


class RunaiClientError(RunaiError):
    def __init__(self, err: Exception, message: str):
        out = f"{message}\nError: {err}" if err is not None else f"{message}"
        super().__init__(out)


class RunaiHTTPError(RunaiError):
    def __init__(self, resp=requests.Response):
        self.message = f"[{resp.status_code}] - {resp.text}"
        super().__init__(self.message)


class RunaiBuildModelError(RunaiError):
    def __init__(self, err: Exception, message: str = "Failed to build body scheme"):
        super().__init__(f"{message}: {err}")


class RunaiQueryParamsError(RunaiError):
    def __init__(self, err: Exception, message: str = "Failed to build query parameters"):
        super().__init__(f"{message}: {err}")


class RunaiNotImplementedError(RunaiError):
    def __init__(self, message="Class method not implemented. Please submit a feature request on GitHub"):
        super().__init__(f"{message}")


class RunaiClusterIDNotConfigured(RunaiError):
    """Exception raised when the cluster_id is not configured in the RunaiClient."""

    def __init__(self):
        message = (
            "Client cluster_id is not configured, cannot use endpoints.\n"
            "Run client.config_cluster_id() first or provide cluster_id to RunaiClient()."
        )
        super().__init__(message)
