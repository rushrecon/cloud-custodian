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


class ConnectionStateSnapshot(Model):
    """Connection state snapshot.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param connection_state: The connection state. Possible values include:
     'Reachable', 'Unreachable', 'Unknown'
    :type connection_state: str or
     ~azure.mgmt.network.v2018_12_01.models.ConnectionState
    :param start_time: The start time of the connection snapshot.
    :type start_time: datetime
    :param end_time: The end time of the connection snapshot.
    :type end_time: datetime
    :param evaluation_state: Connectivity analysis evaluation state. Possible
     values include: 'NotStarted', 'InProgress', 'Completed'
    :type evaluation_state: str or
     ~azure.mgmt.network.v2018_12_01.models.EvaluationState
    :param avg_latency_in_ms: Average latency in ms.
    :type avg_latency_in_ms: int
    :param min_latency_in_ms: Minimum latency in ms.
    :type min_latency_in_ms: int
    :param max_latency_in_ms: Maximum latency in ms.
    :type max_latency_in_ms: int
    :param probes_sent: The number of sent probes.
    :type probes_sent: int
    :param probes_failed: The number of failed probes.
    :type probes_failed: int
    :ivar hops: List of hops between the source and the destination.
    :vartype hops:
     list[~azure.mgmt.network.v2018_12_01.models.ConnectivityHop]
    """

    _validation = {
        'hops': {'readonly': True},
    }

    _attribute_map = {
        'connection_state': {'key': 'connectionState', 'type': 'str'},
        'start_time': {'key': 'startTime', 'type': 'iso-8601'},
        'end_time': {'key': 'endTime', 'type': 'iso-8601'},
        'evaluation_state': {'key': 'evaluationState', 'type': 'str'},
        'avg_latency_in_ms': {'key': 'avgLatencyInMs', 'type': 'int'},
        'min_latency_in_ms': {'key': 'minLatencyInMs', 'type': 'int'},
        'max_latency_in_ms': {'key': 'maxLatencyInMs', 'type': 'int'},
        'probes_sent': {'key': 'probesSent', 'type': 'int'},
        'probes_failed': {'key': 'probesFailed', 'type': 'int'},
        'hops': {'key': 'hops', 'type': '[ConnectivityHop]'},
    }

    def __init__(self, *, connection_state=None, start_time=None, end_time=None, evaluation_state=None, avg_latency_in_ms: int=None, min_latency_in_ms: int=None, max_latency_in_ms: int=None, probes_sent: int=None, probes_failed: int=None, **kwargs) -> None:
        super(ConnectionStateSnapshot, self).__init__(**kwargs)
        self.connection_state = connection_state
        self.start_time = start_time
        self.end_time = end_time
        self.evaluation_state = evaluation_state
        self.avg_latency_in_ms = avg_latency_in_ms
        self.min_latency_in_ms = min_latency_in_ms
        self.max_latency_in_ms = max_latency_in_ms
        self.probes_sent = probes_sent
        self.probes_failed = probes_failed
        self.hops = None
