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


class BatchAccountRegenerateKeyParameters(Model):
    """Parameters supplied to the RegenerateKey operation.

    :param key_name: The type of account key to regenerate. Possible values
     include: 'Primary', 'Secondary'
    :type key_name: str or ~azure.mgmt.batch.models.AccountKeyType
    """

    _validation = {
        'key_name': {'required': True},
    }

    _attribute_map = {
        'key_name': {'key': 'keyName', 'type': 'AccountKeyType'},
    }

    def __init__(self, key_name):
        super(BatchAccountRegenerateKeyParameters, self).__init__()
        self.key_name = key_name
