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


class SyncGroupSchemaTableColumn(Model):
    """Properties of column in sync group table.

    :param quoted_name: Quoted name of sync group table column.
    :type quoted_name: str
    :param data_size: Data size of the column.
    :type data_size: str
    :param data_type: Data type of the column.
    :type data_type: str
    """

    _attribute_map = {
        'quoted_name': {'key': 'quotedName', 'type': 'str'},
        'data_size': {'key': 'dataSize', 'type': 'str'},
        'data_type': {'key': 'dataType', 'type': 'str'},
    }

    def __init__(self, *, quoted_name: str=None, data_size: str=None, data_type: str=None, **kwargs) -> None:
        super(SyncGroupSchemaTableColumn, self).__init__(**kwargs)
        self.quoted_name = quoted_name
        self.data_size = data_size
        self.data_type = data_type
