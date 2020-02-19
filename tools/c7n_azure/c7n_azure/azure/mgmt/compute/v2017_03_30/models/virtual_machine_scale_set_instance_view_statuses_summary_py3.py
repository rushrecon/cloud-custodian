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


class VirtualMachineScaleSetInstanceViewStatusesSummary(Model):
    """Instance view statuses summary for virtual machines of a virtual machine
    scale set.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar statuses_summary: The extensions information.
    :vartype statuses_summary:
     list[~azure.mgmt.compute.v2017_03_30.models.VirtualMachineStatusCodeCount]
    """

    _validation = {
        'statuses_summary': {'readonly': True},
    }

    _attribute_map = {
        'statuses_summary': {'key': 'statusesSummary', 'type': '[VirtualMachineStatusCodeCount]'},
    }

    def __init__(self, **kwargs) -> None:
        super(VirtualMachineScaleSetInstanceViewStatusesSummary, self).__init__(**kwargs)
        self.statuses_summary = None
