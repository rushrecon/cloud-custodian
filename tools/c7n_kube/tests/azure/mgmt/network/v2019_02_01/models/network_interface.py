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


class NetworkInterface(Resource):
    """A network interface in a resource group.

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
    :ivar virtual_machine: The reference of a virtual machine.
    :vartype virtual_machine:
     ~azure.mgmt.network.v2019_02_01.models.SubResource
    :param network_security_group: The reference of the NetworkSecurityGroup
     resource.
    :type network_security_group:
     ~azure.mgmt.network.v2019_02_01.models.NetworkSecurityGroup
    :ivar interface_endpoint: A reference to the interface endpoint to which
     the network interface is linked.
    :vartype interface_endpoint:
     ~azure.mgmt.network.v2019_02_01.models.InterfaceEndpoint
    :param ip_configurations: A list of IPConfigurations of the network
     interface.
    :type ip_configurations:
     list[~azure.mgmt.network.v2019_02_01.models.NetworkInterfaceIPConfiguration]
    :param tap_configurations: A list of TapConfigurations of the network
     interface.
    :type tap_configurations:
     list[~azure.mgmt.network.v2019_02_01.models.NetworkInterfaceTapConfiguration]
    :param dns_settings: The DNS settings in network interface.
    :type dns_settings:
     ~azure.mgmt.network.v2019_02_01.models.NetworkInterfaceDnsSettings
    :param mac_address: The MAC address of the network interface.
    :type mac_address: str
    :param primary: Gets whether this is a primary network interface on a
     virtual machine.
    :type primary: bool
    :param enable_accelerated_networking: If the network interface is
     accelerated networking enabled.
    :type enable_accelerated_networking: bool
    :param enable_ip_forwarding: Indicates whether IP forwarding is enabled on
     this network interface.
    :type enable_ip_forwarding: bool
    :ivar hosted_workloads: A list of references to linked BareMetal resources
    :vartype hosted_workloads: list[str]
    :param resource_guid: The resource GUID property of the network interface
     resource.
    :type resource_guid: str
    :param provisioning_state: The provisioning state of the public IP
     resource. Possible values are: 'Updating', 'Deleting', and 'Failed'.
    :type provisioning_state: str
    :param etag: A unique read-only string that changes whenever the resource
     is updated.
    :type etag: str
    """

    _validation = {
        'name': {'readonly': True},
        'type': {'readonly': True},
        'virtual_machine': {'readonly': True},
        'interface_endpoint': {'readonly': True},
        'hosted_workloads': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'virtual_machine': {'key': 'properties.virtualMachine', 'type': 'SubResource'},
        'network_security_group': {'key': 'properties.networkSecurityGroup', 'type': 'NetworkSecurityGroup'},
        'interface_endpoint': {'key': 'properties.interfaceEndpoint', 'type': 'InterfaceEndpoint'},
        'ip_configurations': {'key': 'properties.ipConfigurations', 'type': '[NetworkInterfaceIPConfiguration]'},
        'tap_configurations': {'key': 'properties.tapConfigurations', 'type': '[NetworkInterfaceTapConfiguration]'},
        'dns_settings': {'key': 'properties.dnsSettings', 'type': 'NetworkInterfaceDnsSettings'},
        'mac_address': {'key': 'properties.macAddress', 'type': 'str'},
        'primary': {'key': 'properties.primary', 'type': 'bool'},
        'enable_accelerated_networking': {'key': 'properties.enableAcceleratedNetworking', 'type': 'bool'},
        'enable_ip_forwarding': {'key': 'properties.enableIPForwarding', 'type': 'bool'},
        'hosted_workloads': {'key': 'properties.hostedWorkloads', 'type': '[str]'},
        'resource_guid': {'key': 'properties.resourceGuid', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(NetworkInterface, self).__init__(**kwargs)
        self.virtual_machine = None
        self.network_security_group = kwargs.get('network_security_group', None)
        self.interface_endpoint = None
        self.ip_configurations = kwargs.get('ip_configurations', None)
        self.tap_configurations = kwargs.get('tap_configurations', None)
        self.dns_settings = kwargs.get('dns_settings', None)
        self.mac_address = kwargs.get('mac_address', None)
        self.primary = kwargs.get('primary', None)
        self.enable_accelerated_networking = kwargs.get('enable_accelerated_networking', None)
        self.enable_ip_forwarding = kwargs.get('enable_ip_forwarding', None)
        self.hosted_workloads = None
        self.resource_guid = kwargs.get('resource_guid', None)
        self.provisioning_state = kwargs.get('provisioning_state', None)
        self.etag = kwargs.get('etag', None)
