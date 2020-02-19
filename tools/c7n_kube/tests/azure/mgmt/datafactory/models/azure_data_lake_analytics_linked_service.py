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

from .linked_service import LinkedService


class AzureDataLakeAnalyticsLinkedService(LinkedService):
    """Azure Data Lake Analytics linked service.

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param connect_via: The integration runtime reference.
    :type connect_via:
     ~azure.mgmt.datafactory.models.IntegrationRuntimeReference
    :param description: Linked service description.
    :type description: str
    :param parameters: Parameters for linked service.
    :type parameters: dict[str,
     ~azure.mgmt.datafactory.models.ParameterSpecification]
    :param annotations: List of tags that can be used for describing the
     Dataset.
    :type annotations: list[object]
    :param type: Constant filled by server.
    :type type: str
    :param account_name: The Azure Data Lake Analytics account name. Type:
     string (or Expression with resultType string).
    :type account_name: object
    :param service_principal_id: The ID of the application used to
     authenticate against the Azure Data Lake Analytics account. Type: string
     (or Expression with resultType string).
    :type service_principal_id: object
    :param service_principal_key: The Key of the application used to
     authenticate against the Azure Data Lake Analytics account.
    :type service_principal_key: ~azure.mgmt.datafactory.models.SecretBase
    :param tenant: The name or ID of the tenant to which the service principal
     belongs. Type: string (or Expression with resultType string).
    :type tenant: object
    :param subscription_id: Data Lake Analytics account subscription ID (if
     different from Data Factory account). Type: string (or Expression with
     resultType string).
    :type subscription_id: object
    :param resource_group_name: Data Lake Analytics account resource group
     name (if different from Data Factory account). Type: string (or Expression
     with resultType string).
    :type resource_group_name: object
    :param data_lake_analytics_uri: Azure Data Lake Analytics URI Type: string
     (or Expression with resultType string).
    :type data_lake_analytics_uri: object
    :param encrypted_credential: The encrypted credential used for
     authentication. Credentials are encrypted using the integration runtime
     credential manager. Type: string (or Expression with resultType string).
    :type encrypted_credential: object
    """

    _validation = {
        'type': {'required': True},
        'account_name': {'required': True},
        'tenant': {'required': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'connect_via': {'key': 'connectVia', 'type': 'IntegrationRuntimeReference'},
        'description': {'key': 'description', 'type': 'str'},
        'parameters': {'key': 'parameters', 'type': '{ParameterSpecification}'},
        'annotations': {'key': 'annotations', 'type': '[object]'},
        'type': {'key': 'type', 'type': 'str'},
        'account_name': {'key': 'typeProperties.accountName', 'type': 'object'},
        'service_principal_id': {'key': 'typeProperties.servicePrincipalId', 'type': 'object'},
        'service_principal_key': {'key': 'typeProperties.servicePrincipalKey', 'type': 'SecretBase'},
        'tenant': {'key': 'typeProperties.tenant', 'type': 'object'},
        'subscription_id': {'key': 'typeProperties.subscriptionId', 'type': 'object'},
        'resource_group_name': {'key': 'typeProperties.resourceGroupName', 'type': 'object'},
        'data_lake_analytics_uri': {'key': 'typeProperties.dataLakeAnalyticsUri', 'type': 'object'},
        'encrypted_credential': {'key': 'typeProperties.encryptedCredential', 'type': 'object'},
    }

    def __init__(self, account_name, tenant, additional_properties=None, connect_via=None, description=None, parameters=None, annotations=None, service_principal_id=None, service_principal_key=None, subscription_id=None, resource_group_name=None, data_lake_analytics_uri=None, encrypted_credential=None):
        super(AzureDataLakeAnalyticsLinkedService, self).__init__(additional_properties=additional_properties, connect_via=connect_via, description=description, parameters=parameters, annotations=annotations)
        self.account_name = account_name
        self.service_principal_id = service_principal_id
        self.service_principal_key = service_principal_key
        self.tenant = tenant
        self.subscription_id = subscription_id
        self.resource_group_name = resource_group_name
        self.data_lake_analytics_uri = data_lake_analytics_uri
        self.encrypted_credential = encrypted_credential
        self.type = 'AzureDataLakeAnalytics'
