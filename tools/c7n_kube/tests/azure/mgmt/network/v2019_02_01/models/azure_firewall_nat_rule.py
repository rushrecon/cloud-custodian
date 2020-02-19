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

from msrest.serialization import Model


class AzureFirewallNatRule(Model):
    """Properties of a NAT rule.

    :param name: Name of the NAT rule.
    :type name: str
    :param description: Description of the rule.
    :type description: str
    :param source_addresses: List of source IP addresses for this rule.
    :type source_addresses: list[str]
    :param destination_addresses: List of destination IP addresses for this
     rule. Supports IP ranges, prefixes, and service tags.
    :type destination_addresses: list[str]
    :param destination_ports: List of destination ports.
    :type destination_ports: list[str]
    :param protocols: Array of AzureFirewallNetworkRuleProtocols applicable to
     this NAT rule.
    :type protocols: list[str or
     ~azure.mgmt.network.v2019_02_01.models.AzureFirewallNetworkRuleProtocol]
    :param translated_address: The translated address for this NAT rule.
    :type translated_address: str
    :param translated_port: The translated port for this NAT rule.
    :type translated_port: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'source_addresses': {'key': 'sourceAddresses', 'type': '[str]'},
        'destination_addresses': {'key': 'destinationAddresses', 'type': '[str]'},
        'destination_ports': {'key': 'destinationPorts', 'type': '[str]'},
        'protocols': {'key': 'protocols', 'type': '[str]'},
        'translated_address': {'key': 'translatedAddress', 'type': 'str'},
        'translated_port': {'key': 'translatedPort', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(AzureFirewallNatRule, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.description = kwargs.get('description', None)
        self.source_addresses = kwargs.get('source_addresses', None)
        self.destination_addresses = kwargs.get('destination_addresses', None)
        self.destination_ports = kwargs.get('destination_ports', None)
        self.protocols = kwargs.get('protocols', None)
        self.translated_address = kwargs.get('translated_address', None)
        self.translated_port = kwargs.get('translated_port', None)
