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

from .sub_resource import SubResource


class Delegation(SubResource):
    """Details the service to which the subnet is delegated.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param id: Resource ID.
    :type id: str
    :param service_name: The name of the service to whom the subnet should be
     delegated (e.g. Microsoft.Sql/servers)
    :type service_name: str
    :param actions: Describes the actions permitted to the service upon
     delegation
    :type actions: list[str]
    :ivar provisioning_state: The provisioning state of the resource.
    :vartype provisioning_state: str
    :param name: The name of the resource that is unique within a subnet. This
     name can be used to access the resource.
    :type name: str
    :param etag: A unique read-only string that changes whenever the resource
     is updated.
    :type etag: str
    """

    _validation = {
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'service_name': {'key': 'properties.serviceName', 'type': 'str'},
        'actions': {'key': 'properties.actions', 'type': '[str]'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(Delegation, self).__init__(**kwargs)
        self.service_name = kwargs.get('service_name', None)
        self.actions = kwargs.get('actions', None)
        self.provisioning_state = None
        self.name = kwargs.get('name', None)
        self.etag = kwargs.get('etag', None)
