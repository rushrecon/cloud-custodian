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


class OSDiskImage(Model):
    """Contains the os disk image information.

    All required parameters must be populated in order to send to Azure.

    :param operating_system: Required. The operating system of the
     osDiskImage. Possible values include: 'Windows', 'Linux'
    :type operating_system: str or
     ~azure.mgmt.compute.v2016_04_30_preview.models.OperatingSystemTypes
    """

    _validation = {
        'operating_system': {'required': True},
    }

    _attribute_map = {
        'operating_system': {'key': 'operatingSystem', 'type': 'OperatingSystemTypes'},
    }

    def __init__(self, *, operating_system, **kwargs) -> None:
        super(OSDiskImage, self).__init__(**kwargs)
        self.operating_system = operating_system
