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


class FrontendIPConfiguration(SubResource):
    """Frontend IP address of the load balancer.

    :param id: Resource Identifier.
    :type id: str
    :param inbound_nat_rules: Read only. Inbound rules URIs that use this
     frontend IP.
    :type inbound_nat_rules:
     list[~azure.mgmt.network.v2015_06_15.models.SubResource]
    :param inbound_nat_pools: Read only. Inbound pools URIs that use this
     frontend IP.
    :type inbound_nat_pools:
     list[~azure.mgmt.network.v2015_06_15.models.SubResource]
    :param outbound_nat_rules: Read only. Outbound rules URIs that use this
     frontend IP.
    :type outbound_nat_rules:
     list[~azure.mgmt.network.v2015_06_15.models.SubResource]
    :param load_balancing_rules: Gets load balancing rules URIs that use this
     frontend IP.
    :type load_balancing_rules:
     list[~azure.mgmt.network.v2015_06_15.models.SubResource]
    :param private_ip_address: The private IP address of the IP configuration.
    :type private_ip_address: str
    :param private_ip_allocation_method: The Private IP allocation method.
     Possible values are: 'Static' and 'Dynamic'. Possible values include:
     'Static', 'Dynamic'
    :type private_ip_allocation_method: str or
     ~azure.mgmt.network.v2015_06_15.models.IPAllocationMethod
    :param subnet: The reference of the subnet resource.
    :type subnet: ~azure.mgmt.network.v2015_06_15.models.Subnet
    :param public_ip_address: The reference of the Public IP resource.
    :type public_ip_address:
     ~azure.mgmt.network.v2015_06_15.models.PublicIPAddress
    :param provisioning_state: Gets the provisioning state of the public IP
     resource. Possible values are: 'Updating', 'Deleting', and 'Failed'.
    :type provisioning_state: str
    :param name: The name of the resource that is unique within a resource
     group. This name can be used to access the resource.
    :type name: str
    :param etag: A unique read-only string that changes whenever the resource
     is updated.
    :type etag: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'inbound_nat_rules': {'key': 'properties.inboundNatRules', 'type': '[SubResource]'},
        'inbound_nat_pools': {'key': 'properties.inboundNatPools', 'type': '[SubResource]'},
        'outbound_nat_rules': {'key': 'properties.outboundNatRules', 'type': '[SubResource]'},
        'load_balancing_rules': {'key': 'properties.loadBalancingRules', 'type': '[SubResource]'},
        'private_ip_address': {'key': 'properties.privateIPAddress', 'type': 'str'},
        'private_ip_allocation_method': {'key': 'properties.privateIPAllocationMethod', 'type': 'str'},
        'subnet': {'key': 'properties.subnet', 'type': 'Subnet'},
        'public_ip_address': {'key': 'properties.publicIPAddress', 'type': 'PublicIPAddress'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(FrontendIPConfiguration, self).__init__(**kwargs)
        self.inbound_nat_rules = kwargs.get('inbound_nat_rules', None)
        self.inbound_nat_pools = kwargs.get('inbound_nat_pools', None)
        self.outbound_nat_rules = kwargs.get('outbound_nat_rules', None)
        self.load_balancing_rules = kwargs.get('load_balancing_rules', None)
        self.private_ip_address = kwargs.get('private_ip_address', None)
        self.private_ip_allocation_method = kwargs.get('private_ip_allocation_method', None)
        self.subnet = kwargs.get('subnet', None)
        self.public_ip_address = kwargs.get('public_ip_address', None)
        self.provisioning_state = kwargs.get('provisioning_state', None)
        self.name = kwargs.get('name', None)
        self.etag = kwargs.get('etag', None)
