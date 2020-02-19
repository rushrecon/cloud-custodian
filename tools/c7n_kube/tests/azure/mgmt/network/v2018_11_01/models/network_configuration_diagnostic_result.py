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


class NetworkConfigurationDiagnosticResult(Model):
    """Network configuration diagnostic result corresponded to provided traffic
    query.

    :param profile:
    :type profile:
     ~azure.mgmt.network.v2018_11_01.models.NetworkConfigurationDiagnosticProfile
    :param network_security_group_result:
    :type network_security_group_result:
     ~azure.mgmt.network.v2018_11_01.models.NetworkSecurityGroupResult
    """

    _attribute_map = {
        'profile': {'key': 'profile', 'type': 'NetworkConfigurationDiagnosticProfile'},
        'network_security_group_result': {'key': 'networkSecurityGroupResult', 'type': 'NetworkSecurityGroupResult'},
    }

    def __init__(self, **kwargs):
        super(NetworkConfigurationDiagnosticResult, self).__init__(**kwargs)
        self.profile = kwargs.get('profile', None)
        self.network_security_group_result = kwargs.get('network_security_group_result', None)
