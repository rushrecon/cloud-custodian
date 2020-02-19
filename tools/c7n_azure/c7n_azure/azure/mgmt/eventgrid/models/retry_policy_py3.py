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


class RetryPolicy(Model):
    """Information about the retry policy for an event subscription.

    :param max_delivery_attempts: Maximum number of delivery retry attempts
     for events.
    :type max_delivery_attempts: int
    :param event_time_to_live_in_minutes: Time To Live (in minutes) for
     events.
    :type event_time_to_live_in_minutes: int
    """

    _attribute_map = {
        'max_delivery_attempts': {'key': 'maxDeliveryAttempts', 'type': 'int'},
        'event_time_to_live_in_minutes': {'key': 'eventTimeToLiveInMinutes', 'type': 'int'},
    }

    def __init__(self, *, max_delivery_attempts: int=None, event_time_to_live_in_minutes: int=None, **kwargs) -> None:
        super(RetryPolicy, self).__init__(**kwargs)
        self.max_delivery_attempts = max_delivery_attempts
        self.event_time_to_live_in_minutes = event_time_to_live_in_minutes
