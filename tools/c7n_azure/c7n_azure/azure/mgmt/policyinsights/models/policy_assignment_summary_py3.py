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


class PolicyAssignmentSummary(Model):
    """Policy assignment summary.

    :param policy_assignment_id: Policy assignment ID.
    :type policy_assignment_id: str
    :param policy_set_definition_id: Policy set definition ID, if the policy
     assignment is for a policy set.
    :type policy_set_definition_id: str
    :param results: Non-compliance summary for the policy assignment.
    :type results: ~azure.mgmt.policyinsights.models.SummaryResults
    :param policy_definitions: Policy definitions summary.
    :type policy_definitions:
     list[~azure.mgmt.policyinsights.models.PolicyDefinitionSummary]
    """

    _attribute_map = {
        'policy_assignment_id': {'key': 'policyAssignmentId', 'type': 'str'},
        'policy_set_definition_id': {'key': 'policySetDefinitionId', 'type': 'str'},
        'results': {'key': 'results', 'type': 'SummaryResults'},
        'policy_definitions': {'key': 'policyDefinitions', 'type': '[PolicyDefinitionSummary]'},
    }

    def __init__(self, *, policy_assignment_id: str=None, policy_set_definition_id: str=None, results=None, policy_definitions=None, **kwargs) -> None:
        super(PolicyAssignmentSummary, self).__init__(**kwargs)
        self.policy_assignment_id = policy_assignment_id
        self.policy_set_definition_id = policy_set_definition_id
        self.results = results
        self.policy_definitions = policy_definitions
