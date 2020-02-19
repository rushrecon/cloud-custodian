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

from msrest.serialization import Model


class TopologyParameters(Model):
    """Parameters that define the representation of topology.

    :param target_resource_group_name: The name of the target resource group
     to perform topology on.
    :type target_resource_group_name: str
    :param target_virtual_network: The reference of the Virtual Network
     resource.
    :type target_virtual_network:
     ~azure.mgmt.network.v2018_08_01.models.SubResource
    :param target_subnet: The reference of the Subnet resource.
    :type target_subnet: ~azure.mgmt.network.v2018_08_01.models.SubResource
    """

    _attribute_map = {
        'target_resource_group_name': {'key': 'targetResourceGroupName', 'type': 'str'},
        'target_virtual_network': {'key': 'targetVirtualNetwork', 'type': 'SubResource'},
        'target_subnet': {'key': 'targetSubnet', 'type': 'SubResource'},
    }

    def __init__(self, *, target_resource_group_name: str=None, target_virtual_network=None, target_subnet=None, **kwargs) -> None:
        super(TopologyParameters, self).__init__(**kwargs)
        self.target_resource_group_name = target_resource_group_name
        self.target_virtual_network = target_virtual_network
        self.target_subnet = target_subnet
