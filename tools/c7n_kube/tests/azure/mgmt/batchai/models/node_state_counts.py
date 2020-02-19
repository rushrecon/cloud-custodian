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


class NodeStateCounts(Model):
    """Counts of various compute node states on the cluster.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar idle_node_count: Number of compute nodes in idle state.
    :vartype idle_node_count: int
    :ivar running_node_count: Number of compute nodes which are running jobs.
    :vartype running_node_count: int
    :ivar preparing_node_count: Number of compute nodes which are being
     prepared.
    :vartype preparing_node_count: int
    :ivar unusable_node_count: Number of compute nodes which are unusable.
    :vartype unusable_node_count: int
    :ivar leaving_node_count: Number of compute nodes which are leaving the
     cluster.
    :vartype leaving_node_count: int
    """

    _validation = {
        'idle_node_count': {'readonly': True},
        'running_node_count': {'readonly': True},
        'preparing_node_count': {'readonly': True},
        'unusable_node_count': {'readonly': True},
        'leaving_node_count': {'readonly': True},
    }

    _attribute_map = {
        'idle_node_count': {'key': 'idleNodeCount', 'type': 'int'},
        'running_node_count': {'key': 'runningNodeCount', 'type': 'int'},
        'preparing_node_count': {'key': 'preparingNodeCount', 'type': 'int'},
        'unusable_node_count': {'key': 'unusableNodeCount', 'type': 'int'},
        'leaving_node_count': {'key': 'leavingNodeCount', 'type': 'int'},
    }

    def __init__(self, **kwargs):
        super(NodeStateCounts, self).__init__(**kwargs)
        self.idle_node_count = None
        self.running_node_count = None
        self.preparing_node_count = None
        self.unusable_node_count = None
        self.leaving_node_count = None
