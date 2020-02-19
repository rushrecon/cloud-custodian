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

from .resource_py3 import Resource


class RouteFilter(Resource):
    """Route Filter Resource.

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
    :param rules: Collection of RouteFilterRules contained within a route
     filter.
    :type rules: list[~azure.mgmt.network.v2018_02_01.models.RouteFilterRule]
    :param peerings: A collection of references to express route circuit
     peerings.
    :type peerings:
     list[~azure.mgmt.network.v2018_02_01.models.ExpressRouteCircuitPeering]
    :ivar provisioning_state: The provisioning state of the resource. Possible
     values are: 'Updating', 'Deleting', 'Succeeded' and 'Failed'.
    :vartype provisioning_state: str
    :ivar etag: Gets a unique read-only string that changes whenever the
     resource is updated.
    :vartype etag: str
    """

    _validation = {
        'name': {'readonly': True},
        'type': {'readonly': True},
        'provisioning_state': {'readonly': True},
        'etag': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'rules': {'key': 'properties.rules', 'type': '[RouteFilterRule]'},
        'peerings': {'key': 'properties.peerings', 'type': '[ExpressRouteCircuitPeering]'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, *, id: str=None, location: str=None, tags=None, rules=None, peerings=None, **kwargs) -> None:
        super(RouteFilter, self).__init__(id=id, location=location, tags=tags, **kwargs)
        self.rules = rules
        self.peerings = peerings
        self.provisioning_state = None
        self.etag = None
