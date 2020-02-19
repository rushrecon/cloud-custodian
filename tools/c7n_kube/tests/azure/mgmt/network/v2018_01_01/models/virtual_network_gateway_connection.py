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


class VirtualNetworkGatewayConnection(Resource):
    """A common class for general resource information.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

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
    :param authorization_key: The authorizationKey.
    :type authorization_key: str
    :param virtual_network_gateway1: Required. The reference to virtual
     network gateway resource.
    :type virtual_network_gateway1:
     ~azure.mgmt.network.v2018_01_01.models.VirtualNetworkGateway
    :param virtual_network_gateway2: The reference to virtual network gateway
     resource.
    :type virtual_network_gateway2:
     ~azure.mgmt.network.v2018_01_01.models.VirtualNetworkGateway
    :param local_network_gateway2: The reference to local network gateway
     resource.
    :type local_network_gateway2:
     ~azure.mgmt.network.v2018_01_01.models.LocalNetworkGateway
    :param connection_type: Required. Gateway connection type. Possible values
     are: 'IPsec','Vnet2Vnet','ExpressRoute', and 'VPNClient. Possible values
     include: 'IPsec', 'Vnet2Vnet', 'ExpressRoute', 'VPNClient'
    :type connection_type: str or
     ~azure.mgmt.network.v2018_01_01.models.VirtualNetworkGatewayConnectionType
    :param routing_weight: The routing weight.
    :type routing_weight: int
    :param shared_key: The IPSec shared key.
    :type shared_key: str
    :ivar connection_status: Virtual network Gateway connection status.
     Possible values are 'Unknown', 'Connecting', 'Connected' and
     'NotConnected'. Possible values include: 'Unknown', 'Connecting',
     'Connected', 'NotConnected'
    :vartype connection_status: str or
     ~azure.mgmt.network.v2018_01_01.models.VirtualNetworkGatewayConnectionStatus
    :ivar tunnel_connection_status: Collection of all tunnels' connection
     health status.
    :vartype tunnel_connection_status:
     list[~azure.mgmt.network.v2018_01_01.models.TunnelConnectionHealth]
    :ivar egress_bytes_transferred: The egress bytes transferred in this
     connection.
    :vartype egress_bytes_transferred: long
    :ivar ingress_bytes_transferred: The ingress bytes transferred in this
     connection.
    :vartype ingress_bytes_transferred: long
    :param peer: The reference to peerings resource.
    :type peer: ~azure.mgmt.network.v2018_01_01.models.SubResource
    :param enable_bgp: EnableBgp flag
    :type enable_bgp: bool
    :param use_policy_based_traffic_selectors: Enable policy-based traffic
     selectors.
    :type use_policy_based_traffic_selectors: bool
    :param ipsec_policies: The IPSec Policies to be considered by this
     connection.
    :type ipsec_policies:
     list[~azure.mgmt.network.v2018_01_01.models.IpsecPolicy]
    :param resource_guid: The resource GUID property of the
     VirtualNetworkGatewayConnection resource.
    :type resource_guid: str
    :ivar provisioning_state: The provisioning state of the
     VirtualNetworkGatewayConnection resource. Possible values are: 'Updating',
     'Deleting', and 'Failed'.
    :vartype provisioning_state: str
    :param etag: Gets a unique read-only string that changes whenever the
     resource is updated.
    :type etag: str
    """

    _validation = {
        'name': {'readonly': True},
        'type': {'readonly': True},
        'virtual_network_gateway1': {'required': True},
        'connection_type': {'required': True},
        'connection_status': {'readonly': True},
        'tunnel_connection_status': {'readonly': True},
        'egress_bytes_transferred': {'readonly': True},
        'ingress_bytes_transferred': {'readonly': True},
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'authorization_key': {'key': 'properties.authorizationKey', 'type': 'str'},
        'virtual_network_gateway1': {'key': 'properties.virtualNetworkGateway1', 'type': 'VirtualNetworkGateway'},
        'virtual_network_gateway2': {'key': 'properties.virtualNetworkGateway2', 'type': 'VirtualNetworkGateway'},
        'local_network_gateway2': {'key': 'properties.localNetworkGateway2', 'type': 'LocalNetworkGateway'},
        'connection_type': {'key': 'properties.connectionType', 'type': 'str'},
        'routing_weight': {'key': 'properties.routingWeight', 'type': 'int'},
        'shared_key': {'key': 'properties.sharedKey', 'type': 'str'},
        'connection_status': {'key': 'properties.connectionStatus', 'type': 'str'},
        'tunnel_connection_status': {'key': 'properties.tunnelConnectionStatus', 'type': '[TunnelConnectionHealth]'},
        'egress_bytes_transferred': {'key': 'properties.egressBytesTransferred', 'type': 'long'},
        'ingress_bytes_transferred': {'key': 'properties.ingressBytesTransferred', 'type': 'long'},
        'peer': {'key': 'properties.peer', 'type': 'SubResource'},
        'enable_bgp': {'key': 'properties.enableBgp', 'type': 'bool'},
        'use_policy_based_traffic_selectors': {'key': 'properties.usePolicyBasedTrafficSelectors', 'type': 'bool'},
        'ipsec_policies': {'key': 'properties.ipsecPolicies', 'type': '[IpsecPolicy]'},
        'resource_guid': {'key': 'properties.resourceGuid', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(VirtualNetworkGatewayConnection, self).__init__(**kwargs)
        self.authorization_key = kwargs.get('authorization_key', None)
        self.virtual_network_gateway1 = kwargs.get('virtual_network_gateway1', None)
        self.virtual_network_gateway2 = kwargs.get('virtual_network_gateway2', None)
        self.local_network_gateway2 = kwargs.get('local_network_gateway2', None)
        self.connection_type = kwargs.get('connection_type', None)
        self.routing_weight = kwargs.get('routing_weight', None)
        self.shared_key = kwargs.get('shared_key', None)
        self.connection_status = None
        self.tunnel_connection_status = None
        self.egress_bytes_transferred = None
        self.ingress_bytes_transferred = None
        self.peer = kwargs.get('peer', None)
        self.enable_bgp = kwargs.get('enable_bgp', None)
        self.use_policy_based_traffic_selectors = kwargs.get('use_policy_based_traffic_selectors', None)
        self.ipsec_policies = kwargs.get('ipsec_policies', None)
        self.resource_guid = kwargs.get('resource_guid', None)
        self.provisioning_state = None
        self.etag = kwargs.get('etag', None)
