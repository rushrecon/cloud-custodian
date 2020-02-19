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

from .resource_py3 import Resource


class ApplicationGatewayFirewallRuleSet(Resource):
    """A web application firewall rule set.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param id: Resource ID.
    :type id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param location: Resource location.
    :type location: str
    :param tags: Resource tags.
    :type tags: dict[str, str]
    :param provisioning_state: The provisioning state of the web application
     firewall rule set.
    :type provisioning_state: str
    :param rule_set_type: Required. The type of the web application firewall
     rule set.
    :type rule_set_type: str
    :param rule_set_version: Required. The version of the web application
     firewall rule set type.
    :type rule_set_version: str
    :param rule_groups: Required. The rule groups of the web application
     firewall rule set.
    :type rule_groups:
     list[~azure.mgmt.network.v2017_11_01.models.ApplicationGatewayFirewallRuleGroup]
    """

    _validation = {
        'name': {'readonly': True},
        'type': {'readonly': True},
        'rule_set_type': {'required': True},
        'rule_set_version': {'required': True},
        'rule_groups': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'rule_set_type': {'key': 'properties.ruleSetType', 'type': 'str'},
        'rule_set_version': {'key': 'properties.ruleSetVersion', 'type': 'str'},
        'rule_groups': {'key': 'properties.ruleGroups', 'type': '[ApplicationGatewayFirewallRuleGroup]'},
    }

    def __init__(self, *, rule_set_type: str, rule_set_version: str, rule_groups, id: str=None, location: str=None, tags=None, provisioning_state: str=None, **kwargs) -> None:
        super(ApplicationGatewayFirewallRuleSet, self).__init__(id=id, location=location, tags=tags, **kwargs)
        self.provisioning_state = provisioning_state
        self.rule_set_type = rule_set_type
        self.rule_set_version = rule_set_version
        self.rule_groups = rule_groups
