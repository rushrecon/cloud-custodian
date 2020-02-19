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

from .entity_health_state_py3 import EntityHealthState


class DeployedApplicationHealthState(EntityHealthState):
    """Represents the health state of a deployed application, which contains the
    entity identifier and the aggregated health state.

    :param aggregated_health_state: The health state of a Service Fabric
     entity such as Cluster, Node, Application, Service, Partition, Replica
     etc. Possible values include: 'Invalid', 'Ok', 'Warning', 'Error',
     'Unknown'
    :type aggregated_health_state: str or
     ~azure.servicefabric.models.HealthState
    :param node_name: Name of the node on which the service package is
     deployed.
    :type node_name: str
    :param application_name: The name of the application, including the
     'fabric:' URI scheme.
    :type application_name: str
    """

    _attribute_map = {
        'aggregated_health_state': {'key': 'AggregatedHealthState', 'type': 'str'},
        'node_name': {'key': 'NodeName', 'type': 'str'},
        'application_name': {'key': 'ApplicationName', 'type': 'str'},
    }

    def __init__(self, *, aggregated_health_state=None, node_name: str=None, application_name: str=None, **kwargs) -> None:
        super(DeployedApplicationHealthState, self).__init__(aggregated_health_state=aggregated_health_state, **kwargs)
        self.node_name = node_name
        self.application_name = application_name
