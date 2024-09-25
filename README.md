# runapy
Run:ai platform streamlines AI workload orchestration, enabling organizations to efficiently manage and scale their machine learning tasks while optimizing resource utilization.

This project provides a Python client SDK to interact with the [Run:ai REST API](https://app.run.ai/api/docs).

 Core Capabilities:
- A single class interface to perform all API actions
- Body schema validation on compilation (with Pydantic)
- Static type checks
- Retry mechanism for resiliency on intermittent network errors
- Debug messages flag
- Automatic API token refresh

## Table of Contents

1. [Requirements](#requirements)
2. [Installation](#installation)
3. [Client Usage](#client-usage)
4. [Controllers](#controllers)
5. [Examples](#examples)
6. [Using CLIv2 Token](#using-cliv2-token)
7. [Warranty](#warranty)
8. [License](#license)

## Requirements
- **Run:ai control-plane version >= 2.18:** The SDK requires Run:ai control-plane version 2.18 or higher for compatibility with its API features
- **Python version >= 3.11:** Compatibility with libraries and language features
- **Run:ai Client Application:** A client application is needed to generate the `client_id` and `client_secret` credentials required for API access. [Create a client application here.](https://docs.run.ai/v2.18/developer/rest-auth/#create-a-client-application)


 #### Note on token and permissions
Ensure the application token has the required role and scope permissions for the necessary API actions. Some API calls may fail with a 403 error if the token lacks sufficient permissions.

## Installation

runapy is available in PyPi and can be downloaded directly as a python package
```bash
pip3 install runapy
```
We recommend using a Python virtual environment to avoid package conflicts.

```bash
python3 -m venv myenv
source myenv/bin/activate
pip3 install runapy
```
## Client

`RunaiClient` is the only class required to interact with the [Run:ai REST API](https://app.run.ai/api/docs)

```python
from runai.client import RunaiClient

client = RunaiClient(
            client_id="API",
            client_secret="clientsecret",
            runai_base_url="https://myorg.run.ai",
            cluster_id="513423qx-127t-4yk6-979g-5po843g37e2b",
            retries=3,
    )
```
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `client_id`      | `string` | **Required**: The Run:ai application client ID, usually representing the application name |
| `client_secret`      | `string` | **Required**: The client secret associated with the Run:ai application, acting as a password |
| `runai_base_url`      | `string` | **Required**: The base URL for the Run:ai instance your organization uses. Example: `https://myorg.run.ai`|
| `bearer_token`      | `string` | **Optional**: The API bearer token. Used for CLIv2 compatibility |
| `retries`      | `int` | **Optional**: Number of retries to attempt on each failed API call for 5xx errors. Default is 1 |
| `cluster_id`      | `string` | **Optional**: The ID of the cluster. Default is None|
| `debug`      | `bool` | **Optional**: Debug mode output. Default is False |

If you don't have the  `cluster_id`, it can be obtained with:
```python
clusters = client.clusters.all()
for cluster in clusters:
    cluster_id = cluster["uuid"]
```
**Note** - If you have more than one cluster, make sure to save the ids to `cluster_ids_list`, and select the relevant `cluster_id`

Then, configure the client with the cluster id:
```python
client.config_cluster_id(cluster["uuid"])
```
**Note** - The `cluster_id` must be present in order to use endpoints that have `cluster_id` required in payload according to [Run:ai REST API](https://app.run.ai/api/docs).\
So make sure to configure the cluster_id before using them.
## Note on Controllers
The RunaiClient exposes object controllers, which provide a convenient way to interact with specific resources on the Run:ai
platform.
For example, to access projects:
```python
from runai.client import RunaiClient

client = RunaiClient(
            client_id="API",
            client_secret="clientsecret",
            runai_base_url="https://myorg.run.ai",
            cluster_id="513423qx-127t-4yk6-979g-5po843g37e2b",
            retries=3,
    )

client.projects.all()
```
`client.projects.all()` returns a list of all projects in a given cluster according to the cluster id of the RunaiClient.

Currently supported controllers:
```python
client.projects
client.node_pools
client.departments
client.access_rules
client.roles
client.users

client.workloads
client.workspace
client.training
client.inference
client.distributed

client.assets.pvc
client.assets.s3
client.assets.git
client.assets.nfs
client.assets.credentials.access_key
client.assets.credentials.password
client.assets.credentials.docker_registry_secret
```
Each controller exposes the function `options()` so you can see which methods are currently availalble for a given controller.\
For example:
```python
client.roles.options()
-> 
['all', 'get', 'get_roles_name_to_id_map']
```

Controller methods are documented.\
Hover on the method parentheses to see the required and optional fields to pass to the function.

## Examples

Check the examples section [here](examples/) for common API interactions, such as:


- Create, list, patch projects/departments resources in a cluster
- Create Nvidia nim llama inference workload
- Create, Delete, Stop and Resume training and interactive workloads
- Creating and modifying access rules and user roles
- Managing PVC, S3, NFS, Git Run:ai assets
- And more

Feel free to copy and run them as is, modify them as needed, or use them as a reference.

## CLIv2 token
CLIv2 is Run:ai’s command-line interface version 2, which allows users to authenticate via the `runai login` command.\
The package supports making API calls with the same user entity defined in the authentication.json file, generated by `runai login`.\
Before executing the code below, ensure that CLIv2 is installed, `runai login` has been executed, and a successful login has been completed.\

You can run the following code to authenticate with the CLI user:
```python
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
```
The example is also documented [here](examples/with_cliv2_token.py) with added instructions.

## Warranty
This package is an open-source project maintained by the Run:ai Professional Services team.\
While it is not an official project of the Run:ai product, it is actively maintained with a commitment to continued development.

In the future, the project is planned to become community-driven, inviting contributions and collaboration from users and the broader open-source community.

If you experience any issues or have feature requests, please submit them via the [repository’s issue tracker](https://github.com/runai-professional-services/runapy/issues). \
Your feedback is highly appreciated and will help guide the project's future direction.

## License
This project is licensed under the MIT License. 
See the LICENSE file for details.
