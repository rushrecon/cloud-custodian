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


class ExpressRouteCrossConnectionPeering(SubResource):
    """Peering in an ExpressRoute Cross Connection resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param id: Resource ID.
    :type id: str
    :param peering_type: The peering type. Possible values include:
     'AzurePublicPeering', 'AzurePrivatePeering', 'MicrosoftPeering'
    :type peering_type: str or
     ~azure.mgmt.network.v2018_12_01.models.ExpressRoutePeeringType
    :param state: The peering state. Possible values include: 'Disabled',
     'Enabled'
    :type state: str or
     ~azure.mgmt.network.v2018_12_01.models.ExpressRoutePeeringState
    :ivar azure_asn: The Azure ASN.
    :vartype azure_asn: int
    :param peer_asn: The peer ASN.
    :type peer_asn: long
    :param primary_peer_address_prefix: The primary address prefix.
    :type primary_peer_address_prefix: str
    :param secondary_peer_address_prefix: The secondary address prefix.
    :type secondary_peer_address_prefix: str
    :ivar primary_azure_port: The primary port.
    :vartype primary_azure_port: str
    :ivar secondary_azure_port: The secondary port.
    :vartype secondary_azure_port: str
    :param shared_key: The shared key.
    :type shared_key: str
    :param vlan_id: The VLAN ID.
    :type vlan_id: int
    :param microsoft_peering_config: The Microsoft peering configuration.
    :type microsoft_peering_config:
     ~azure.mgmt.network.v2018_12_01.models.ExpressRouteCircuitPeeringConfig
    :ivar provisioning_state: Gets the provisioning state of the public IP
     resource. Possible values are: 'Updating', 'Deleting', and 'Failed'.
    :vartype provisioning_state: str
    :param gateway_manager_etag: The GatewayManager Etag.
    :type gateway_manager_etag: str
    :param last_modified_by: Gets whether the provider or the customer last
     modified the peering.
    :type last_modified_by: str
    :param ipv6_peering_config: The IPv6 peering configuration.
    :type ipv6_peering_config:
     ~azure.mgmt.network.v2018_12_01.models.Ipv6ExpressRouteCircuitPeeringConfig
    :param name: Gets name of the resource that is unique within a resource
     group. This name can be used to access the resource.
    :type name: str
    :ivar etag: A unique read-only string that changes whenever the resource
     is updated.
    :vartype etag: str
    """

    _validation = {
        'azure_asn': {'readonly': True},
        'peer_asn': {'maximum': 4294967295, 'minimum': 1},
        'primary_azure_port': {'readonly': True},
        'secondary_azure_port': {'readonly': True},
        'provisioning_state': {'readonly': True},
        'etag': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'peering_type': {'key': 'properties.peeringType', 'type': 'str'},
        'state': {'key': 'properties.state', 'type': 'str'},
        'azure_asn': {'key': 'properties.azureASN', 'type': 'int'},
        'peer_asn': {'key': 'properties.peerASN', 'type': 'long'},
        'primary_peer_address_prefix': {'key': 'properties.primaryPeerAddressPrefix', 'type': 'str'},
        'secondary_peer_address_prefix': {'key': 'properties.secondaryPeerAddressPrefix', 'type': 'str'},
        'primary_azure_port': {'key': 'properties.primaryAzurePort', 'type': 'str'},
        'secondary_azure_port': {'key': 'properties.secondaryAzurePort', 'type': 'str'},
        'shared_key': {'key': 'properties.sharedKey', 'type': 'str'},
        'vlan_id': {'key': 'properties.vlanId', 'type': 'int'},
        'microsoft_peering_config': {'key': 'properties.microsoftPeeringConfig', 'type': 'ExpressRouteCircuitPeeringConfig'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'gateway_manager_etag': {'key': 'properties.gatewayManagerEtag', 'type': 'str'},
        'last_modified_by': {'key': 'properties.lastModifiedBy', 'type': 'str'},
        'ipv6_peering_config': {'key': 'properties.ipv6PeeringConfig', 'type': 'Ipv6ExpressRouteCircuitPeeringConfig'},
        'name': {'key': 'name', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, *, id: str=None, peering_type=None, state=None, peer_asn: int=None, primary_peer_address_prefix: str=None, secondary_peer_address_prefix: str=None, shared_key: str=None, vlan_id: int=None, microsoft_peering_config=None, gateway_manager_etag: str=None, last_modified_by: str=None, ipv6_peering_config=None, name: str=None, **kwargs) -> None:
        super(ExpressRouteCrossConnectionPeering, self).__init__(id=id, **kwargs)
        self.peering_type = peering_type
        self.state = state
        self.azure_asn = None
        self.peer_asn = peer_asn
        self.primary_peer_address_prefix = primary_peer_address_prefix
        self.secondary_peer_address_prefix = secondary_peer_address_prefix
        self.primary_azure_port = None
        self.secondary_azure_port = None
        self.shared_key = shared_key
        self.vlan_id = vlan_id
        self.microsoft_peering_config = microsoft_peering_config
        self.provisioning_state = None
        self.gateway_manager_etag = gateway_manager_etag
        self.last_modified_by = last_modified_by
        self.ipv6_peering_config = ipv6_peering_config
        self.name = name
        self.etag = None
