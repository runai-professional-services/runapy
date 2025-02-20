import warnings


class RunaiAPIService:

    def options(self, include_deprecated: bool = False) -> list:
        """
        Return all available methods for the given api service

        include_deprecated (bool): use to also return deprecated methods
        """
        # Get all methods of the class
        methods = [
            attr
            for attr in dir(self)
            if (
                callable(getattr(self, attr, None))
                or isinstance(getattr(type(self), attr, None), property)
            )
            and not attr.startswith("_")
        ]

        if include_deprecated:
            return methods
        else:
            return [
                method
                for method in methods
                # Check for the specific _is_deprecated marker
                if not getattr(getattr(self, method), "_is_deprecated", False)
            ]


def deprecated_message():
    """
    Decorator to mark methods as deprecated. Logs a warning using the instance's logger if available.
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            # Access `self` from the decorated method
            instance = args[0] if args else None

            # Check if `self` has `api_client` and a logger
            if (
                instance
                and hasattr(instance, "_api_client")
                and hasattr(instance._api_client, "logger")
            ):
                logger = instance._api_client.logger
                logger.warning(
                    f"The method {func.__name__} is deprecated and will be removed in a future release. "
                    "Please consider an alternative method or refer to the documentation."
                )
            else:
                # Fallback to a standard warning if logger is unavailable
                warnings.warn(
                    f"The method {func.__name__} is deprecated and will be removed in a future release.",
                    DeprecationWarning,
                    stacklevel=2,
                )

            # Call the original method
            return func(*args, **kwargs)

        wrapper._is_deprecated = True
        return wrapper

    return decorator
