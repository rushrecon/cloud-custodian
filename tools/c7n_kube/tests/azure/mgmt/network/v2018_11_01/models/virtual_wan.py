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

from .resource import Resource


class VirtualWAN(Resource):
    """VirtualWAN Resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param id: Resource ID.
    :type id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param location: Resource location.
    :type location: str
    :param tags: Resource tags.
    :type tags: dict[str, str]
    :param disable_vpn_encryption: Vpn encryption to be disabled or not.
    :type disable_vpn_encryption: bool
    :ivar virtual_hubs: List of VirtualHubs in the VirtualWAN.
    :vartype virtual_hubs:
     list[~azure.mgmt.network.v2018_11_01.models.SubResource]
    :ivar vpn_sites:
    :vartype vpn_sites:
     list[~azure.mgmt.network.v2018_11_01.models.SubResource]
    :param security_provider_name: The Security Provider name.
    :type security_provider_name: str
    :param allow_branch_to_branch_traffic: True if branch to branch traffic is
     allowed.
    :type allow_branch_to_branch_traffic: bool
    :param allow_vnet_to_vnet_traffic: True if Vnet to Vnet traffic is
     allowed.
    :type allow_vnet_to_vnet_traffic: bool
    :param office365_local_breakout_category: The office local breakout
     category. Possible values include: 'Optimize', 'OptimizeAndAllow', 'All',
     'None'
    :type office365_local_breakout_category: str or
     ~azure.mgmt.network.v2018_11_01.models.OfficeTrafficCategory
    :param p2_svpn_server_configurations: list of all
     P2SVpnServerConfigurations associated with the virtual wan.
    :type p2_svpn_server_configurations:
     list[~azure.mgmt.network.v2018_11_01.models.P2SVpnServerConfiguration]
    :param provisioning_state: The provisioning state of the resource.
     Possible values include: 'Succeeded', 'Updating', 'Deleting', 'Failed'
    :type provisioning_state: str or
     ~azure.mgmt.network.v2018_11_01.models.ProvisioningState
    :ivar etag: Gets a unique read-only string that changes whenever the
     resource is updated.
    :vartype etag: str
    """

    _validation = {
        'name': {'readonly': True},
        'type': {'readonly': True},
        'virtual_hubs': {'readonly': True},
        'vpn_sites': {'readonly': True},
        'etag': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'disable_vpn_encryption': {'key': 'properties.disableVpnEncryption', 'type': 'bool'},
        'virtual_hubs': {'key': 'properties.virtualHubs', 'type': '[SubResource]'},
        'vpn_sites': {'key': 'properties.vpnSites', 'type': '[SubResource]'},
        'security_provider_name': {'key': 'properties.securityProviderName', 'type': 'str'},
        'allow_branch_to_branch_traffic': {'key': 'properties.allowBranchToBranchTraffic', 'type': 'bool'},
        'allow_vnet_to_vnet_traffic': {'key': 'properties.allowVnetToVnetTraffic', 'type': 'bool'},
        'office365_local_breakout_category': {'key': 'properties.office365LocalBreakoutCategory', 'type': 'str'},
        'p2_svpn_server_configurations': {'key': 'properties.p2SVpnServerConfigurations', 'type': '[P2SVpnServerConfiguration]'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(VirtualWAN, self).__init__(**kwargs)
        self.disable_vpn_encryption = kwargs.get('disable_vpn_encryption', None)
        self.virtual_hubs = None
        self.vpn_sites = None
        self.security_provider_name = kwargs.get('security_provider_name', None)
        self.allow_branch_to_branch_traffic = kwargs.get('allow_branch_to_branch_traffic', None)
        self.allow_vnet_to_vnet_traffic = kwargs.get('allow_vnet_to_vnet_traffic', None)
        self.office365_local_breakout_category = kwargs.get('office365_local_breakout_category', None)
        self.p2_svpn_server_configurations = kwargs.get('p2_svpn_server_configurations', None)
        self.provisioning_state = kwargs.get('provisioning_state', None)
        self.etag = None
