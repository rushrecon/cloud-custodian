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


class Subnet(SubResource):
    """Subnet in a virtual network resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param id: Resource ID.
    :type id: str
    :param address_prefix: The address prefix for the subnet.
    :type address_prefix: str
    :param address_prefixes: List of  address prefixes for the subnet.
    :type address_prefixes: list[str]
    :param network_security_group: The reference of the NetworkSecurityGroup
     resource.
    :type network_security_group:
     ~azure.mgmt.network.v2018_12_01.models.NetworkSecurityGroup
    :param route_table: The reference of the RouteTable resource.
    :type route_table: ~azure.mgmt.network.v2018_12_01.models.RouteTable
    :param service_endpoints: An array of service endpoints.
    :type service_endpoints:
     list[~azure.mgmt.network.v2018_12_01.models.ServiceEndpointPropertiesFormat]
    :param service_endpoint_policies: An array of service endpoint policies.
    :type service_endpoint_policies:
     list[~azure.mgmt.network.v2018_12_01.models.ServiceEndpointPolicy]
    :ivar interface_endpoints: An array of references to interface endpoints
    :vartype interface_endpoints:
     list[~azure.mgmt.network.v2018_12_01.models.InterfaceEndpoint]
    :ivar ip_configurations: Gets an array of references to the network
     interface IP configurations using subnet.
    :vartype ip_configurations:
     list[~azure.mgmt.network.v2018_12_01.models.IPConfiguration]
    :ivar ip_configuration_profiles: Array of IP configuration profiles which
     reference this subnet.
    :vartype ip_configuration_profiles:
     list[~azure.mgmt.network.v2018_12_01.models.IPConfigurationProfile]
    :param resource_navigation_links: Gets an array of references to the
     external resources using subnet.
    :type resource_navigation_links:
     list[~azure.mgmt.network.v2018_12_01.models.ResourceNavigationLink]
    :param service_association_links: Gets an array of references to services
     injecting into this subnet.
    :type service_association_links:
     list[~azure.mgmt.network.v2018_12_01.models.ServiceAssociationLink]
    :param delegations: Gets an array of references to the delegations on the
     subnet.
    :type delegations: list[~azure.mgmt.network.v2018_12_01.models.Delegation]
    :ivar purpose: A read-only string identifying the intention of use for
     this subnet based on delegations and other user-defined properties.
    :vartype purpose: str
    :param provisioning_state: The provisioning state of the resource.
    :type provisioning_state: str
    :param name: The name of the resource that is unique within a resource
     group. This name can be used to access the resource.
    :type name: str
    :param etag: A unique read-only string that changes whenever the resource
     is updated.
    :type etag: str
    """

    _validation = {
        'interface_endpoints': {'readonly': True},
        'ip_configurations': {'readonly': True},
        'ip_configuration_profiles': {'readonly': True},
        'purpose': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'address_prefix': {'key': 'properties.addressPrefix', 'type': 'str'},
        'address_prefixes': {'key': 'properties.addressPrefixes', 'type': '[str]'},
        'network_security_group': {'key': 'properties.networkSecurityGroup', 'type': 'NetworkSecurityGroup'},
        'route_table': {'key': 'properties.routeTable', 'type': 'RouteTable'},
        'service_endpoints': {'key': 'properties.serviceEndpoints', 'type': '[ServiceEndpointPropertiesFormat]'},
        'service_endpoint_policies': {'key': 'properties.serviceEndpointPolicies', 'type': '[ServiceEndpointPolicy]'},
        'interface_endpoints': {'key': 'properties.interfaceEndpoints', 'type': '[InterfaceEndpoint]'},
        'ip_configurations': {'key': 'properties.ipConfigurations', 'type': '[IPConfiguration]'},
        'ip_configuration_profiles': {'key': 'properties.ipConfigurationProfiles', 'type': '[IPConfigurationProfile]'},
        'resource_navigation_links': {'key': 'properties.resourceNavigationLinks', 'type': '[ResourceNavigationLink]'},
        'service_association_links': {'key': 'properties.serviceAssociationLinks', 'type': '[ServiceAssociationLink]'},
        'delegations': {'key': 'properties.delegations', 'type': '[Delegation]'},
        'purpose': {'key': 'properties.purpose', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(Subnet, self).__init__(**kwargs)
        self.address_prefix = kwargs.get('address_prefix', None)
        self.address_prefixes = kwargs.get('address_prefixes', None)
        self.network_security_group = kwargs.get('network_security_group', None)
        self.route_table = kwargs.get('route_table', None)
        self.service_endpoints = kwargs.get('service_endpoints', None)
        self.service_endpoint_policies = kwargs.get('service_endpoint_policies', None)
        self.interface_endpoints = None
        self.ip_configurations = None
        self.ip_configuration_profiles = None
        self.resource_navigation_links = kwargs.get('resource_navigation_links', None)
        self.service_association_links = kwargs.get('service_association_links', None)
        self.delegations = kwargs.get('delegations', None)
        self.purpose = None
        self.provisioning_state = kwargs.get('provisioning_state', None)
        self.name = kwargs.get('name', None)
        self.etag = kwargs.get('etag', None)
