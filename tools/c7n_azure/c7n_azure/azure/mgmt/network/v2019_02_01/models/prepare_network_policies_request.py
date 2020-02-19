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


class PrepareNetworkPoliciesRequest(Model):
    """Details of PrepareNetworkPolicies for Subnet.

    :param service_name: The name of the service for which subnet is being
     prepared for.
    :type service_name: str
    :param resource_group_name: The name of the resource group where the
     Network Intent Policy will be stored.
    :type resource_group_name: str
    :param network_intent_policy_configurations: A list of
     NetworkIntentPolicyConfiguration.
    :type network_intent_policy_configurations:
     list[~azure.mgmt.network.v2019_02_01.models.NetworkIntentPolicyConfiguration]
    """

    _attribute_map = {
        'service_name': {'key': 'serviceName', 'type': 'str'},
        'resource_group_name': {'key': 'resourceGroupName', 'type': 'str'},
        'network_intent_policy_configurations': {'key': 'networkIntentPolicyConfigurations', 'type': '[NetworkIntentPolicyConfiguration]'},
    }

    def __init__(self, **kwargs):
        super(PrepareNetworkPoliciesRequest, self).__init__(**kwargs)
        self.service_name = kwargs.get('service_name', None)
        self.resource_group_name = kwargs.get('resource_group_name', None)
        self.network_intent_policy_configurations = kwargs.get('network_intent_policy_configurations', None)
