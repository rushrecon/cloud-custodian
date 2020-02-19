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


class CreateComposeDeploymentDescription(Model):
    """Defines description for creating a Service Fabric compose deployment.

    All required parameters must be populated in order to send to Azure.

    :param deployment_name: Required. The name of the deployment.
    :type deployment_name: str
    :param compose_file_content: Required. The content of the compose file
     that describes the deployment to create.
    :type compose_file_content: str
    :param registry_credential: Credential information to connect to container
     registry.
    :type registry_credential: ~azure.servicefabric.models.RegistryCredential
    """

    _validation = {
        'deployment_name': {'required': True},
        'compose_file_content': {'required': True},
    }

    _attribute_map = {
        'deployment_name': {'key': 'DeploymentName', 'type': 'str'},
        'compose_file_content': {'key': 'ComposeFileContent', 'type': 'str'},
        'registry_credential': {'key': 'RegistryCredential', 'type': 'RegistryCredential'},
    }

    def __init__(self, **kwargs):
        super(CreateComposeDeploymentDescription, self).__init__(**kwargs)
        self.deployment_name = kwargs.get('deployment_name', None)
        self.compose_file_content = kwargs.get('compose_file_content', None)
        self.registry_credential = kwargs.get('registry_credential', None)
