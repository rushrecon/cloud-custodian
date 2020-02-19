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


class ApplicationGatewayAutoscaleConfiguration(Model):
    """Application Gateway autoscale configuration.

    All required parameters must be populated in order to send to Azure.

    :param min_capacity: Required. Lower bound on number of Application
     Gateway capacity
    :type min_capacity: int
    :param max_capacity: Upper bound on number of Application Gateway capacity
    :type max_capacity: int
    """

    _validation = {
        'min_capacity': {'required': True, 'minimum': 0},
        'max_capacity': {'minimum': 2},
    }

    _attribute_map = {
        'min_capacity': {'key': 'minCapacity', 'type': 'int'},
        'max_capacity': {'key': 'maxCapacity', 'type': 'int'},
    }

    def __init__(self, *, min_capacity: int, max_capacity: int=None, **kwargs) -> None:
        super(ApplicationGatewayAutoscaleConfiguration, self).__init__(**kwargs)
        self.min_capacity = min_capacity
        self.max_capacity = max_capacity
