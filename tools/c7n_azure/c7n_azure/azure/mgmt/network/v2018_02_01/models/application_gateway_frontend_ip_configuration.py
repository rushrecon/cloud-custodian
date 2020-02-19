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


class ApplicationGatewayFrontendIPConfiguration(SubResource):
    """Frontend IP configuration of an application gateway.

    :param id: Resource ID.
    :type id: str
    :param private_ip_address: PrivateIPAddress of the network interface IP
     Configuration.
    :type private_ip_address: str
    :param private_ip_allocation_method: PrivateIP allocation method. Possible
     values include: 'Static', 'Dynamic'
    :type private_ip_allocation_method: str or
     ~azure.mgmt.network.v2018_02_01.models.IPAllocationMethod
    :param subnet: Reference of the subnet resource.
    :type subnet: ~azure.mgmt.network.v2018_02_01.models.SubResource
    :param public_ip_address: Reference of the PublicIP resource.
    :type public_ip_address:
     ~azure.mgmt.network.v2018_02_01.models.SubResource
    :param provisioning_state: Provisioning state of the public IP resource.
     Possible values are: 'Updating', 'Deleting', and 'Failed'.
    :type provisioning_state: str
    :param name: Name of the resource that is unique within a resource group.
     This name can be used to access the resource.
    :type name: str
    :param etag: A unique read-only string that changes whenever the resource
     is updated.
    :type etag: str
    :param type: Type of the resource.
    :type type: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'private_ip_address': {'key': 'properties.privateIPAddress', 'type': 'str'},
        'private_ip_allocation_method': {'key': 'properties.privateIPAllocationMethod', 'type': 'str'},
        'subnet': {'key': 'properties.subnet', 'type': 'SubResource'},
        'public_ip_address': {'key': 'properties.publicIPAddress', 'type': 'SubResource'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ApplicationGatewayFrontendIPConfiguration, self).__init__(**kwargs)
        self.private_ip_address = kwargs.get('private_ip_address', None)
        self.private_ip_allocation_method = kwargs.get('private_ip_allocation_method', None)
        self.subnet = kwargs.get('subnet', None)
        self.public_ip_address = kwargs.get('public_ip_address', None)
        self.provisioning_state = kwargs.get('provisioning_state', None)
        self.name = kwargs.get('name', None)
        self.etag = kwargs.get('etag', None)
        self.type = kwargs.get('type', None)
