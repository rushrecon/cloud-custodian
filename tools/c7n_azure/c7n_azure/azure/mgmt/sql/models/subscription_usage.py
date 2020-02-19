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

from .proxy_resource import ProxyResource


class SubscriptionUsage(ProxyResource):
    """Usage Metric of a Subscription in a Location.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource ID.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :ivar display_name: User-readable name of the metric.
    :vartype display_name: str
    :ivar current_value: Current value of the metric.
    :vartype current_value: float
    :ivar limit: Boundary value of the metric.
    :vartype limit: float
    :ivar unit: Unit of the metric.
    :vartype unit: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'display_name': {'readonly': True},
        'current_value': {'readonly': True},
        'limit': {'readonly': True},
        'unit': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'display_name': {'key': 'properties.displayName', 'type': 'str'},
        'current_value': {'key': 'properties.currentValue', 'type': 'float'},
        'limit': {'key': 'properties.limit', 'type': 'float'},
        'unit': {'key': 'properties.unit', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(SubscriptionUsage, self).__init__(**kwargs)
        self.display_name = None
        self.current_value = None
        self.limit = None
        self.unit = None
