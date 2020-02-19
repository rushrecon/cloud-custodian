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


class KeyVaultKeyReference(Model):
    """Describes a reference to Key Vault Key.

    All required parameters must be populated in order to send to Azure.

    :param key_url: Required. The URL referencing a key encryption key in Key
     Vault.
    :type key_url: str
    :param source_vault: Required. The relative URL of the Key Vault
     containing the key.
    :type source_vault: ~azure.mgmt.compute.v2017_03_30.models.SubResource
    """

    _validation = {
        'key_url': {'required': True},
        'source_vault': {'required': True},
    }

    _attribute_map = {
        'key_url': {'key': 'keyUrl', 'type': 'str'},
        'source_vault': {'key': 'sourceVault', 'type': 'SubResource'},
    }

    def __init__(self, **kwargs):
        super(KeyVaultKeyReference, self).__init__(**kwargs)
        self.key_url = kwargs.get('key_url', None)
        self.source_vault = kwargs.get('source_vault', None)
