import json
import base64
from pathlib import Path


class CLIv2Config:
    def __init__(self, cliv2_config_path: str) -> None:
        """
        Initializes the loader for CLIv2 configuration.

        :param cliv2_config_path: Path to the directory containing CLIv2 config files. CLIv2Config("/path/to/.runai")\n
                                  Make sure the path dir contains both authentication.json and config.json
        """
        self.cliv2_dir = Path(cliv2_config_path)
        if not self.cliv2_dir.is_dir():
            raise ValueError(
                f"Invalid path to Run:ai CLIv2 configuration: {cliv2_config_path}"
            )

        self.auth_file_path = self.cliv2_dir / "authentication.json"
        self.config_file_path = self.cliv2_dir / "config.json"

        self.token = (None,)
        self.cluster_uuid = (None,)
        self.control_plane_url = (None,)

    def load(self) -> None:
        """
        Load and parse both authentication.json and config.json files.
        Raises an error if any required field is missing.
        """
        encoded_token = self._load_json_fields(self.auth_file_path, ["accessToken"])[
            "accessToken"
        ]
        self.token = self._decode_base64_token(encoded_token)

        config_data = self._load_json(self.config_file_path)
        self.cluster_uuid = config_data["cluster"]["uuid"]
        self.control_plane_url = config_data["control_plane"]["url"]

    def _load_json_fields(self, file_path: Path, field_names: list):
        """
        Load specific fields from a JSON file.

        :param file_path: The path to the JSON file.
        :param field_names: A list of fields to extract from the JSON data.
        :return: A dictionary containing the requested fields.
        :raises ValueError: If any of the fields are missing or the file cannot be read.
        """
        data = self._load_json(file_path)
        result = {}
        for field_name in field_names:
            if field_name not in data:
                raise ValueError(f"Field '{field_name}' not found in {file_path}")
            result[field_name] = data[field_name]
        return result

    def _load_json(self, file_path: Path):
        """
        Load and parse a JSON file.

        :param file_path: The path to the JSON file.
        :return: The parsed JSON data.
        :raises FileNotFoundError: If the file cannot be found.
        :raises JSONDecodeError: If the file is not valid JSON.
        """
        try:
            with open(file_path, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {file_path}")
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON format in {file_path}")

    def _decode_base64_token(self, token: str) -> str:
        """
        Decode a Base64 encoded token and return the decoded string.

        :param token: Base64 encoded access token.
        :return: Decoded access token string.
        :raises ValueError: If the token is not valid Base64.
        """
        try:
            decoded_bytes = base64.urlsafe_b64decode(
                token + "=="
            )  # Ensure proper padding for Base64
            return decoded_bytes.decode("utf-8")
        except (base64.binascii.Error, UnicodeDecodeError):
            raise ValueError("Invalid Base64 encoded token")
