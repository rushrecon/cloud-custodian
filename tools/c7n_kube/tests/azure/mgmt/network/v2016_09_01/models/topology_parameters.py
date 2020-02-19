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


class TopologyParameters(Model):
    """Parameters that define the representation of topology.

    All required parameters must be populated in order to send to Azure.

    :param target_resource_group_name: Required. The name of the target
     resource group to perform topology on.
    :type target_resource_group_name: str
    """

    _validation = {
        'target_resource_group_name': {'required': True},
    }

    _attribute_map = {
        'target_resource_group_name': {'key': 'targetResourceGroupName', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(TopologyParameters, self).__init__(**kwargs)
        self.target_resource_group_name = kwargs.get('target_resource_group_name', None)
