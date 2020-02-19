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


class VirtualNetworkPeering(SubResource):
    """Peerings in a virtual network resource.

    :param id: Resource ID.
    :type id: str
    :param allow_virtual_network_access: Whether the VMs in the local virtual
     network space would be able to access the VMs in remote virtual network
     space.
    :type allow_virtual_network_access: bool
    :param allow_forwarded_traffic: Whether the forwarded traffic from the VMs
     in the local virtual network will be allowed/disallowed in remote virtual
     network.
    :type allow_forwarded_traffic: bool
    :param allow_gateway_transit: If gateway links can be used in remote
     virtual networking to link to this virtual network.
    :type allow_gateway_transit: bool
    :param use_remote_gateways: If remote gateways can be used on this virtual
     network. If the flag is set to true, and allowGatewayTransit on remote
     peering is also true, virtual network will use gateways of remote virtual
     network for transit. Only one peering can have this flag set to true. This
     flag cannot be set if virtual network already has a gateway.
    :type use_remote_gateways: bool
    :param remote_virtual_network: The reference of the remote virtual
     network. The remote virtual network can be in the same or different region
     (preview). See here to register for the preview and learn more
     (https://docs.microsoft.com/en-us/azure/virtual-network/virtual-network-create-peering).
    :type remote_virtual_network:
     ~azure.mgmt.network.v2019_02_01.models.SubResource
    :param remote_address_space: The reference of the remote virtual network
     address space.
    :type remote_address_space:
     ~azure.mgmt.network.v2019_02_01.models.AddressSpace
    :param peering_state: The status of the virtual network peering. Possible
     values are 'Initiated', 'Connected', and 'Disconnected'. Possible values
     include: 'Initiated', 'Connected', 'Disconnected'
    :type peering_state: str or
     ~azure.mgmt.network.v2019_02_01.models.VirtualNetworkPeeringState
    :param provisioning_state: The provisioning state of the resource.
    :type provisioning_state: str
    :param name: The name of the resource that is unique within a resource
     group. This name can be used to access the resource.
    :type name: str
    :param etag: A unique read-only string that changes whenever the resource
     is updated.
    :type etag: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'allow_virtual_network_access': {'key': 'properties.allowVirtualNetworkAccess', 'type': 'bool'},
        'allow_forwarded_traffic': {'key': 'properties.allowForwardedTraffic', 'type': 'bool'},
        'allow_gateway_transit': {'key': 'properties.allowGatewayTransit', 'type': 'bool'},
        'use_remote_gateways': {'key': 'properties.useRemoteGateways', 'type': 'bool'},
        'remote_virtual_network': {'key': 'properties.remoteVirtualNetwork', 'type': 'SubResource'},
        'remote_address_space': {'key': 'properties.remoteAddressSpace', 'type': 'AddressSpace'},
        'peering_state': {'key': 'properties.peeringState', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, *, id: str=None, allow_virtual_network_access: bool=None, allow_forwarded_traffic: bool=None, allow_gateway_transit: bool=None, use_remote_gateways: bool=None, remote_virtual_network=None, remote_address_space=None, peering_state=None, provisioning_state: str=None, name: str=None, etag: str=None, **kwargs) -> None:
        super(VirtualNetworkPeering, self).__init__(id=id, **kwargs)
        self.allow_virtual_network_access = allow_virtual_network_access
        self.allow_forwarded_traffic = allow_forwarded_traffic
        self.allow_gateway_transit = allow_gateway_transit
        self.use_remote_gateways = use_remote_gateways
        self.remote_virtual_network = remote_virtual_network
        self.remote_address_space = remote_address_space
        self.peering_state = peering_state
        self.provisioning_state = provisioning_state
        self.name = name
        self.etag = etag
