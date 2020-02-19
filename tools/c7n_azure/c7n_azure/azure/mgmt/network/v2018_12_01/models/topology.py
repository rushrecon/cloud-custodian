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


class Topology(Model):
    """Topology of the specified resource group.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: GUID representing the operation id.
    :vartype id: str
    :ivar created_date_time: The datetime when the topology was initially
     created for the resource group.
    :vartype created_date_time: datetime
    :ivar last_modified: The datetime when the topology was last modified.
    :vartype last_modified: datetime
    :param resources:
    :type resources:
     list[~azure.mgmt.network.v2018_12_01.models.TopologyResource]
    """

    _validation = {
        'id': {'readonly': True},
        'created_date_time': {'readonly': True},
        'last_modified': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'created_date_time': {'key': 'createdDateTime', 'type': 'iso-8601'},
        'last_modified': {'key': 'lastModified', 'type': 'iso-8601'},
        'resources': {'key': 'resources', 'type': '[TopologyResource]'},
    }

    def __init__(self, **kwargs):
        super(Topology, self).__init__(**kwargs)
        self.id = None
        self.created_date_time = None
        self.last_modified = None
        self.resources = kwargs.get('resources', None)
