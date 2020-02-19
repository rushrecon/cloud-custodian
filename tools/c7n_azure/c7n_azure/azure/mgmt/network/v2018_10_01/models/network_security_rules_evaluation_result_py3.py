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


class NetworkSecurityRulesEvaluationResult(Model):
    """Network security rules evaluation result.

    :param name: Name of the network security rule.
    :type name: str
    :param protocol_matched: Value indicating whether protocol is matched.
    :type protocol_matched: bool
    :param source_matched: Value indicating whether source is matched.
    :type source_matched: bool
    :param source_port_matched: Value indicating whether source port is
     matched.
    :type source_port_matched: bool
    :param destination_matched: Value indicating whether destination is
     matched.
    :type destination_matched: bool
    :param destination_port_matched: Value indicating whether destination port
     is matched.
    :type destination_port_matched: bool
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'protocol_matched': {'key': 'protocolMatched', 'type': 'bool'},
        'source_matched': {'key': 'sourceMatched', 'type': 'bool'},
        'source_port_matched': {'key': 'sourcePortMatched', 'type': 'bool'},
        'destination_matched': {'key': 'destinationMatched', 'type': 'bool'},
        'destination_port_matched': {'key': 'destinationPortMatched', 'type': 'bool'},
    }

    def __init__(self, *, name: str=None, protocol_matched: bool=None, source_matched: bool=None, source_port_matched: bool=None, destination_matched: bool=None, destination_port_matched: bool=None, **kwargs) -> None:
        super(NetworkSecurityRulesEvaluationResult, self).__init__(**kwargs)
        self.name = name
        self.protocol_matched = protocol_matched
        self.source_matched = source_matched
        self.source_port_matched = source_port_matched
        self.destination_matched = destination_matched
        self.destination_port_matched = destination_port_matched
