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


class DomainSharedAccessKeys(Model):
    """Shared access keys of the Domain.

    :param key1: Shared access key1 for the domain.
    :type key1: str
    :param key2: Shared access key2 for the domain.
    :type key2: str
    """

    _attribute_map = {
        'key1': {'key': 'key1', 'type': 'str'},
        'key2': {'key': 'key2', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(DomainSharedAccessKeys, self).__init__(**kwargs)
        self.key1 = kwargs.get('key1', None)
        self.key2 = kwargs.get('key2', None)
