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


class InboundNatRule(SubResource):
    """Inbound NAT rule of the load balancer.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param id: Resource ID.
    :type id: str
    :param frontend_ip_configuration: A reference to frontend IP addresses.
    :type frontend_ip_configuration:
     ~azure.mgmt.network.v2019_02_01.models.SubResource
    :ivar backend_ip_configuration: A reference to a private IP address
     defined on a network interface of a VM. Traffic sent to the frontend port
     of each of the frontend IP configurations is forwarded to the backend IP.
    :vartype backend_ip_configuration:
     ~azure.mgmt.network.v2019_02_01.models.NetworkInterfaceIPConfiguration
    :param protocol: The reference to the transport protocol used by the load
     balancing rule. Possible values include: 'Udp', 'Tcp', 'All'
    :type protocol: str or
     ~azure.mgmt.network.v2019_02_01.models.TransportProtocol
    :param frontend_port: The port for the external endpoint. Port numbers for
     each rule must be unique within the Load Balancer. Acceptable values range
     from 1 to 65534.
    :type frontend_port: int
    :param backend_port: The port used for the internal endpoint. Acceptable
     values range from 1 to 65535.
    :type backend_port: int
    :param idle_timeout_in_minutes: The timeout for the TCP idle connection.
     The value can be set between 4 and 30 minutes. The default value is 4
     minutes. This element is only used when the protocol is set to TCP.
    :type idle_timeout_in_minutes: int
    :param enable_floating_ip: Configures a virtual machine's endpoint for the
     floating IP capability required to configure a SQL AlwaysOn Availability
     Group. This setting is required when using the SQL AlwaysOn Availability
     Groups in SQL server. This setting can't be changed after you create the
     endpoint.
    :type enable_floating_ip: bool
    :param enable_tcp_reset: Receive bidirectional TCP Reset on TCP flow idle
     timeout or unexpected connection termination. This element is only used
     when the protocol is set to TCP.
    :type enable_tcp_reset: bool
    :param provisioning_state: Gets the provisioning state of the public IP
     resource. Possible values are: 'Updating', 'Deleting', and 'Failed'.
    :type provisioning_state: str
    :param name: Gets name of the resource that is unique within a resource
     group. This name can be used to access the resource.
    :type name: str
    :param etag: A unique read-only string that changes whenever the resource
     is updated.
    :type etag: str
    """

    _validation = {
        'backend_ip_configuration': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'frontend_ip_configuration': {'key': 'properties.frontendIPConfiguration', 'type': 'SubResource'},
        'backend_ip_configuration': {'key': 'properties.backendIPConfiguration', 'type': 'NetworkInterfaceIPConfiguration'},
        'protocol': {'key': 'properties.protocol', 'type': 'str'},
        'frontend_port': {'key': 'properties.frontendPort', 'type': 'int'},
        'backend_port': {'key': 'properties.backendPort', 'type': 'int'},
        'idle_timeout_in_minutes': {'key': 'properties.idleTimeoutInMinutes', 'type': 'int'},
        'enable_floating_ip': {'key': 'properties.enableFloatingIP', 'type': 'bool'},
        'enable_tcp_reset': {'key': 'properties.enableTcpReset', 'type': 'bool'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(InboundNatRule, self).__init__(**kwargs)
        self.frontend_ip_configuration = kwargs.get('frontend_ip_configuration', None)
        self.backend_ip_configuration = None
        self.protocol = kwargs.get('protocol', None)
        self.frontend_port = kwargs.get('frontend_port', None)
        self.backend_port = kwargs.get('backend_port', None)
        self.idle_timeout_in_minutes = kwargs.get('idle_timeout_in_minutes', None)
        self.enable_floating_ip = kwargs.get('enable_floating_ip', None)
        self.enable_tcp_reset = kwargs.get('enable_tcp_reset', None)
        self.provisioning_state = kwargs.get('provisioning_state', None)
        self.name = kwargs.get('name', None)
        self.etag = kwargs.get('etag', None)
