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


class WebApplicationFirewallCustomRule(Model):
    """Defines contents of a web application rule.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param name: Gets name of the resource that is unique within a policy.
     This name can be used to access the resource.
    :type name: str
    :ivar etag: Gets a unique read-only string that changes whenever the
     resource is updated.
    :vartype etag: str
    :param priority: Required. Describes priority of the rule. Rules with a
     lower value will be evaluated before rules with a higher value
    :type priority: int
    :param rule_type: Required. Describes type of rule. Possible values
     include: 'MatchRule', 'Invalid'
    :type rule_type: str or
     ~azure.mgmt.network.v2019_02_01.models.WebApplicationFirewallRuleType
    :param match_conditions: Required. List of match conditions
    :type match_conditions:
     list[~azure.mgmt.network.v2019_02_01.models.MatchCondition]
    :param action: Required. Type of Actions. Possible values include:
     'Allow', 'Block', 'Log'
    :type action: str or
     ~azure.mgmt.network.v2019_02_01.models.WebApplicationFirewallAction
    """

    _validation = {
        'name': {'max_length': 128},
        'etag': {'readonly': True},
        'priority': {'required': True},
        'rule_type': {'required': True},
        'match_conditions': {'required': True},
        'action': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
        'priority': {'key': 'priority', 'type': 'int'},
        'rule_type': {'key': 'ruleType', 'type': 'str'},
        'match_conditions': {'key': 'matchConditions', 'type': '[MatchCondition]'},
        'action': {'key': 'action', 'type': 'str'},
    }

    def __init__(self, *, priority: int, rule_type, match_conditions, action, name: str=None, **kwargs) -> None:
        super(WebApplicationFirewallCustomRule, self).__init__(**kwargs)
        self.name = name
        self.etag = None
        self.priority = priority
        self.rule_type = rule_type
        self.match_conditions = match_conditions
        self.action = action
