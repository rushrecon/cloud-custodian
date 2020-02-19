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


class AzureFirewallApplicationRule(Model):
    """Properties of an application rule.

    :param name: Name of the application rule.
    :type name: str
    :param description: Description of the rule.
    :type description: str
    :param source_addresses: List of source IP addresses for this rule.
    :type source_addresses: list[str]
    :param protocols: Array of ApplicationRuleProtocols.
    :type protocols:
     list[~azure.mgmt.network.v2018_08_01.models.AzureFirewallApplicationRuleProtocol]
    :param target_fqdns: List of FQDNs for this rule.
    :type target_fqdns: list[str]
    :param fqdn_tags: List of FQDN Tags for this rule.
    :type fqdn_tags: list[str]
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'source_addresses': {'key': 'sourceAddresses', 'type': '[str]'},
        'protocols': {'key': 'protocols', 'type': '[AzureFirewallApplicationRuleProtocol]'},
        'target_fqdns': {'key': 'targetFqdns', 'type': '[str]'},
        'fqdn_tags': {'key': 'fqdnTags', 'type': '[str]'},
    }

    def __init__(self, **kwargs):
        super(AzureFirewallApplicationRule, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.description = kwargs.get('description', None)
        self.source_addresses = kwargs.get('source_addresses', None)
        self.protocols = kwargs.get('protocols', None)
        self.target_fqdns = kwargs.get('target_fqdns', None)
        self.fqdn_tags = kwargs.get('fqdn_tags', None)
