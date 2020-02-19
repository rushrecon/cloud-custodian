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


class ApplicationGatewayBackendHttpSettings(SubResource):
    """Backend address pool settings of an application gateway.

    :param id: Resource Identifier.
    :type id: str
    :param port: Port
    :type port: int
    :param protocol: Protocol. Possible values are: 'Http' and 'Https'.
     Possible values include: 'Http', 'Https'
    :type protocol: str or
     ~azure.mgmt.network.v2015_06_15.models.ApplicationGatewayProtocol
    :param cookie_based_affinity: Cookie based affinity. Possible values are:
     'Enabled' and 'Disabled'. Possible values include: 'Enabled', 'Disabled'
    :type cookie_based_affinity: str or
     ~azure.mgmt.network.v2015_06_15.models.ApplicationGatewayCookieBasedAffinity
    :param request_timeout: Request timeout in seconds. Application Gateway
     will fail the request if response is not received within RequestTimeout.
     Acceptable values are from 1 second to 86400 seconds.
    :type request_timeout: int
    :param probe: Probe resource of an application gateway.
    :type probe: ~azure.mgmt.network.v2015_06_15.models.SubResource
    :param provisioning_state: Gets or sets Provisioning state of the backend
     http settings resource Updating/Deleting/Failed
    :type provisioning_state: str
    :param name: Name of the resource that is unique within a resource group.
     This name can be used to access the resource.
    :type name: str
    :param etag: A unique read-only string that changes whenever the resource
     is updated.
    :type etag: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'port': {'key': 'properties.port', 'type': 'int'},
        'protocol': {'key': 'properties.protocol', 'type': 'str'},
        'cookie_based_affinity': {'key': 'properties.cookieBasedAffinity', 'type': 'str'},
        'request_timeout': {'key': 'properties.requestTimeout', 'type': 'int'},
        'probe': {'key': 'properties.probe', 'type': 'SubResource'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, *, id: str=None, port: int=None, protocol=None, cookie_based_affinity=None, request_timeout: int=None, probe=None, provisioning_state: str=None, name: str=None, etag: str=None, **kwargs) -> None:
        super(ApplicationGatewayBackendHttpSettings, self).__init__(id=id, **kwargs)
        self.port = port
        self.protocol = protocol
        self.cookie_based_affinity = cookie_based_affinity
        self.request_timeout = request_timeout
        self.probe = probe
        self.provisioning_state = provisioning_state
        self.name = name
        self.etag = etag
