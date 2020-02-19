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

from .event_subscription_destination import EventSubscriptionDestination


class StorageQueueEventSubscriptionDestination(EventSubscriptionDestination):
    """Information about the storage queue destination for an event subscription.

    All required parameters must be populated in order to send to Azure.

    :param endpoint_type: Required. Constant filled by server.
    :type endpoint_type: str
    :param resource_id: The Azure Resource ID of the storage account that
     contains the queue that is the destination of an event subscription.
    :type resource_id: str
    :param queue_name: The name of the Storage queue under a storage account
     that is the destination of an event subscription.
    :type queue_name: str
    """

    _validation = {
        'endpoint_type': {'required': True},
    }

    _attribute_map = {
        'endpoint_type': {'key': 'endpointType', 'type': 'str'},
        'resource_id': {'key': 'properties.resourceId', 'type': 'str'},
        'queue_name': {'key': 'properties.queueName', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(StorageQueueEventSubscriptionDestination, self).__init__(**kwargs)
        self.resource_id = kwargs.get('resource_id', None)
        self.queue_name = kwargs.get('queue_name', None)
        self.endpoint_type = 'StorageQueue'
