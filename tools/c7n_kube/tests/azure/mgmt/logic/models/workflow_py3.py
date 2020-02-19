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


class Workflow(Resource):
    """The workflow type.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The resource id.
    :vartype id: str
    :ivar name: Gets the resource name.
    :vartype name: str
    :ivar type: Gets the resource type.
    :vartype type: str
    :param location: The resource location.
    :type location: str
    :param tags: The resource tags.
    :type tags: dict[str, str]
    :ivar provisioning_state: Gets the provisioning state. Possible values
     include: 'NotSpecified', 'Accepted', 'Running', 'Ready', 'Creating',
     'Created', 'Deleting', 'Deleted', 'Canceled', 'Failed', 'Succeeded',
     'Moving', 'Updating', 'Registering', 'Registered', 'Unregistering',
     'Unregistered', 'Completed'
    :vartype provisioning_state: str or
     ~azure.mgmt.logic.models.WorkflowProvisioningState
    :ivar created_time: Gets the created time.
    :vartype created_time: datetime
    :ivar changed_time: Gets the changed time.
    :vartype changed_time: datetime
    :param state: The state. Possible values include: 'NotSpecified',
     'Completed', 'Enabled', 'Disabled', 'Deleted', 'Suspended'
    :type state: str or ~azure.mgmt.logic.models.WorkflowState
    :ivar version: Gets the version.
    :vartype version: str
    :ivar access_endpoint: Gets the access endpoint.
    :vartype access_endpoint: str
    :param sku: The sku.
    :type sku: ~azure.mgmt.logic.models.Sku
    :param integration_account: The integration account.
    :type integration_account: ~azure.mgmt.logic.models.ResourceReference
    :param definition: The definition.
    :type definition: object
    :param parameters: The parameters.
    :type parameters: dict[str, ~azure.mgmt.logic.models.WorkflowParameter]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'provisioning_state': {'readonly': True},
        'created_time': {'readonly': True},
        'changed_time': {'readonly': True},
        'version': {'readonly': True},
        'access_endpoint': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'WorkflowProvisioningState'},
        'created_time': {'key': 'properties.createdTime', 'type': 'iso-8601'},
        'changed_time': {'key': 'properties.changedTime', 'type': 'iso-8601'},
        'state': {'key': 'properties.state', 'type': 'WorkflowState'},
        'version': {'key': 'properties.version', 'type': 'str'},
        'access_endpoint': {'key': 'properties.accessEndpoint', 'type': 'str'},
        'sku': {'key': 'properties.sku', 'type': 'Sku'},
        'integration_account': {'key': 'properties.integrationAccount', 'type': 'ResourceReference'},
        'definition': {'key': 'properties.definition', 'type': 'object'},
        'parameters': {'key': 'properties.parameters', 'type': '{WorkflowParameter}'},
    }

    def __init__(self, *, location: str=None, tags=None, state=None, sku=None, integration_account=None, definition=None, parameters=None, **kwargs) -> None:
        super(Workflow, self).__init__(location=location, tags=tags, **kwargs)
        self.provisioning_state = None
        self.created_time = None
        self.changed_time = None
        self.state = state
        self.version = None
        self.access_endpoint = None
        self.sku = sku
        self.integration_account = integration_account
        self.definition = definition
        self.parameters = parameters
