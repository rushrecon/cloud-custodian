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


class ResourceMetricProperty(Model):
    """Resource metric property.

    :param key: Key for resource metric property.
    :type key: str
    :param value: Value of pair.
    :type value: str
    """

    _attribute_map = {
        'key': {'key': 'key', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'},
    }

    def __init__(self, key=None, value=None):
        super(ResourceMetricProperty, self).__init__()
        self.key = key
        self.value = value
