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


class NetworkSecurityGroupResult(Model):
    """Network configuration diagnostic result corresponded provided traffic
    query.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param security_rule_access_result: The network traffic is allowed or
     denied. Possible values are 'Allow' and 'Deny'. Possible values include:
     'Allow', 'Deny'
    :type security_rule_access_result: str or
     ~azure.mgmt.network.v2018_11_01.models.SecurityRuleAccess
    :ivar evaluated_network_security_groups: List of results network security
     groups diagnostic.
    :vartype evaluated_network_security_groups:
     list[~azure.mgmt.network.v2018_11_01.models.EvaluatedNetworkSecurityGroup]
    """

    _validation = {
        'evaluated_network_security_groups': {'readonly': True},
    }

    _attribute_map = {
        'security_rule_access_result': {'key': 'securityRuleAccessResult', 'type': 'str'},
        'evaluated_network_security_groups': {'key': 'evaluatedNetworkSecurityGroups', 'type': '[EvaluatedNetworkSecurityGroup]'},
    }

    def __init__(self, **kwargs):
        super(NetworkSecurityGroupResult, self).__init__(**kwargs)
        self.security_rule_access_result = kwargs.get('security_rule_access_result', None)
        self.evaluated_network_security_groups = None
