# coding: utf-8

"""
Runai API

# Introduction  The Run:AI Control-Plane API reference is a guide that provides an easy-to-use programming interface for adding various tasks to your application, including workload submission, resource management, and administrative operations.  Run:ai APIs are accessed using *bearer tokens*. To obtain a token, you need to create an **Application** through the Run:ai user interface. To create an application, in your UI, go to `Settings & Tools`, `Application` and create a new Application.  After you have created a new application, you will need to assign it access rules. To assign access rules to the application, see [Create access rules](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#create-or-delete-rules). Make sure you assign the correct rules to your application. Use the [Roles](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#roles) to assign the correct access rules.  To get your access token, follow the instructions in [Request a token](https://docs.run.ai/latest/developer/rest-auth/#request-an-api-token).

The version of the OpenAPI document: 2.0.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class NodeMetricType(str, Enum):
    """
    Specify which metric data to request.

    Allowed enum values:

    GPU_UTILIZATION_PER_GPU = 'GPU_UTILIZATION_PER_GPU'

    GPU_UTILIZATION = 'GPU_UTILIZATION'

    GPU_MEMORY_UTILIZATION_PER_GPU = 'GPU_MEMORY_UTILIZATION_PER_GPU'

    GPU_MEMORY_UTILIZATION = 'GPU_MEMORY_UTILIZATION'

    GPU_MEMORY_USAGE_BYTES_PER_GPU = 'GPU_MEMORY_USAGE_BYTES_PER_GPU'

    GPU_MEMORY_USAGE_BYTES = 'GPU_MEMORY_USAGE_BYTES'

    CPU_USAGE_CORES = 'CPU_USAGE_CORES'

    CPU_UTILIZATION = 'CPU_UTILIZATION'

    CPU_MEMORY_USAGE_BYTES = 'CPU_MEMORY_USAGE_BYTES'

    CPU_MEMORY_UTILIZATION = 'CPU_MEMORY_UTILIZATION'

    GPU_OOMKILL_BURST_COUNT_PER_GPU = 'GPU_OOMKILL_BURST_COUNT_PER_GPU'

    GPU_OOMKILL_IDLE_COUNT_PER_GPU = 'GPU_OOMKILL_IDLE_COUNT_PER_GPU'

    GPU_OOMKILL_SWAP_OUT_OF_RAM_COUNT_PER_GPU = 'GPU_OOMKILL_SWAP_OUT_OF_RAM_COUNT_PER_GPU'


    Example:
        ```python
        NodeMetricType.GPU_UTILIZATION_PER_GPU
        NodeMetricType.GPU_UTILIZATION
        NodeMetricType.GPU_MEMORY_UTILIZATION_PER_GPU
        NodeMetricType.GPU_MEMORY_UTILIZATION
        NodeMetricType.GPU_MEMORY_USAGE_BYTES_PER_GPU
        NodeMetricType.GPU_MEMORY_USAGE_BYTES
        NodeMetricType.CPU_USAGE_CORES
        NodeMetricType.CPU_UTILIZATION
        NodeMetricType.CPU_MEMORY_USAGE_BYTES
        NodeMetricType.CPU_MEMORY_UTILIZATION
        NodeMetricType.GPU_OOMKILL_BURST_COUNT_PER_GPU
        NodeMetricType.GPU_OOMKILL_IDLE_COUNT_PER_GPU
        NodeMetricType.GPU_OOMKILL_SWAP_OUT_OF_RAM_COUNT_PER_GPU
        ```
    """

    GPU_UTILIZATION_PER_GPU = "GPU_UTILIZATION_PER_GPU"
    GPU_UTILIZATION = "GPU_UTILIZATION"
    GPU_MEMORY_UTILIZATION_PER_GPU = "GPU_MEMORY_UTILIZATION_PER_GPU"
    GPU_MEMORY_UTILIZATION = "GPU_MEMORY_UTILIZATION"
    GPU_MEMORY_USAGE_BYTES_PER_GPU = "GPU_MEMORY_USAGE_BYTES_PER_GPU"
    GPU_MEMORY_USAGE_BYTES = "GPU_MEMORY_USAGE_BYTES"
    CPU_USAGE_CORES = "CPU_USAGE_CORES"
    CPU_UTILIZATION = "CPU_UTILIZATION"
    CPU_MEMORY_USAGE_BYTES = "CPU_MEMORY_USAGE_BYTES"
    CPU_MEMORY_UTILIZATION = "CPU_MEMORY_UTILIZATION"
    GPU_OOMKILL_BURST_COUNT_PER_GPU = "GPU_OOMKILL_BURST_COUNT_PER_GPU"
    GPU_OOMKILL_IDLE_COUNT_PER_GPU = "GPU_OOMKILL_IDLE_COUNT_PER_GPU"
    GPU_OOMKILL_SWAP_OUT_OF_RAM_COUNT_PER_GPU = (
        "GPU_OOMKILL_SWAP_OUT_OF_RAM_COUNT_PER_GPU"
    )

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of NodeMetricType from a JSON string"""
        return cls(json.loads(json_str))
