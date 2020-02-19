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


class NatGateway(Resource):
    """Nat Gateway resource.

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
    :param sku: The nat gateway SKU.
    :type sku: ~azure.mgmt.network.v2019_02_01.models.NatGatewaySku
    :param idle_timeout_in_minutes: The idle timeout of the nat gateway.
    :type idle_timeout_in_minutes: int
    :param public_ip_addresses: An array of public ip addresses associated
     with the nat gateway resource.
    :type public_ip_addresses:
     list[~azure.mgmt.network.v2019_02_01.models.SubResource]
    :param public_ip_prefixes: An array of public ip prefixes associated with
     the nat gateway resource.
    :type public_ip_prefixes:
     list[~azure.mgmt.network.v2019_02_01.models.SubResource]
    :ivar subnets: An array of references to the subnets using this nat
     gateway resource.
    :vartype subnets: list[~azure.mgmt.network.v2019_02_01.models.SubResource]
    :param resource_guid: The resource GUID property of the nat gateway
     resource.
    :type resource_guid: str
    :param provisioning_state: The provisioning state of the NatGateway
     resource. Possible values are: 'Updating', 'Deleting', and 'Failed'.
    :type provisioning_state: str
    :param etag: A unique read-only string that changes whenever the resource
     is updated.
    :type etag: str
    """

    _validation = {
        'name': {'readonly': True},
        'type': {'readonly': True},
        'subnets': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'sku': {'key': 'sku', 'type': 'NatGatewaySku'},
        'idle_timeout_in_minutes': {'key': 'properties.idleTimeoutInMinutes', 'type': 'int'},
        'public_ip_addresses': {'key': 'properties.publicIpAddresses', 'type': '[SubResource]'},
        'public_ip_prefixes': {'key': 'properties.publicIpPrefixes', 'type': '[SubResource]'},
        'subnets': {'key': 'properties.subnets', 'type': '[SubResource]'},
        'resource_guid': {'key': 'properties.resourceGuid', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, *, id: str=None, location: str=None, tags=None, sku=None, idle_timeout_in_minutes: int=None, public_ip_addresses=None, public_ip_prefixes=None, resource_guid: str=None, provisioning_state: str=None, etag: str=None, **kwargs) -> None:
        super(NatGateway, self).__init__(id=id, location=location, tags=tags, **kwargs)
        self.sku = sku
        self.idle_timeout_in_minutes = idle_timeout_in_minutes
        self.public_ip_addresses = public_ip_addresses
        self.public_ip_prefixes = public_ip_prefixes
        self.subnets = None
        self.resource_guid = resource_guid
        self.provisioning_state = provisioning_state
        self.etag = etag
