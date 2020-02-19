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


class NetworkProfile(Resource):
    """Network profile resource.

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
    :param container_network_interfaces: List of child container network
     interfaces.
    :type container_network_interfaces:
     list[~azure.mgmt.network.v2019_02_01.models.ContainerNetworkInterface]
    :param container_network_interface_configurations: List of chid container
     network interface configurations.
    :type container_network_interface_configurations:
     list[~azure.mgmt.network.v2019_02_01.models.ContainerNetworkInterfaceConfiguration]
    :ivar resource_guid: The resource GUID property of the network interface
     resource.
    :vartype resource_guid: str
    :ivar provisioning_state: The provisioning state of the resource.
    :vartype provisioning_state: str
    :param etag: A unique read-only string that changes whenever the resource
     is updated.
    :type etag: str
    """

    _validation = {
        'name': {'readonly': True},
        'type': {'readonly': True},
        'resource_guid': {'readonly': True},
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'container_network_interfaces': {'key': 'properties.containerNetworkInterfaces', 'type': '[ContainerNetworkInterface]'},
        'container_network_interface_configurations': {'key': 'properties.containerNetworkInterfaceConfigurations', 'type': '[ContainerNetworkInterfaceConfiguration]'},
        'resource_guid': {'key': 'properties.resourceGuid', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(NetworkProfile, self).__init__(**kwargs)
        self.container_network_interfaces = kwargs.get('container_network_interfaces', None)
        self.container_network_interface_configurations = kwargs.get('container_network_interface_configurations', None)
        self.resource_guid = None
        self.provisioning_state = None
        self.etag = kwargs.get('etag', None)
