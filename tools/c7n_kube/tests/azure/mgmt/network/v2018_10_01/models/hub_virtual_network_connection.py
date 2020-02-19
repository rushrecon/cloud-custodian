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


class HubVirtualNetworkConnection(SubResource):
    """HubVirtualNetworkConnection Resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param id: Resource ID.
    :type id: str
    :param remote_virtual_network: Reference to the remote virtual network.
    :type remote_virtual_network:
     ~azure.mgmt.network.v2018_10_01.models.SubResource
    :param allow_hub_to_remote_vnet_transit: VirtualHub to RemoteVnet transit
     to enabled or not.
    :type allow_hub_to_remote_vnet_transit: bool
    :param allow_remote_vnet_to_use_hub_vnet_gateways: Allow RemoteVnet to use
     Virtual Hub's gateways.
    :type allow_remote_vnet_to_use_hub_vnet_gateways: bool
    :param enable_internet_security: Enable internet security
    :type enable_internet_security: bool
    :param provisioning_state: The provisioning state of the resource.
     Possible values include: 'Succeeded', 'Updating', 'Deleting', 'Failed'
    :type provisioning_state: str or
     ~azure.mgmt.network.v2018_10_01.models.ProvisioningState
    :param name: The name of the resource that is unique within a resource
     group. This name can be used to access the resource.
    :type name: str
    :ivar etag: Gets a unique read-only string that changes whenever the
     resource is updated.
    :vartype etag: str
    """

    _validation = {
        'etag': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'remote_virtual_network': {'key': 'properties.remoteVirtualNetwork', 'type': 'SubResource'},
        'allow_hub_to_remote_vnet_transit': {'key': 'properties.allowHubToRemoteVnetTransit', 'type': 'bool'},
        'allow_remote_vnet_to_use_hub_vnet_gateways': {'key': 'properties.allowRemoteVnetToUseHubVnetGateways', 'type': 'bool'},
        'enable_internet_security': {'key': 'properties.enableInternetSecurity', 'type': 'bool'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(HubVirtualNetworkConnection, self).__init__(**kwargs)
        self.remote_virtual_network = kwargs.get('remote_virtual_network', None)
        self.allow_hub_to_remote_vnet_transit = kwargs.get('allow_hub_to_remote_vnet_transit', None)
        self.allow_remote_vnet_to_use_hub_vnet_gateways = kwargs.get('allow_remote_vnet_to_use_hub_vnet_gateways', None)
        self.enable_internet_security = kwargs.get('enable_internet_security', None)
        self.provisioning_state = kwargs.get('provisioning_state', None)
        self.name = kwargs.get('name', None)
        self.etag = None
