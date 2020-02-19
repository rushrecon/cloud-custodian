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


class OutboundRule(SubResource):
    """Outbound pool of the load balancer.

    All required parameters must be populated in order to send to Azure.

    :param id: Resource ID.
    :type id: str
    :param allocated_outbound_ports: The number of outbound ports to be used
     for NAT.
    :type allocated_outbound_ports: int
    :param frontend_ip_configurations: Required. The Frontend IP addresses of
     the load balancer.
    :type frontend_ip_configurations:
     list[~azure.mgmt.network.v2018_12_01.models.SubResource]
    :param backend_address_pool: Required. A reference to a pool of DIPs.
     Outbound traffic is randomly load balanced across IPs in the backend IPs.
    :type backend_address_pool:
     ~azure.mgmt.network.v2018_12_01.models.SubResource
    :param provisioning_state: Gets the provisioning state of the PublicIP
     resource. Possible values are: 'Updating', 'Deleting', and 'Failed'.
    :type provisioning_state: str
    :param protocol: Required. Protocol - TCP, UDP or All. Possible values
     include: 'Tcp', 'Udp', 'All'
    :type protocol: str or ~azure.mgmt.network.v2018_12_01.models.enum
    :param enable_tcp_reset: Receive bidirectional TCP Reset on TCP flow idle
     timeout or unexpected connection termination. This element is only used
     when the protocol is set to TCP.
    :type enable_tcp_reset: bool
    :param idle_timeout_in_minutes: The timeout for the TCP idle connection
    :type idle_timeout_in_minutes: int
    :param name: The name of the resource that is unique within a resource
     group. This name can be used to access the resource.
    :type name: str
    :param etag: A unique read-only string that changes whenever the resource
     is updated.
    :type etag: str
    """

    _validation = {
        'frontend_ip_configurations': {'required': True},
        'backend_address_pool': {'required': True},
        'protocol': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'allocated_outbound_ports': {'key': 'properties.allocatedOutboundPorts', 'type': 'int'},
        'frontend_ip_configurations': {'key': 'properties.frontendIPConfigurations', 'type': '[SubResource]'},
        'backend_address_pool': {'key': 'properties.backendAddressPool', 'type': 'SubResource'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'protocol': {'key': 'properties.protocol', 'type': 'str'},
        'enable_tcp_reset': {'key': 'properties.enableTcpReset', 'type': 'bool'},
        'idle_timeout_in_minutes': {'key': 'properties.idleTimeoutInMinutes', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(OutboundRule, self).__init__(**kwargs)
        self.allocated_outbound_ports = kwargs.get('allocated_outbound_ports', None)
        self.frontend_ip_configurations = kwargs.get('frontend_ip_configurations', None)
        self.backend_address_pool = kwargs.get('backend_address_pool', None)
        self.provisioning_state = kwargs.get('provisioning_state', None)
        self.protocol = kwargs.get('protocol', None)
        self.enable_tcp_reset = kwargs.get('enable_tcp_reset', None)
        self.idle_timeout_in_minutes = kwargs.get('idle_timeout_in_minutes', None)
        self.name = kwargs.get('name', None)
        self.etag = kwargs.get('etag', None)
