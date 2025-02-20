import base64
import json
import datetime
from threading import Lock


class TokenRefresher:

    def __init__(self, api_client_instance: object) -> None:
        self._api_client_instance = api_client_instance
        self.configuration = self._api_client_instance.configuration
        self._token_refresh_thread_lock = Lock()
        self._token_refresh_thread_is_locked = False
        self._set_token_expiry()

    def _set_token_expiry(self) -> None:
        token_payload = self._api_client_instance._token.split(".")[1]
        token_payload_decoded = json.loads(base64.b64decode(token_payload + "=="))
        self._token_expiry = token_payload_decoded.get("exp", 0)
        if not self._token_expiry:
            raise ValueError("Token payload does not contain 'exp' claim")

    def _is_token_about_to_expire(self) -> bool:
        if not self._api_client_instance._token:
            return True  # If no token is set, treat it as expired
        current_time = datetime.datetime.now(datetime.timezone.utc)
        self._api_client_instance.logger.debug(
            f"Token expires at: {datetime.datetime.fromtimestamp(timestamp=self._token_expiry, tz=datetime.timezone.utc)} and current time is: {current_time}"
        )
        # return true if token has 60 seconds (defined in token_refresh_margin) or less until expiry
        current_time_timestamp = current_time.timestamp()
        return (
            self._token_expiry - current_time_timestamp
            <= self.configuration.token_refresh_margin
        )

    def _refresh_token(self):
        with self._token_refresh_thread_lock:
            self._token_refresh_thread_is_locked = True
            token = self._api_client_instance._make_token_request()
            self._api_client_instance._token = token
            self._set_token_expiry()
            self._api_client_instance.set_default_header(
                "authorization", f"Bearer {self._api_client_instance._token}"
            )
            self._api_client_instance.logger.debug("API token refreshed successfully.")
            self._token_refresh_thread_is_locked = False

    def _check_token_expired(self):
        if self._is_token_about_to_expire():
            self._api_client_instance.logger.debug("Need to refresh token")
            if self._token_refresh_thread_is_locked is not True:
                self._refresh_token()
            else:
                self._api_client_instance.logger.debug(
                    "Another thread is already refreshing the token, skipping refresh"
                )
        else:
            self._api_client_instance.logger.debug(
                "Token is in expiration time range, Skipping refresh"
            )
