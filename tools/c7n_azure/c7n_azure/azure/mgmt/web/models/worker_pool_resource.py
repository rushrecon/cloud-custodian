# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .proxy_only_resource import ProxyOnlyResource


class WorkerPoolResource(ProxyOnlyResource):
    """Worker pool of an App Service Environment ARM resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource Name.
    :vartype name: str
    :param kind: Kind of resource.
    :type kind: str
    :ivar type: Resource type.
    :vartype type: str
    :param worker_size_id: Worker size ID for referencing this worker pool.
    :type worker_size_id: int
    :param compute_mode: Shared or dedicated app hosting. Possible values
     include: 'Shared', 'Dedicated', 'Dynamic'
    :type compute_mode: str or ~azure.mgmt.web.models.ComputeModeOptions
    :param worker_size: VM size of the worker pool instances.
    :type worker_size: str
    :param worker_count: Number of instances in the worker pool.
    :type worker_count: int
    :ivar instance_names: Names of all instances in the worker pool (read
     only).
    :vartype instance_names: list[str]
    :param sku:
    :type sku: ~azure.mgmt.web.models.SkuDescription
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'instance_names': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'worker_size_id': {'key': 'properties.workerSizeId', 'type': 'int'},
        'compute_mode': {'key': 'properties.computeMode', 'type': 'ComputeModeOptions'},
        'worker_size': {'key': 'properties.workerSize', 'type': 'str'},
        'worker_count': {'key': 'properties.workerCount', 'type': 'int'},
        'instance_names': {'key': 'properties.instanceNames', 'type': '[str]'},
        'sku': {'key': 'sku', 'type': 'SkuDescription'},
    }

    def __init__(self, kind=None, worker_size_id=None, compute_mode=None, worker_size=None, worker_count=None, sku=None):
        super(WorkerPoolResource, self).__init__(kind=kind)
        self.worker_size_id = worker_size_id
        self.compute_mode = compute_mode
        self.worker_size = worker_size
        self.worker_count = worker_count
        self.instance_names = None
        self.sku = sku
