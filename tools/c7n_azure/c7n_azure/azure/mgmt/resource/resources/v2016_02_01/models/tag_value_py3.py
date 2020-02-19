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


class TagValue(Model):
    """Tag information.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The tag ID.
    :vartype id: str
    :param tag_value: The tag value.
    :type tag_value: str
    :param count: The tag value count.
    :type count: ~azure.mgmt.resource.resources.v2016_02_01.models.TagCount
    """

    _validation = {
        'id': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'tag_value': {'key': 'tagValue', 'type': 'str'},
        'count': {'key': 'count', 'type': 'TagCount'},
    }

    def __init__(self, *, tag_value: str=None, count=None, **kwargs) -> None:
        super(TagValue, self).__init__(**kwargs)
        self.id = None
        self.tag_value = tag_value
        self.count = count
