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


class Ipv6ExpressRouteCircuitPeeringConfig(Model):
    """Contains IPv6 peering config.

    :param primary_peer_address_prefix: The primary address prefix.
    :type primary_peer_address_prefix: str
    :param secondary_peer_address_prefix: The secondary address prefix.
    :type secondary_peer_address_prefix: str
    :param microsoft_peering_config: The Microsoft peering configuration.
    :type microsoft_peering_config:
     ~azure.mgmt.network.v2017_06_01.models.ExpressRouteCircuitPeeringConfig
    :param route_filter: The reference of the RouteFilter resource.
    :type route_filter: ~azure.mgmt.network.v2017_06_01.models.RouteFilter
    :param state: The state of peering. Possible values are: 'Disabled' and
     'Enabled'. Possible values include: 'Disabled', 'Enabled'
    :type state: str or
     ~azure.mgmt.network.v2017_06_01.models.ExpressRouteCircuitPeeringState
    """

    _attribute_map = {
        'primary_peer_address_prefix': {'key': 'primaryPeerAddressPrefix', 'type': 'str'},
        'secondary_peer_address_prefix': {'key': 'secondaryPeerAddressPrefix', 'type': 'str'},
        'microsoft_peering_config': {'key': 'microsoftPeeringConfig', 'type': 'ExpressRouteCircuitPeeringConfig'},
        'route_filter': {'key': 'routeFilter', 'type': 'RouteFilter'},
        'state': {'key': 'state', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(Ipv6ExpressRouteCircuitPeeringConfig, self).__init__(**kwargs)
        self.primary_peer_address_prefix = kwargs.get('primary_peer_address_prefix', None)
        self.secondary_peer_address_prefix = kwargs.get('secondary_peer_address_prefix', None)
        self.microsoft_peering_config = kwargs.get('microsoft_peering_config', None)
        self.route_filter = kwargs.get('route_filter', None)
        self.state = kwargs.get('state', None)
