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


class ExpressRouteCircuitPeering(SubResource):
    """Peering in an ExpressRouteCircuit resource.

    :param id: Resource Identifier.
    :type id: str
    :param peering_type: The PeeringType. Possible values are:
     'AzurePublicPeering', 'AzurePrivatePeering', and 'MicrosoftPeering'.
     Possible values include: 'AzurePublicPeering', 'AzurePrivatePeering',
     'MicrosoftPeering'
    :type peering_type: str or
     ~azure.mgmt.network.v2015_06_15.models.ExpressRouteCircuitPeeringType
    :param state: The state of peering. Possible values are: 'Disabled' and
     'Enabled'. Possible values include: 'Disabled', 'Enabled'
    :type state: str or
     ~azure.mgmt.network.v2015_06_15.models.ExpressRouteCircuitPeeringState
    :param azure_asn: The Azure ASN.
    :type azure_asn: int
    :param peer_asn: The peer ASN.
    :type peer_asn: int
    :param primary_peer_address_prefix: The primary address prefix.
    :type primary_peer_address_prefix: str
    :param secondary_peer_address_prefix: The secondary address prefix.
    :type secondary_peer_address_prefix: str
    :param primary_azure_port: The primary port.
    :type primary_azure_port: str
    :param secondary_azure_port: The secondary port.
    :type secondary_azure_port: str
    :param shared_key: The shared key.
    :type shared_key: str
    :param vlan_id: The VLAN ID.
    :type vlan_id: int
    :param microsoft_peering_config: The Microsoft peering configuration.
    :type microsoft_peering_config:
     ~azure.mgmt.network.v2015_06_15.models.ExpressRouteCircuitPeeringConfig
    :param stats: Gets peering stats.
    :type stats:
     ~azure.mgmt.network.v2015_06_15.models.ExpressRouteCircuitStats
    :param provisioning_state: Gets the provisioning state of the public IP
     resource. Possible values are: 'Updating', 'Deleting', and 'Failed'.
    :type provisioning_state: str
    :param name: Gets name of the resource that is unique within a resource
     group. This name can be used to access the resource.
    :type name: str
    :param etag: A unique read-only string that changes whenever the resource
     is updated.
    :type etag: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'peering_type': {'key': 'properties.peeringType', 'type': 'str'},
        'state': {'key': 'properties.state', 'type': 'str'},
        'azure_asn': {'key': 'properties.azureASN', 'type': 'int'},
        'peer_asn': {'key': 'properties.peerASN', 'type': 'int'},
        'primary_peer_address_prefix': {'key': 'properties.primaryPeerAddressPrefix', 'type': 'str'},
        'secondary_peer_address_prefix': {'key': 'properties.secondaryPeerAddressPrefix', 'type': 'str'},
        'primary_azure_port': {'key': 'properties.primaryAzurePort', 'type': 'str'},
        'secondary_azure_port': {'key': 'properties.secondaryAzurePort', 'type': 'str'},
        'shared_key': {'key': 'properties.sharedKey', 'type': 'str'},
        'vlan_id': {'key': 'properties.vlanId', 'type': 'int'},
        'microsoft_peering_config': {'key': 'properties.microsoftPeeringConfig', 'type': 'ExpressRouteCircuitPeeringConfig'},
        'stats': {'key': 'properties.stats', 'type': 'ExpressRouteCircuitStats'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ExpressRouteCircuitPeering, self).__init__(**kwargs)
        self.peering_type = kwargs.get('peering_type', None)
        self.state = kwargs.get('state', None)
        self.azure_asn = kwargs.get('azure_asn', None)
        self.peer_asn = kwargs.get('peer_asn', None)
        self.primary_peer_address_prefix = kwargs.get('primary_peer_address_prefix', None)
        self.secondary_peer_address_prefix = kwargs.get('secondary_peer_address_prefix', None)
        self.primary_azure_port = kwargs.get('primary_azure_port', None)
        self.secondary_azure_port = kwargs.get('secondary_azure_port', None)
        self.shared_key = kwargs.get('shared_key', None)
        self.vlan_id = kwargs.get('vlan_id', None)
        self.microsoft_peering_config = kwargs.get('microsoft_peering_config', None)
        self.stats = kwargs.get('stats', None)
        self.provisioning_state = kwargs.get('provisioning_state', None)
        self.name = kwargs.get('name', None)
        self.etag = kwargs.get('etag', None)
