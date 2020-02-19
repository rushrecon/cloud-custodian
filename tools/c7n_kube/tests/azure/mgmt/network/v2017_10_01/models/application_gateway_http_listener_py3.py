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


class ApplicationGatewayHttpListener(SubResource):
    """Http listener of an application gateway.

    :param id: Resource ID.
    :type id: str
    :param frontend_ip_configuration: Frontend IP configuration resource of an
     application gateway.
    :type frontend_ip_configuration:
     ~azure.mgmt.network.v2017_10_01.models.SubResource
    :param frontend_port: Frontend port resource of an application gateway.
    :type frontend_port: ~azure.mgmt.network.v2017_10_01.models.SubResource
    :param protocol: Protocol. Possible values include: 'Http', 'Https'
    :type protocol: str or
     ~azure.mgmt.network.v2017_10_01.models.ApplicationGatewayProtocol
    :param host_name: Host name of HTTP listener.
    :type host_name: str
    :param ssl_certificate: SSL certificate resource of an application
     gateway.
    :type ssl_certificate: ~azure.mgmt.network.v2017_10_01.models.SubResource
    :param require_server_name_indication: Applicable only if protocol is
     https. Enables SNI for multi-hosting.
    :type require_server_name_indication: bool
    :param provisioning_state: Provisioning state of the HTTP listener
     resource. Possible values are: 'Updating', 'Deleting', and 'Failed'.
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
        'frontend_ip_configuration': {'key': 'properties.frontendIPConfiguration', 'type': 'SubResource'},
        'frontend_port': {'key': 'properties.frontendPort', 'type': 'SubResource'},
        'protocol': {'key': 'properties.protocol', 'type': 'str'},
        'host_name': {'key': 'properties.hostName', 'type': 'str'},
        'ssl_certificate': {'key': 'properties.sslCertificate', 'type': 'SubResource'},
        'require_server_name_indication': {'key': 'properties.requireServerNameIndication', 'type': 'bool'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, *, id: str=None, frontend_ip_configuration=None, frontend_port=None, protocol=None, host_name: str=None, ssl_certificate=None, require_server_name_indication: bool=None, provisioning_state: str=None, name: str=None, etag: str=None, type: str=None, **kwargs) -> None:
        super(ApplicationGatewayHttpListener, self).__init__(id=id, **kwargs)
        self.frontend_ip_configuration = frontend_ip_configuration
        self.frontend_port = frontend_port
        self.protocol = protocol
        self.host_name = host_name
        self.ssl_certificate = ssl_certificate
        self.require_server_name_indication = require_server_name_indication
        self.provisioning_state = provisioning_state
        self.name = name
        self.etag = etag
        self.type = type
