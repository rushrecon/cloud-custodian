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


class SubResource(Model):
    """Azure resource manager sub resource properties.

    :param id: Resource Identifier.
    :type id: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(SubResource, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
