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


class Region(Model):
    """Class representing a region in the Geographic hierarchy used with the
    Geographic traffic routing method.

    :param code: The code of the region
    :type code: str
    :param name: The name of the region
    :type name: str
    :param regions: The list of Regions grouped under this Region in the
     Geographic Hierarchy.
    :type regions: list[~azure.mgmt.trafficmanager.models.Region]
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'regions': {'key': 'regions', 'type': '[Region]'},
    }

    def __init__(self, *, code: str=None, name: str=None, regions=None, **kwargs) -> None:
        super(Region, self).__init__(**kwargs)
        self.code = code
        self.name = name
        self.regions = regions
