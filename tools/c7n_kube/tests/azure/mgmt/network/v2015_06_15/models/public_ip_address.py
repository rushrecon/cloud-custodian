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


class PublicIPAddress(Resource):
    """Public IP address resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param id: Resource Identifier.
    :type id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param location: Resource location.
    :type location: str
    :param tags: Resource tags.
    :type tags: dict[str, str]
    :param public_ip_allocation_method: The public IP allocation method.
     Possible values are: 'Static' and 'Dynamic'. Possible values include:
     'Static', 'Dynamic'
    :type public_ip_allocation_method: str or
     ~azure.mgmt.network.v2015_06_15.models.IPAllocationMethod
    :param ip_configuration:
    :type ip_configuration:
     ~azure.mgmt.network.v2015_06_15.models.IPConfiguration
    :param dns_settings: The FQDN of the DNS record associated with the public
     IP address.
    :type dns_settings:
     ~azure.mgmt.network.v2015_06_15.models.PublicIPAddressDnsSettings
    :param ip_address:
    :type ip_address: str
    :param idle_timeout_in_minutes: The idle timeout of the public IP address.
    :type idle_timeout_in_minutes: int
    :param resource_guid: The resource GUID property of the public IP
     resource.
    :type resource_guid: str
    :param provisioning_state: The provisioning state of the PublicIP
     resource. Possible values are: 'Updating', 'Deleting', and 'Failed'.
    :type provisioning_state: str
    :param etag: A unique read-only string that changes whenever the resource
     is updated.
    :type etag: str
    """

    _validation = {
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'public_ip_allocation_method': {'key': 'properties.publicIPAllocationMethod', 'type': 'str'},
        'ip_configuration': {'key': 'properties.ipConfiguration', 'type': 'IPConfiguration'},
        'dns_settings': {'key': 'properties.dnsSettings', 'type': 'PublicIPAddressDnsSettings'},
        'ip_address': {'key': 'properties.ipAddress', 'type': 'str'},
        'idle_timeout_in_minutes': {'key': 'properties.idleTimeoutInMinutes', 'type': 'int'},
        'resource_guid': {'key': 'properties.resourceGuid', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(PublicIPAddress, self).__init__(**kwargs)
        self.public_ip_allocation_method = kwargs.get('public_ip_allocation_method', None)
        self.ip_configuration = kwargs.get('ip_configuration', None)
        self.dns_settings = kwargs.get('dns_settings', None)
        self.ip_address = kwargs.get('ip_address', None)
        self.idle_timeout_in_minutes = kwargs.get('idle_timeout_in_minutes', None)
        self.resource_guid = kwargs.get('resource_guid', None)
        self.provisioning_state = kwargs.get('provisioning_state', None)
        self.etag = kwargs.get('etag', None)
