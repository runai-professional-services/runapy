"""
Example usage of `RunaiClient` with `CLIv2Config`.
The script will load configuration values and authenticate wtih the same CLI user credentials against the Run:ai API.

This example demonstrates how to:
1. Load the CLIv2 configuration from a specified path.
2. Retrieve essential authentication and configuration values:
   - `accessToken` from the authentication.json.
   - `cluster_uuid` and `control_plane_url` from the config.json.
3. Use the loaded values to initialize a `RunaiClient`, which will perform API actions on behalf of the user's .

Note:
Make sure you are logged in to the CLIv2 with the your user `runai login`
Ensure to replace `"/path/to/.runai"` with the actual path to your `.runai` configuration directory, typically located in your home directory.
"""

from runai.client import RunaiClient
from runai.cliv2_config_loader import CLIv2Config

config = CLIv2Config(cliv2_config_path="/path/to/.runai")

config.load()

token = config.token
runai_base_url = config.control_plane_url
cluster_id = config.cluster_uuid

client = RunaiClient(
    cluster_id=cluster_id,
    bearer_token=token,
    runai_base_url=runai_base_url
)
