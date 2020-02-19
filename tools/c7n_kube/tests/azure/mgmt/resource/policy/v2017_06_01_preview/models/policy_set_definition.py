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


class PolicySetDefinition(Model):
    """The policy set definition.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param policy_type: The type of policy definition. Possible values are
     NotSpecified, BuiltIn, and Custom. Possible values include:
     'NotSpecified', 'BuiltIn', 'Custom'
    :type policy_type: str or
     ~azure.mgmt.resource.policy.v2017_06_01_preview.models.PolicyType
    :param display_name: The display name of the policy set definition.
    :type display_name: str
    :param description: The policy set definition description.
    :type description: str
    :param metadata: The policy set definition metadata.
    :type metadata: object
    :param parameters: The policy set definition parameters that can be used
     in policy definition references.
    :type parameters: object
    :param policy_definitions: Required. An array of policy definition
     references.
    :type policy_definitions:
     list[~azure.mgmt.resource.policy.v2017_06_01_preview.models.PolicyDefinitionReference]
    :ivar id: The ID of the policy set definition.
    :vartype id: str
    :ivar name: The name of the policy set definition.
    :vartype name: str
    :ivar type: The type of the resource
     (Microsoft.Authorization/policySetDefinitions).
    :vartype type: str
    """

    _validation = {
        'policy_definitions': {'required': True},
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'policy_type': {'key': 'properties.policyType', 'type': 'str'},
        'display_name': {'key': 'properties.displayName', 'type': 'str'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'metadata': {'key': 'properties.metadata', 'type': 'object'},
        'parameters': {'key': 'properties.parameters', 'type': 'object'},
        'policy_definitions': {'key': 'properties.policyDefinitions', 'type': '[PolicyDefinitionReference]'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(PolicySetDefinition, self).__init__(**kwargs)
        self.policy_type = kwargs.get('policy_type', None)
        self.display_name = kwargs.get('display_name', None)
        self.description = kwargs.get('description', None)
        self.metadata = kwargs.get('metadata', None)
        self.parameters = kwargs.get('parameters', None)
        self.policy_definitions = kwargs.get('policy_definitions', None)
        self.id = None
        self.name = None
        self.type = None
