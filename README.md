# runapy

This project provides a Python client SDK to interact with the [Run:ai REST API](https://app.run.ai/api/docs).

 The client offers:
- A single class interface to perform all API actions
- Body schema validation on compilation (with Pydantic)
- Static type checks
- Retry mechanism for resiliency on intermittent network errors
- Debug messages flag

## Requirements
- **Run:ai control-plane version 2.18 and above:** Required for compatibility with the SDK.
- **Python 3.11 and above:** Ensures compatibility with the latest Python features and libraries.
- **Run:ai Client Application:** A client application is needed to generate the credentials required for API access. [Create a client application here.](https://docs.run.ai/v2.18/developer/rest-auth/#create-a-client-application)


 #### Note on token and permissions
When creating an application, it is important to select the relevant role and scope for the required API actions.\
Some API calls may fail with 403 if the application token does not have sufficient permissions.

## Installation

runapy is available in PyPi and can be downloaded directly as a python package
```bash
pip3 install runapy
```
It's recommended to install `runapy` in a virtual environment to avoid conflicts with other packages.

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
            realm="myorgrealm",
            client_id="API",
            client_secret="clientsecret",
            runai_base_url="https://myorg.run.ai",
            cluster_id="513423qx-127t-4yk6-979g-5po843g37e2b",
            retries=3,
            debug=False
    )
```
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `realm`      | `string` | **Required**: Can be obtained from the UI login screen at your Run:ai domain app.run.ai -> app.run.ai/auth/realms/<realm>|
| `client_id`      | `string` | **Required**: The Run:ai application client ID, usually representing the application name |
| `client_secret`      | `string` | **Required**: The client secret associated with the Run:ai application, acting as a password |
| `runai_base_url`      | `string` | **Required**: The base URL for the Run:ai instance your organization uses. Example: `https://myorg.run.ai`|
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
The `RunaiClient` exposes object controllers for all API endpoints.
For example, to access projects:
```python
from runai.client import RunaiClient

client = RunaiClient(
            realm="myorgrealm",
            client_id="API",
            client_secret="clientsecret",
            runai_base_url="https://myorg.run.ai",
            cluster_id="513423qx-127t-4yk6-979g-5po843g37e2b",
            retries=3,
            debug=False
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

For more practical examples, check the existing examples [here](examples/):
- How to create, list, patch projects/departments resources in a cluster
- Creating and managing workloads
- Accessing and modifying user roles
- Managing PVC, S3, NFS, Git assets

Feel free to copy and run them as is, modify them as needed, or use them as a reference.


## Warranty
This package is not maintained by the Run:ai product team.

For any issues and requests, please open an issue, or contact the authors of this package.

## License
This project is licensed under the MIT License. 
See the LICENSE file for details.
