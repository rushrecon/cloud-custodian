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


class ConnectionMonitorResult(Model):
    """Information about the connection monitor.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar name: Name of the connection monitor.
    :vartype name: str
    :ivar id: ID of the connection monitor.
    :vartype id: str
    :param etag:  Default value: "A unique read-only string that changes
     whenever the resource is updated." .
    :type etag: str
    :ivar type: Connection monitor type.
    :vartype type: str
    :param location: Connection monitor location.
    :type location: str
    :param tags: Connection monitor tags.
    :type tags: dict[str, str]
    :param source: Required.
    :type source:
     ~azure.mgmt.network.v2018_11_01.models.ConnectionMonitorSource
    :param destination: Required.
    :type destination:
     ~azure.mgmt.network.v2018_11_01.models.ConnectionMonitorDestination
    :param auto_start: Determines if the connection monitor will start
     automatically once created. Default value: True .
    :type auto_start: bool
    :param monitoring_interval_in_seconds: Monitoring interval in seconds.
     Default value: 60 .
    :type monitoring_interval_in_seconds: int
    :param provisioning_state: The provisioning state of the connection
     monitor. Possible values include: 'Succeeded', 'Updating', 'Deleting',
     'Failed'
    :type provisioning_state: str or
     ~azure.mgmt.network.v2018_11_01.models.ProvisioningState
    :param start_time: The date and time when the connection monitor was
     started.
    :type start_time: datetime
    :param monitoring_status: The monitoring status of the connection monitor.
    :type monitoring_status: str
    """

    _validation = {
        'name': {'readonly': True},
        'id': {'readonly': True},
        'type': {'readonly': True},
        'source': {'required': True},
        'destination': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'source': {'key': 'properties.source', 'type': 'ConnectionMonitorSource'},
        'destination': {'key': 'properties.destination', 'type': 'ConnectionMonitorDestination'},
        'auto_start': {'key': 'properties.autoStart', 'type': 'bool'},
        'monitoring_interval_in_seconds': {'key': 'properties.monitoringIntervalInSeconds', 'type': 'int'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'start_time': {'key': 'properties.startTime', 'type': 'iso-8601'},
        'monitoring_status': {'key': 'properties.monitoringStatus', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ConnectionMonitorResult, self).__init__(**kwargs)
        self.name = None
        self.id = None
        self.etag = kwargs.get('etag', "A unique read-only string that changes whenever the resource is updated.")
        self.type = None
        self.location = kwargs.get('location', None)
        self.tags = kwargs.get('tags', None)
        self.source = kwargs.get('source', None)
        self.destination = kwargs.get('destination', None)
        self.auto_start = kwargs.get('auto_start', True)
        self.monitoring_interval_in_seconds = kwargs.get('monitoring_interval_in_seconds', 60)
        self.provisioning_state = kwargs.get('provisioning_state', None)
        self.start_time = kwargs.get('start_time', None)
        self.monitoring_status = kwargs.get('monitoring_status', None)
