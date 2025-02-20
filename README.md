# Runapy

Python client for the [Run:ai REST API](https://app.run.ai/api/docs).

- A single class interface to perform all Run:ai REST API actions
- Automatic API token refresh, useful for long-running tasks
- Built-in retry mechanism for handling transient network errors
- Runtime data validation and serialization using Pydantic models

```python
from runai.configuration import Configuration
from runai.api_client import ApiClient
from runai.runai_client import RunaiClient

config = Configuration(
    client_id="your-client-id",
    client_secret="your-client-secret",
    runai_base_url="https://your-org.run.ai",
)

client = RunaiClient(ApiClient(config))

# Start making API calls
projects = client.organizations.projects.get_projects()
```

Jump to our [examples](examples/) section for more detailed examples.

## Table of Contents

1. [Requirements](#requirements)
2. [Installation](#installation)
3. [Getting Started](#getting-started)
4. [API Structure](#api-structure)
5. [Client Configuration Options](#client-configuration-options)
6. [Authentication Methods](#authentication-methods)
7. [Examples](#examples)
8. [Versioning](#versioning)
9. [About](#about)
10. [License](#license)

## Requirements
* **Run:ai control-plane version >= 2.18:** The client requires Run:ai control-plane version 2.18 or higher
* **Python version >= 3.8:** Required for compatibility with core dependencies
* **Run:ai Client Application:** Required to generate the `client_id` and `client_secret` credentials. [Create a client application](https://docs.run.ai/latest/developer/rest-auth/#create-a-client-application)

#### Note on Token Permissions
Ensure your application token has the required role and scope permissions for your intended API operations. \
API calls will fail with a 403 error if the token lacks sufficient role or scope.

## Installation

For SaaS environments or latest Run:ai control-plane:
```bash
pip3 install runapy
```

For self-hosted environments, specify the minor version matching your control-plane version. \
For example, with Run:ai 2.19 control-plane:
```bash
pip3 install runapy~=1.219.0
```
To understand the versioning scheme, refer to the [Versioning](#versioning) section.

## Getting Started

The client provides three client types to suit different use cases:

1. `ApiClient`: Standard synchronous client for sequential operations
2. `ThreadedApiClient`: Thread-safe client for parallel operations in multithreaded environments
3. `AsyncApiClient`: Asynchronous client for `async/await` support

Here's a basic example using the standard client:

```python
from runai.configuration import Configuration
from runai.api_client import ApiClient
from runai.runai_client import RunaiClient

config = Configuration(
    client_id="your-client-id",
    client_secret="your-client-secret",
    runai_base_url="https://your-org.run.ai",
)

client = RunaiClient(ApiClient(config))

# Start making API calls
projects = client.organizations.projects.get_projects()
```
See all client configuration options in the [Client configuration options](#client-configuration-options)

See [Examples](#examples) for quickstart guides

### Multithreaded Operations
For parallel operations in a multithreaded environment, use `ThreadedApiClient`:

```python
from runai.api_client import ThreadedApiClient

with RunaiClient(ThreadedApiClient(config)) as client:
    # These operations can run concurrently
    projects = client.organizations.projects.get_projects()
```

### Asynchronous Operations
For async/await support, use `AsyncApiClient`:

```python
import asyncio
from runai.api_client import AsyncApiClient

async def main():
    async with RunaiClient(AsyncApiClient(config)) as client:
        projects = await client.organizations.projects.get_projects()

asyncio.run(main())
```

## API Structure

The client matches the Run:ai REST API documentation structure with three levels of groups:

1. **API Categories**: Top-level groupings (e.g., `organizations`, `authentication_and_authorization`)
2. **API Groups**: Resource-specific groups within categories (e.g., `projects`, `departments` under `organizations`)
3. **API Methods**: Individual operations on resources (e.g., `get_projects`, `create_project`)

Example of navigating the API structure:

```python
# List available API groups in the organizations category
client.organizations.options()
# ['projects', 'departments', 'clusters', 'nodes', ...]

# List available methods in the projects group
client.organizations.projects.options()
# ['get_projects', 'create_project', 'delete_project', ...]
```

### Deprecated Methods
Deprecated methods are hidden by default. \
To view both supported and deprecated methods, use the `include_deprecated` flag:
```python
client.organizations.projects.options(include_deprecated=True)
```

## Client Configuration Options

| Parameter | Type | Description |
| :-------- | :------- | :-------------------------------- |
| `client_id` | `string` | **Required**: The Run:ai application client ID, usually representing the application name |
| `client_secret` | `string` | **Required**: The client secret associated with the Run:ai application |
| `runai_base_url` | `string` | **Required**: The base URL for the Run:ai instance your organization uses (e.g., `https://myorg.run.ai`) |
| `bearer_token` | `string` | **Optional**: Bearer token for CLIv2 compatibility. Cannot be used together with client credentials |
| `verify_ssl` | `bool` | **Optional**: Whether to verify SSL certificates. Default is `True` |
| `ssl_ca_cert` | `string` | **Optional**: Path to CA certificate file |
| `cert_file` | `string` | **Optional**: Path to client certificate file |
| `key_file` | `string` | **Optional**: Path to client key file |
| `pool_maxsize` | `int` | **Optional**: Maximum number of connections to keep in pool. Default is `4` |
| `pool_size` | `int` | **Optional**: Initial number of connections in pool. Defaults to `pool_maxsize` |
| `retry_enabled` | `bool` | **Optional**: Whether to enable request retries. Default is `True` |
| `retry_max_retries` | `int` | **Optional**: Maximum number of retry attempts. Default is `3` |
| `retry_backoff_factor` | `float` | **Optional**: Exponential backoff factor between retries. Default is `0.5` |
| `proxy_url` | `string` | **Optional**: URL for proxy server |
| `proxy_headers` | `dict` | **Optional**: Additional headers for proxy |
| `proxy_server_name` | `string` | **Optional**: SNI hostname for TLS connections |
| `auto_refresh_token` | `bool` | **Optional**: Whether to auto refresh token before expiry. Default is `True` |
| `token_refresh_margin` | `int` | **Optional**: Seconds before expiry to refresh token. Default is `60` |
| `debug` | `bool` | **Optional**: Enable debug logging. Default is `False` |

## Authentication Methods

The client supports three authentication methods:

### 1. Client Credentials
Use client ID and secret from your Run:ai application:
```python
config = Configuration(
    client_id="your-client-id",
    client_secret="your-client-secret",
    runai_base_url="https://your-org.run.ai"
)
```

### 2. Bearer Token
Direct authentication using a bearer token:
```python
config = Configuration(
    bearer_token="your-bearer-token",
    runai_base_url="https://your-org.run.ai"
)
```

### 3. CLIv2 Token (Bearer token)
The CLIv2 token method is useful for:
* Local development and testing
* Scripts running on machines with existing CLI authentication
* Maintaining consistent authentication with CLI sessions
* End user operations

Requirements:
* Run:ai CLI v2 installed
* Successful `runai login` completed
* Valid authentication token in CLI config

```python
from runai.cliv2_config_loader import CLIv2Config

# Default config path is ~/.runai
config = CLIv2Config()
# Or specify a custom path
config = CLIv2Config(cliv2_config_path="/path/to/.runai")

token = config.token
runai_base_url = config.control_plane_url
cluster_id = config.cluster_uuid

client = RunaiClient(
    cluster_id=cluster_id,
    bearer_token=token,
    runai_base_url=runai_base_url
)
```

## Examples

The repo provides Hand-crafted examples showing common use cases.\
See [here](examples/).

The API client include APIs for all Run:ai UI functionalities.\
We encourage you to explore the client relevant categories if you attempt to run a task that is not shown in the examples.

Note: There are also auto-generated examples under /examples/generated (may require syntax adjustments to run properly)
## Versioning
The Run:ai API is an integral part of the control-plane microservices.\
As the control-plane evolves, APIs may be added, modified, or deprecated.\
This version binding ensures that API changes in the client match the control-plane capabilities.

The client follows semantic versioning (X.Y.Z) with a special alignment to Run:ai's control-plane versions:

* **X (Major)**: Major changes in the client
* **Y (Minor)**: Run:ai control-plane version (e.g., 219 for control-plane 2.19)
* **Z (Patch)**: Small bug fixes and non-breaking changes

For example:
```
1.218.0  # Initial release for control-plane 2.18
1.218.1  # Patch release for control-plane 2.18
1.219.0  # Initial release for control-plane 2.19
```

This versioning convention ensures that:
1. Each control-plane version has a matching client version
2. Client versions clearly indicate their compatible control-plane version
3. Client breaking changes are managed in major version bumps

## About
This package is an open-source project maintained by the Run:ai Professional Services team.\
If you experience any issues or have feature requests, please submit them via the [repository’s issue tracker](https://github.com/runai-professional-services/runapy/issues).

## License
This project is licensed under the Apache-2 License. \
See the LICENSE file for details.
