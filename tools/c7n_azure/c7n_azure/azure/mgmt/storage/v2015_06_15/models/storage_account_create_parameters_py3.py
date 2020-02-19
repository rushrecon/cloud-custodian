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


class StorageAccountCreateParameters(Model):
    """The parameters to provide for the account.

    All required parameters must be populated in order to send to Azure.

    :param location: Required. The location of the resource. This will be one
     of the supported and registered Azure Geo Regions (e.g. West US, East US,
     Southeast Asia, etc.). The geo region of a resource cannot be changed once
     it is created, but if an identical geo region is specified on update, the
     request will succeed.
    :type location: str
    :param tags: A list of key value pairs that describe the resource. These
     tags can be used for viewing and grouping this resource (across resource
     groups). A maximum of 15 tags can be provided for a resource. Each tag
     must have a key with a length no greater than 128 characters and a value
     with a length no greater than 256 characters.
    :type tags: dict[str, str]
    :param account_type: Required. The sku name. Required for account
     creation; optional for update. Note that in older versions, sku name was
     called accountType. Possible values include: 'Standard_LRS',
     'Standard_ZRS', 'Standard_GRS', 'Standard_RAGRS', 'Premium_LRS'
    :type account_type: str or
     ~azure.mgmt.storage.v2015_06_15.models.AccountType
    """

    _validation = {
        'location': {'required': True},
        'account_type': {'required': True},
    }

    _attribute_map = {
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'account_type': {'key': 'properties.accountType', 'type': 'AccountType'},
    }

    def __init__(self, *, location: str, account_type, tags=None, **kwargs) -> None:
        super(StorageAccountCreateParameters, self).__init__(**kwargs)
        self.location = location
        self.tags = tags
        self.account_type = account_type
