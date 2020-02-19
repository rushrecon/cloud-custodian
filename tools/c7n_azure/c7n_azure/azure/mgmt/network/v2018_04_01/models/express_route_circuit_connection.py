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


class ExpressRouteCircuitConnection(SubResource):
    """Express Route Circuit Connection in an ExpressRouteCircuitPeering resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param id: Resource ID.
    :type id: str
    :param express_route_circuit_peering: Reference to Express Route Circuit
     Private Peering Resource of the circuit initiating connection.
    :type express_route_circuit_peering:
     ~azure.mgmt.network.v2018_04_01.models.SubResource
    :param peer_express_route_circuit_peering: Reference to Express Route
     Circuit Private Peering Resource of the peered circuit.
    :type peer_express_route_circuit_peering:
     ~azure.mgmt.network.v2018_04_01.models.SubResource
    :param address_prefix: /29 IP address space to carve out Customer
     addresses for tunnels.
    :type address_prefix: str
    :param authorization_key: The authorization key.
    :type authorization_key: str
    :ivar circuit_connection_status: Express Route Circuit Connection State.
     Possible values are: 'Connected' and 'Disconnected'. Possible values
     include: 'Connected', 'Connecting', 'Disconnected'
    :vartype circuit_connection_status: str or
     ~azure.mgmt.network.v2018_04_01.models.CircuitConnectionStatus
    :ivar provisioning_state: Provisioning state of the circuit connection
     resource. Possible values are: 'Succeeded', 'Updating', 'Deleting', and
     'Failed'.
    :vartype provisioning_state: str
    :param name: Gets name of the resource that is unique within a resource
     group. This name can be used to access the resource.
    :type name: str
    :ivar etag: A unique read-only string that changes whenever the resource
     is updated.
    :vartype etag: str
    """

    _validation = {
        'circuit_connection_status': {'readonly': True},
        'provisioning_state': {'readonly': True},
        'etag': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'express_route_circuit_peering': {'key': 'properties.expressRouteCircuitPeering', 'type': 'SubResource'},
        'peer_express_route_circuit_peering': {'key': 'properties.peerExpressRouteCircuitPeering', 'type': 'SubResource'},
        'address_prefix': {'key': 'properties.addressPrefix', 'type': 'str'},
        'authorization_key': {'key': 'properties.authorizationKey', 'type': 'str'},
        'circuit_connection_status': {'key': 'properties.circuitConnectionStatus', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ExpressRouteCircuitConnection, self).__init__(**kwargs)
        self.express_route_circuit_peering = kwargs.get('express_route_circuit_peering', None)
        self.peer_express_route_circuit_peering = kwargs.get('peer_express_route_circuit_peering', None)
        self.address_prefix = kwargs.get('address_prefix', None)
        self.authorization_key = kwargs.get('authorization_key', None)
        self.circuit_connection_status = None
        self.provisioning_state = None
        self.name = kwargs.get('name', None)
        self.etag = None
