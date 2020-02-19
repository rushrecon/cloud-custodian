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

from .sub_resource_py3 import SubResource


class AzureFirewallNetworkRuleCollection(SubResource):
    """Network rule collection resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param id: Resource ID.
    :type id: str
    :param priority: Priority of the network rule collection resource.
    :type priority: int
    :param action: The action type of a rule collection
    :type action: ~azure.mgmt.network.v2019_02_01.models.AzureFirewallRCAction
    :param rules: Collection of rules used by a network rule collection.
    :type rules:
     list[~azure.mgmt.network.v2019_02_01.models.AzureFirewallNetworkRule]
    :param provisioning_state: The provisioning state of the resource.
     Possible values include: 'Succeeded', 'Updating', 'Deleting', 'Failed'
    :type provisioning_state: str or
     ~azure.mgmt.network.v2019_02_01.models.ProvisioningState
    :param name: Gets name of the resource that is unique within a resource
     group. This name can be used to access the resource.
    :type name: str
    :ivar etag: Gets a unique read-only string that changes whenever the
     resource is updated.
    :vartype etag: str
    """

    _validation = {
        'priority': {'maximum': 65000, 'minimum': 100},
        'etag': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'priority': {'key': 'properties.priority', 'type': 'int'},
        'action': {'key': 'properties.action', 'type': 'AzureFirewallRCAction'},
        'rules': {'key': 'properties.rules', 'type': '[AzureFirewallNetworkRule]'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, *, id: str=None, priority: int=None, action=None, rules=None, provisioning_state=None, name: str=None, **kwargs) -> None:
        super(AzureFirewallNetworkRuleCollection, self).__init__(id=id, **kwargs)
        self.priority = priority
        self.action = action
        self.rules = rules
        self.provisioning_state = provisioning_state
        self.name = name
        self.etag = None
