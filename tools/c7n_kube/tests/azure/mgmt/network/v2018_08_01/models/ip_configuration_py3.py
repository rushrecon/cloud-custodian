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

from .sub_resource_py3 import SubResource


class IPConfiguration(SubResource):
    """IP configuration.

    :param id: Resource ID.
    :type id: str
    :param private_ip_address: The private IP address of the IP configuration.
    :type private_ip_address: str
    :param private_ip_allocation_method: The private IP allocation method.
     Possible values are 'Static' and 'Dynamic'. Possible values include:
     'Static', 'Dynamic'
    :type private_ip_allocation_method: str or
     ~azure.mgmt.network.v2018_08_01.models.IPAllocationMethod
    :param subnet: The reference of the subnet resource.
    :type subnet: ~azure.mgmt.network.v2018_08_01.models.Subnet
    :param public_ip_address: The reference of the public IP resource.
    :type public_ip_address:
     ~azure.mgmt.network.v2018_08_01.models.PublicIPAddress
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
        'private_ip_address': {'key': 'properties.privateIPAddress', 'type': 'str'},
        'private_ip_allocation_method': {'key': 'properties.privateIPAllocationMethod', 'type': 'str'},
        'subnet': {'key': 'properties.subnet', 'type': 'Subnet'},
        'public_ip_address': {'key': 'properties.publicIPAddress', 'type': 'PublicIPAddress'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, *, id: str=None, private_ip_address: str=None, private_ip_allocation_method=None, subnet=None, public_ip_address=None, provisioning_state: str=None, name: str=None, etag: str=None, **kwargs) -> None:
        super(IPConfiguration, self).__init__(id=id, **kwargs)
        self.private_ip_address = private_ip_address
        self.private_ip_allocation_method = private_ip_allocation_method
        self.subnet = subnet
        self.public_ip_address = public_ip_address
        self.provisioning_state = provisioning_state
        self.name = name
        self.etag = etag
