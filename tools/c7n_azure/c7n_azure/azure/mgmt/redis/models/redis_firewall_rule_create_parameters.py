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


class RedisFirewallRuleCreateParameters(Model):
    """Parameters required for creating a firewall rule on redis cache.

    :param start_ip: lowest IP address included in the range
    :type start_ip: str
    :param end_ip: highest IP address included in the range
    :type end_ip: str
    """

    _validation = {
        'start_ip': {'required': True},
        'end_ip': {'required': True},
    }

    _attribute_map = {
        'start_ip': {'key': 'properties.startIP', 'type': 'str'},
        'end_ip': {'key': 'properties.endIP', 'type': 'str'},
    }

    def __init__(self, start_ip, end_ip):
        super(RedisFirewallRuleCreateParameters, self).__init__()
        self.start_ip = start_ip
        self.end_ip = end_ip
